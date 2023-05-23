# AbstractFactoryPattern
## 추상 팩토리 패턴이란?
- 서로 관련이 있는 객체들을 통째로 묶어서 팩토리 클래스로 만들고, 이들 팩토리를 조건에 따라 생성하도록 다시 팩토리를 만들어서 객체를 생성하는 패턴
- 서로 관련있는 여러 객체를 만들어주는 인터페이스.
- 구체적으로 어떤 클래스의 인스턴스를(concrete product)를 사용하는지 감출 수 있다.
![image](https://github.com/gijeogiya/TIL/assets/97646078/9a8ba94c-71ea-4774-8ba2-7353654099da)
## 특징
- 클라이언트 코드에서 구체적인 클래스의 의존성을 제거한다.
![image](https://github.com/gijeogiya/TIL/assets/97646078/144256bd-2d24-4049-9764-524ec785c2ea)
## 팩토리 메서드 패턴과의 비교
- 모양과 효과는 비슷하지만 아래와 같은 공통점과 차이점이 존재함
  - 둘 다 구체적인 객체 생성 과정을 추상화한 인터페이스를 제공
  - 관점이 다름
    - 팩토리 메소드 패턴은 **팩토리를 구현하는 방법 (inheritance)**에 초점을 둠
    - 추상 팩토리 패턴은 **팩토리를 사용하는 방법 (composition)**에 초점을 둠
  - 목적이 조금 다름
    - 팩토리 메소드 패턴은 구체적인 객체 생성 과정을 하위 또는 구체적인 클래스로 옮기는 것이 목적
    - 추상 팩토리 패턴은 관련있는 여러 객체를 구체적인 클래스에 의존하지 않고 만들 수 있게 해주는 것이 목적
### 팩토리 메서드 패턴
- 조건에 따른 객체 생성을 팩토리 클래스로 위임하여, 팩토르 클래스에서 객체를 생성하는 패턴
- 추상 팩토리 패턴은 어떻게 보면, 팩토리 메서드 패턴을 좀 더 캡슐화한 방식이라고 볼 수 있음
### 팩토리 메소드 패턴의 예시 코드
```java
public interface ShipFactory {

    Ship createShip();
}
```
팩토리 메소드 패턴은 product와 createor간의 의존성을 낮추는것을 목적으로, 서브 클래스인 concreator에게 의존성을 위임
### 추상 팩토리 패턴의 예시 코드
```java
public interface ShipPartsFactory {
    Anchor createAnchor();

    Wheel createWheel();
}
```
추상 팩토리 패턴은 여러 객체의 생성이 있을때 여러 객체의 의존성을 낮추기 위해, 마찬가지로 서브 클래스인 concreator에게 의존성을 위임
## 실무에서는 어떻게 쓰는가?
- 자바 라이브러리
  - javax.xml.xpath.XPathFactory#newInstance()
  - javax.xml.transform.TransformerFactory#newInstance()
  - javax.xml.parsers.DocumentBuilderFactory#newInstance()
- 스프링
  - FactoryBean과 그 구현체
