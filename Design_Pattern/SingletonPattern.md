# Singleton

## SingletonPattern

### SingletonPattern

- class의 instance가 딱 1개만 생성되는 것을 보장하는 design pattern이다.
- 그래서 객체 instance를 2개 이상 생성하지 못하도록 막아야 한다.
- private 생성자를 사용해서 외부에서 임의로 new 키워드를 사용하지 못하도록 막아야 한다

### SingletonPattern 문제점

- SingletonPattern을 구현하는 코드 자체가 많이 들어간다.
- 의존관계상 클라이언트가 구체 class에 의존한다. DIP를 위반한다.
- 클라이언트가 구체 class에 의존해서 OCP 원칙을 위반할 가능성이 높다.
- test가 어렵다.
- 내부 속성을 변경하거나 초기화 하기 어렵다.
- private 생성자로 자식 class를 만들기 어렵다.
- 유연성이 떨어진다.
- anti pattern으로 불리기도 한다

## SingletonContainer

### SingletonContainer

Spring Container는 Singleton Pattern의 문제점을 해결하면서,
객체 인스턴스를 Singleton Pattern(1개만 생성)으로 관리한다.

### SingletonContainer 특징

- Spring Container는 Singleton 패턴을 적용하지 않아도, 객체 instance를 Singleton으로 관리한다.
- 이전에 설명한 Container 생성 과정을 자세히 보자. Container는 객체를 하나만 생성해서 관리한다.
- Spring Container는 Singleton Container 역할을 한다. 이렇게 Singleton 객체를 생성하고 관리하는 기능을 Singleton 레지스트리라 한다.
- Spring Container의 이런 기능 덕분에 Singleton 패턴의 모든 단점을 해결하면서 객체를 Singleton으로 유지할 수있다.
- Singleton Pattern을 위한 지저분한 코드가 들어가지 않아도 된다.
- DIP, OCP, 테스트, Private 생성자로 부터 자유롭게 싱글톤을 사용할 수 있다.

## Singleton 주의점

- Singleton Pattern이든, Spring과 같은 Singleton Container를 사용하든, 객체 인스턴스를 하나만 생성해서 공유하는
  Singleton 방식은 여러 클라이언트가 하나의 같은 객체 instance를 공유하기 때문에 싱글톤 객체는 상태를 유지
  (Stateful)하게 설계하면 안된다.
- 무상태(Stateless)로 설계해야 한다.
- 특정 클라이언트에 의존적인 필드가 있으면 안된다.
- 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안된다.
- 가급적 읽기만 가능해야 한다.
- 필드 대신에 JAVA에서 공유되지 않는, 지역변수, 파라미터, ThreadLocal 등을 사용해야 한다.
- Spring Bin의 필드에 공유 값을 설정하면 정말 큰 장애가 발생할 수 있다.
