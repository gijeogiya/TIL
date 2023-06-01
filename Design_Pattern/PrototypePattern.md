# Prototype Pattern
## 프로토타입 패턴
- 기존 인스턴스를 복제하여 새로운 인스턴스를 만드는 방법
- 복제 기능을 갖추고 있는 기존 인스턴스를 프로토타입으로 사용해 새 인스턴스를 만들 수 있다
![image](https://github.com/gijeogiya/TIL/assets/97646078/92c38d54-54ee-4657-b2d8-c2e7f5a2549d)
## 프로로타입 패턴 구현 방법
![image](https://github.com/gijeogiya/TIL/assets/97646078/abca984b-3811-4c4a-bc18-f8409df51170)
프로토타입의 매커니즘은 매우 단순하다
객체를 새롭게 생성하는데 큰 리소스가 드는 객체의 값을 모두 복제해 새로운 인스턴스를 만든는 것이 프로토타입 패턴이다
값을 복제하기 때문에 2가지 특징을 만족해야 한다
1. clone != gitHubIssue → 다른 인스턴스가 새로 만들어지기 때문에 clone 한 객체는 기존 객체와 다른 객체여야 한다
2. clone.equals(githubIssie) = true → 값을 모두 동일하게 복제하기 때문에 equals() 는 true 여야 한다

- 프로토타입 패턴은, 기존의 다른 패턴과 다르게 새롭게 구현하지 않고 Java 에서 제공해주는 clone( ) 기능을 그대로 사용해준다고 한다.
**Objects.class clone( )** 
- 기본적으로 자바가 제공하는 clone() 메소드를 이용해서 프로토타입 패턴을 구현할 수 있다
- Object.class에서 제공하는 clone() protected 접근제어자로 정의가 되어있기 때문에 clone( ) 을 사용하고자하는 객체에서 재정의해서 사용하여야 한다
- Object.class 의 clone() 은 얕은 복사(shallow copy) 를 제공한다.
- 깊은 복사(deep copy)를 하고 싶다면, 자바에서 제공하는 clone( ) 메소드를 그대로 사용하지않고 새로 정의해야 한다.

## 프로토타입 패턴 장단점
### 장점
- 복잡한 객체를 만드는 과정을 숨길 수 있다
- 기존 객체를 복제하는 과정이 새 인스턴스를 만드는 것보다 비용(시간 또는 메모리)적인
면에서 효율적일 수도 있다
- 추상적인 타입을 리턴할 수 있다
### 단점
- 복제한 객체를 만드는 과정 자체가 복잡할 수 있다 (특히, 순환 참조가 있는 경우)
## 실무에서 어떻게 쓰이나?
- 자바 Object 클래스의 clone 메소드와 Cloneable 인터페이스
- shallow copy와 deep copy
- ModelMapper
