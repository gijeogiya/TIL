# Async
## 비동기(Asynchronous)
- 비동기란 요청과 결과가 동시에 일어나지 않는다는 뜻이다.
- 즉 작업을 요청하고 해당 요청에 대한 결과를 기다리지 않아도 된다. 그렇기에 작업들을 병렬적으로 처리할 수 있다.
- 아래 그림은 동기/비동기의 작업 처리를 나타낸 그림이다.
![image](https://github.com/user-attachments/assets/cb55014b-091e-47f8-b6dc-f20374ceeaae)
## @Async
- Spring에서는 `@Async` 어노테이션을 제공하여 로직의 비동기 처리를 지원한다.
### 간단하게 사용하기
- `SpringBootApplication`에서 `@EnableAsync` 어노테이션를 적용하여 사용한다.
```java
@EnableAsync
@SpringBootApplication
public class MySpringApplication {
	...
}
```
- 후에 메소드에 @Async 어노테이션을 명시하기만하면 태스크 처리를 비동기 방식으로 할 수 있다.
```java
public class AsyncService {
    @Async
    public void asyncMethod(){
    	...
    }
}
```
- 이렇게 간단하게 설정한다면 Thread Executor로 `SimpleAsyncTaskExecutor` 를 사용할 수 있다. 간단하게 `SimpleAsyncTaskExecutor` 에 대해 정리해보면 아래와 같다.
  - `org.springframework.core.task.SimpleAsyncTaskExecutor` 패키지에 존재
  - 각 작업마다 새로운 Thread를 생성하고 비동기방식으로 동작
  - `concurrencyLimit` 프로퍼티를 이용해 지정한 수 보다 요청이 넘어설 경우 제한. default는 `unlimit`
  - `simpleAsyncTaskExecutor`는 Thread를 재사용 하지않음!
`SimpleAsyncTaskExecutor` 은 Thread pool 방식의 Executor가 아니다. 그렇다보니 위에 설명한것처럼 Thread를 재사용하지 않는다. 공식 문서에서는 Thread pool 방식의 TaskExecutor를 사용하기를 고려해보기를 권장한다. 특히 실행시간이 짧은 많은량의 태스크를 처리해야할때 더욱 필요하다.     
### 유의사항
`@Async` 을 사용할 때는 다음 내용을 지켜서 사용해야한다.   
- method 접근지정자 private 사용 불가
- self-invocation(자가 호출) 불가, 즉 inner method는 사용 불가
두 가지 유의사항을 지켜야하는 이유를 설명하려면 @Async가 동작하는 방식을 알아볼 필요가 있다.     
### 작동 방식
`@Async`는 Spring AOP에 의해서 프록시 방식으로 작동된다.     
![image](https://github.com/user-attachments/assets/3605388d-77d9-4761-9ce3-abdb031a9f89)      
Spring Context에 등록되어있는 Async Bean이 호출되면 Spring이 개입하여 해당 Async Bean을 프록시 객체로 Wrapping 한다. 정확히 말하면 컨테이너에 의해 Bean으로 등록되는 시점에 프록시 객체화 하는 것이다. 호출한 객체는 실질적으로 AOP를 통해 만들어진 프록시 객체화된 Async Bean을 참조하게 된다. 즉, 위의 그림에서는 Caller Method B는 Proxy 객체의 Method A를 호출하게 되는 것이다.       
     
그렇다면 이제 위에서 설명한 유의사항들을 설명할 수 있다.     
     
- 위의 그림에서 Method A가 private으로 지정되어 있다면 AOP가 가로채서 프록시 객체로 만들때 Method A에 접근할 수 없으므로 private method는 사용할 수 없다.
- Self-Invocation(자가 호출)의 경우에는 프록시 객체를 거치지 않고 직접 Method A를 호출하기 때문에 Async가 동작하지 않는다.     
### 작동 예시
이제 `@Async`가 정삭적으로 작동하는 경우와 아닌 경우에 대해 살펴보자.       
#### 1. 정상 작동
##### 코드
```java
...
public class CallerService {

    private final AsyncService asyncService;

    /* 정상적으로 Async 호출 */
    public void callAsync(){
        log.info("[Async Method 정상호출]");
        asyncService.asyncReceiver1();
        asyncService.asyncReceiver2();
    }
}

...
public class AsyncService{

    @Async("taskExecutor1")
    public void asyncReceiver1(){
        log.info("[asyncReceiver1()]");
        for(int i=0;i<5;i++){
            log.info("::::::Thread Name : " + Thread.currentThread().getName());
        }
    }

    @Async("taskExecutor2")
    public void asyncReceiver2(){
        log.info("[asyncReceiver2()]");
        for(int i=0;i<5;i++){
            log.info("::::::Thread Name : " + Thread.currentThread().getName());
        }
    }
}
```
##### 출력결과
![image](https://github.com/user-attachments/assets/35afa44d-7ea7-4780-b777-ea627cc822c9)      
taskExecutor1, taskExecutor2 두개의 스레드가 순서와 관계없이 비동기식으로 처리된 결과를 볼 수 있다.     
#### 2. 호출하는 클래스 내부에 있는 Async 메소드를 직접 호출하는 경우
##### 코드
```java
...
public class AsyncService{

	/* 같은 클래스에 있는 async 메소드 호출 */
	public void callInnerAsync(){
        log.info("[내부 클래스의 Async 메소드 호출]");
        this.asyncReceiver1();
        this.asyncReceiver2();
    }

    @Async("taskExecutor1")
    public void asyncReceiver1(){
        log.info("[innerAsyncReceiver1()]");
        for(int i=0;i<5;i++){
            log.info("::::::Thread Name : " + Thread.currentThread().getName());
        }
    }

    @Async("taskExecutor2")
    public void asyncReceiver2(){
        log.info("[innerAsyncReceiver2()]");
        for(int i=0;i<5;i++){
            log.info("::::::Thread Name : " + Thread.currentThread().getName());
        }
    }
}
```
##### 출력결과
![image](https://github.com/user-attachments/assets/c29a20b8-f21f-4b03-b525-314e0d606936)      
결과를 보면 출력이 순차적으로 이루어져 있다. 비동기식으로 작동하지 않은 것이다. 위에 설명한 것 처럼 내부 호출(self-invocation)을 할 경우 프록시 객체를 거치지 않기 때문에 비동기 처리가 되지 않는다. 다음 그림과 같은 형태가 되어버린다.     
![image](https://github.com/user-attachments/assets/ae136abc-5b67-4beb-91be-d70c810cd4dc)
#### 3. 생성자로 생성한 객체의 Async 메소드 호출
##### 코드
```java
...
public class CallerService {
	...
    /* 생성자로 생성하여 Async 메소드 호출 */
    public void callAsyncWithConstructor(){
        AsyncService asyncServiceWithConstructor = new AsyncService();
        log.info("[생성자를 통한 Async 메소드 호출]");
        asyncServiceWithConstructor.asyncReceiver1();
        asyncServiceWithConstructor.asyncReceiver2();
    }
}

...
public class AsyncService{

    @Async("taskExecutor1")
    public void asyncReceiver1(){
        log.info("[asyncReceiver1()]");
        for(int i=0;i<5;i++){
            log.info("::::::Thread Name : " + Thread.currentThread().getName());
        }
    }

    @Async("taskExecutor2")
    public void asyncReceiver2(){
        log.info("[asyncReceiver2()]");
        for(int i=0;i<5;i++){
            log.info("::::::Thread Name : " + Thread.currentThread().getName());
        }
    }
}
```
##### 출력결과
![image](https://github.com/user-attachments/assets/ad37d49b-ec9f-47b1-8fea-b247f0d9e92c)      
3번 결과의 경우도 2번 결과와 비슷하며 제대로 작동하지 않는 원리 또한 비슷하다. 직접 생성자를 이용해 생성함으로써 Bean에 등록이 되지않았고 그렇기에 AOP가 프록시 객체로 만들지 못한다.
## 정리
- 비동기는 요청에 대한 결과를 기다리지 않으므로 작업을 병렬처리가 가능하다.
- `@Async`는 스프링에서 제공하는 비동기 처리 어노테이션이다.
- `SimpleAsyncTaskExecutor`는 Thread pool 방식이 아니기 때문에 Thread pool 방식의 Executor를 쓰자
- `@Async`를 사용할 때는 private 쓰지 말고 자가 호출(self-invocation)하지 말자
- `@Async` 메소드가 호출되면 스프링 AOP에 의해 해당 메소드를 포함한 객체를 Wrapping한 프록시 객체가 만들어지고 호출자는 만들어진 프록시 객체를 참조한다.


