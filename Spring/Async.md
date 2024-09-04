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
`SimpleAsyncTaskExecutor` 은 Thread pool 방식의 Executor가 아니다. 그렇다보니 위에 설명한것처럼 Thread를 재사용하지 않습니다. 공식 문서에서는 Thread pool 방식의 TaskExecutor를 사용하기를 고려해보기를 권장한다. 특히 실행시간이 짧은 많은량의 태스크를 처리해야할때 더욱 필요하다.     
### 유의사항
`@Async` 을 사용할 때는 다음 내용을 지켜서 사용해야한다.   
- method 접근지정자 private 사용 불가
- self-invocation(자가 호출) 불가, 즉 inner method는 사용 불가
두 가지 유의사항을 지켜야하는 이유를 설명하려면 @Async가 동작하는 방식을 알아볼 필요가 있다.     
### 작동 방식
`@Async`는 Spring AOP에 의해서 프록시 방식으로 작동된다.     
![image](https://github.com/user-attachments/assets/3605388d-77d9-4761-9ce3-abdb031a9f89)
Spring Context에 등록되어있는 Async Bean이 호출되면 Spring이 개입하여 해당 Async Bean을 프록시 객체로 Wrapping 한다. 정확히 말하면 컨테이너에 의해 Bean으로 등록되는 시점에 프록시 객체화 하는 것이다. 호출한 객체는 실질적으로 AOP를 통해 만들어진 프록시 객체화된 Async Bean을 참조하게 된다. 즉, 위의 그림에서는 Caller Method B는 Proxy 객체의 Method A를 호출하게 되는 것이다.      
자 그렇다면 이제 위에서 설명한 유의사항들을 설명할 수 있다.    
위의 그림에서 Method A가 private으로 지정되어 있다면 AOP가 가로채서 프록시 객체로 만들때 Method A에 접근할 수 없으므로 private method는 사용할 수 없다.      
self-invocation(자가 호출)의 경우에는 프록시 객체를 거치지 않고 직접 Method A를 호출하기 때문에 Async가 동작하지 않는다.     
