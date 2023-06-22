# FacadePattern
## FacadePattern이란?
- 클라이언트가 사용해야 하는 복잡한 서브 시스템 의존성을 간단한 인터페이스로 추상화 하는 패턴
- Facade는 "건물의 정면"을 의미하는 단어로 어떤 소프트웨어의 다른 커다란 코드 부분에 대하여 간략화된 인터페이스를 제공해주는 디자인 패턴을 의미
- 퍼사드 객체는 복잡한 소프트웨어 바깥쪽의 코드가 라이브러리의 안쪽 코드에 의존하는 일을 감소시켜 주고, 복잡한 소프트웨어를 사용 할 수 있게 간단한 인터페이스를 제공
- 복잡한 서브 시스템 의존성을 최소화하는 것이 목적
![image](https://github.com/gijeogiya/TIL/assets/97646078/f12f0dc5-309b-49d6-bf37-f1677486700a)
![image](https://github.com/gijeogiya/TIL/assets/97646078/a25e9db5-fe7a-4b5d-8648-7740c7ff5dcc)
## FacadePattern 예시 코드
### 동기
어떤 사람이 영화를 보고자 한다. 영화를 보기 위해서는 다음과 같은 과정을 거치게 된다.
음료를 준비한다 -> TV를 켠다 -> 영화를 검색한다 -> 영화를 결제한다 -> 영화를 재생한다.
```java
public void view()
{
     Beverage beverage = new Beverage("켈리");
     Remote_Control remote= new RemoteControl();
     Movie movie = new Movie("범죄도시3");
       
     beverage.prepare();  //음료 준비
     remote.turnOn();   //tv를 켜다
     movie.searchMovie();  //영화를 찾다
     movie.chargeMovie();  // 영화를 결제하다
     movie.playMovie();   //영화를 재생하다
}
```

사용자 입장에서는 영화를 보기위해서는 저런 복잡한 코드를 사용하여 영화를 봐야만 한다. 여기서 퍼사드 객체가 등장하게 되는데 퍼사드는 이런 사용자와 영화를 보기위해 사용하는 서브 클래스들 사이의 간단한 통합 인터페이스를 제공해주는 역할을 하게 된다.
![image](https://github.com/gijeogiya/TIL/assets/97646078/7629bf51-8c6a-45b2-aed7-cb7c5df23d86)
Client 입장에서는 Facde 객체에서 제공하는 doSomething() 메서드를 호출함으로써 복잡한 서브 클래스의 사용을 도와주고 있다.

해당 상황의 전체 코드
- RemoteControl.java  //리모컨을 조작하는 클래스 - 복잡한 서브 클래스들 중 하나
```java
public class RemoteControl {
    
    public void turnOn()
    {
        System.out.println("TV를 켜다");
    }
    public void turnOff()
    {
        System.out.println("TV를 끄다");
    } 
}
```
- Movie.java  //영화 재생과 관련된 클래스 - 마찬가지로 복잡한 서브 클래스들 중 하나
```java
public class Movie {
    
    private String name="";
    
    public Movie(String name)
    {
        this.name = name;
    }
    
    public void searchMovie()
    {
        System.out.println(name+" 영화를 찾다");
    }
    
    public void chargeMovie()
    {
        System.out.println("영화를 결제하다");
    }
    public void playMovie()
    {
        System.out.println("영화 재생");
    } 
}
```
- Beverage.java  //음료를 제공하는 클래스 - 복잡한 서브 클래스들 중 하나
```java
public class Beverage {
    
    private String name="";
    
    public Beverage(String name)
    {
        this.name = name;
    }
    
    public void prepare()
    {
        System.out.println(name+" 음료 준비 완료 ");
    }
}
```

- Facade.java  //가장 중요한 Facade 클래스 - 복잡한 서브 클래스들에 대한 인스턴스를 가지며 복잡한 호출 방식에 대하여 viewMovie() 메서드내에서 구현
```java
public class Facade {
    
    private String BeverageName="";
    private String MovieName="";
    
    public Facade(String BeverageName, String MovieName)
    {
        this.BeverageName=BeverageName;
        this.MovieName=MovieName;
    }
    
    public void viewMovie()
    {
        Beverage beverage = new Beverage(BeverageName);
        RemoteControl remote= new RemoteControl();
        Movie movie = new Movie(MovieName);
        
        beverage.prepare();
        remote.turnOn();
        movie.searchMovie();
        movie.chargeMovie();
        movie.playMovie();
    }
}
```

Viewer.java  //사용자 입장에서는 이제 서브 클래스에 대해서 알 필요가 없음. 단지 Facde 객체의 viewMovie() 메서드를 호출하면서 서브 클래스들의 복잡한 기능을 수행 할 수 있기 떄문.
```java
public class Facade {
    
    public void view()
    {
        Facade facade = new Facade("켈리","범죄도시3");
        facade.viewMovie();
        //"켈리 음료 준비 완료"
        //"tv를 켜다"
        //"범죄도시3 영화를 찾다"
        //"영화를 결제하다"
        //"영화를 재생하다"
    }
```

## 장단점
### 장점
- 서브 시스템에 대한 의존성을 한곳으로 모을 수 있다.
### 단점
- 퍼사드 클래스가 서브 시스템에 대한 모든 의존성을 가지게 된다.

## 실무에서의 예시
- Spring
  - Spring MVC
  - Spring이 제공하는 대부분의 기술 독립적인 인터페이스와 그 구현체
