# Java 04: 객체지향

**2023.01.10**

## 객체지향

### 객체지향 기초

#### 객체의 개념

- 소프트웨어 객체는 현실 세계의 객체를 필드와 메서드로 모델링한 것
- 소프트웨어 객체는 상태를 필드(Field)로 정의하고, 동작을 메서드(Method)로 정의.
- 필드는 객체 내부에 선언된 변수를 의미하고, 메서드는 객체 내부에  정의된 동작

#### 절차 지향 프로그래밍

- 일련의 동작을 순서에 맞추어 단계적으로 실행하도록 명령어를 나열
- 데이터를 정의하는 방법보다는 명령어의 순서와 흐름에 중점
- 수행할 작업을 예상할 수 있어 직관적인데, 규모가 작을 때는 프로그래밍과 이해하기가 용이
- 소프트웨어는 계산 위주이므로 절차 지향 프로그래밍이 적합

#### 객체 지향 프로그래밍

- 소프트웨어의 규모가 커지면서 동작과 분리되어 전 과정에서 서로 복잡하게 얽혀 있는 데이터를 사용했기 때문에 절차 지향 프로그래밍 방식의 한계
- 절차 지향 프로그램은 추후 변경하거나 확장하기도 어려움
- 현실 세계를 객체 단위로 프로그래밍하며, 객체는 필드(데이터)와 메서드(코드)를 하나로 묶어 표현
- 객체지향언어 = 프로그래밍 언어 + 객체지향개념(규칙)
- Object Oriented Programming
  - 캡슐화, 상속, 추상화, **다형성**

#### 객체와 클래스

- 클래스: 객체를 정의해 놓은 것으로 객체를 생성하는데 사용
- 객체: 실제로 존재하는 것, 사물 또는 개념으로 객체가 가지고 있는 기능과 속성에 따라 용도가 다름

![image-20230110140409465](C:\Users\LDCCHRD_\Desktop\Java 04.assets\image-20230110140409465.png)

### 클래스 선언과 객체 생성

#### 특징

- 캡슐화(정보 은닉): 관련된 필드와 메서드를 하나의 캡슐처럼 포장해 세부 내용을 외부에서 알 수 없도록 감추는 것
- 상속: 자녀가 부모 재산을 상속받아 사용하듯이 상위 객체를 상속받은 하위 객체가 상위 객체의 메서드와 필드를 사용하는 것 (상속은 개발된 객체를 재사용하는 방법 중 하나)
- 다형성: 대입되는 객체에 따라서 메서드를 다르게 동작하도록 구현하는 기술. 실행 도중 동일한 이름의 다양한 구현체 중에서 메서드를 선택 가능
- 추상화: 현실 세계의 객체에서 불필요한 속성을 제거하고 중요한 정보만 클래스로 표현하는 일종의 모델링 기법
  - 현실 세계의 객체는 수많은 상태가 있고 다양한 동작을 하지만, 클래스에 모두 포함하기는 어렵기에 추상화(Abstraction)하는 과정이 필요.
  - 사람마다 추상화하는 기법이 같지 않으므로 각 개발자는 클래스를 다르게 정의 가능

#### 클래스 선언

- 형식

```java
class 클래스이름 {
	// 필드
	// 메서드
}
```

- 예

```java
public class Ball {
	double radius = 2.0;
	double getVolume() {
		return 4 / 3 * 3.14 * radius * radius * radius;
	}
}
```

#### 클래스 선언과 파일

- 보통 소스 파일마다 하나의 클래스를 선언하지만, 2개 이상의 클래스를 하나의 파일로 선언 가능
- 하나의 파일에 클래스가 둘 이상 있다면 하나만 public으로 선언할 수 있고, 해당 클래스 이름은 소스 파일 이름과 동일해야 함

#### 객체 생성과 참조 변수

```java
클래스이름 변수;
변수 = new 클래스이름();

// 한 문장으로 변수 선언과 객체 생성
클래스이름 변수 = new 클래스이름();
```

#### 기초 타입과 참조 타입

```java
int tem = 10;
Ball myBall = new Ball();
```

```java
class Phone {
  String name;
  int value;

  void print(){
    System.out.println(value + "만원 짜리 " + name + " 스마트폰");
  }
}

public class PhoneDemo {
  public static void main(String[] args) {
    Phone myPhone = new Phone();
    myPhone.name = "아이폰11 프로";
    myPhone.value = 85;
    myPhone.print();

    Phone myNewPhone = new Phone();
    myNewPhone.name = "갤럭시 폴드2";
    myNewPhone.value = 153;
    myNewPhone.print();
  }
}
```

### 클래스의 구성 요소와 멤버 접근

#### 클래스의 구성요소와 멤버 접근

- 클래스의 구성 요소
  - 멤버: 필드, 메서드
  - 생성자
  - 참고: 지역 변수는 메서드 내부에 선언된 변수. 매개 변수도 일종의 지역 변수임

#### 필드와 메서드 접근

- 예를 들어, 클래스가 radius 필드와 findArea( ) 메서드를 포함한다면 클래스 내부에서는 다음과 같 이 그대로 사용하면 된다.
- `radius` 혹은 `this.radius` : 필드 이름
- `findArea` 혹은 `this.findArea` : 필드 이름

```java
class Phone {
  String name;
  int value;

  Phone(String name, int value){
    this.name = name;
    this.value = value;
  }
  void print(){
    System.out.println(value + "만원 짜리 " + name + " 스마트폰");
  }
}

public class PhoneDemo {
  public static void main(String[] args) {
    Phone myPhone = new Phone("아이폰11 프로", 85);
    myPhone.print();

    Phone myNewPhone = new Phone("갤럭시 폴드2", 153);
    myNewPhone.print();
  }
}
```

### 접근자와 설정자

- 클래스 내부에 캡슐화된 멤버를 외부에서 사용할 필요가 있음
- private으로 지정된 필드에 값을 반환하는 접근자와 값을 변경하는 설정자는 공개된 메서드
- 일반적으로 접근자는 get, 설정자는 set으로 시작하는 이름을 사용
- 필드 이름을 외부와 차단해서 독립시키기 때문에 필드 이름 변경이나 데이터 검증도 가능

```java
public class GetSetDemo {
  public static void main(String[] args) {
    Circle c = new Circle();
    c.setRadius(30);
    System.out.println(c.getRadius());
    System.out.printf("%.2f\n",c.findArea());

    c.setRadius(0);
    System.out.println(c.getRadius());
    System.out.printf("%.2f\n",c.findArea());
  }
}

class Circle {
  private int radius;

  public int getRadius(){ //접근자, getter
    return this.radius;
  }

  public void setRadius(int radius){ //설정자, setter
    if(radius == 0) System.out.println("원의 반지름은 0보다 커야 합니다.");
    else if(radius > 100) System.out.println("원지름의 반지름은 100보다 작아야 합니다.");
    else this.radius = radius;
  }
  double findArea(){
    return 3.14 * radius * radius;
  }
}
```

### 생성자

#### 생성자의 의미와 선언

- 생성자의 역할: 객체를 생성하는 시점에서 필드를 다양하게 초기화
- 생성자의 선언 방식: `클래스이름 (...){...}` (일반적으로 공개되어야 하므로 public으로 선언되지만 아닐 수도 있다.)
- 생성자 사용
  - 생성자 이름은 클래스 이름과 같다.
  - 생선자의 반환 타입은 없다.
  - 생성자는 new 연산자와 함께 사용하며, 객체를 생성할 때 호출한다.
  - 생성자도 오버로딩할 수 있다.

#### 디폴트 생성자

- 모든 클래스는 최소한 하나의 생성자가 있음
- 만약 생성자를 선언하지 않으면 컴파일러가 자동으로 디폴트 생성자를 추가

- 오버로딩하는 경우 디폴트 생성자를 자동으로 만들어주지는 않음

#### this와 this()

```java
public class Constructor {
  public static void main(String[] args) {
    Circle2 c = new Circle2();
    System.out.println(c.color); //파랑
    System.out.println(c.radius); //20.0
  }
}

class Circle2{
  String color = "";
  double radius = 10.0;
  Circle2(){ // 디폴트
    this(10.0); //생성자로 인스턴스 만들어지고 나서,
    this.color = "파랑"; //인스턴스에 접근해야한다. 즉, this()가 먼저 와야한다.
  }
  Circle2(double radius){
    this.radius = radius * 2;
    this.color = "빨강";
  }
  Circle2(String color){
    this.radius = 5.0;
    this.color = color;
  }
}
```

#### 연속 호출

- 예를 들어 반환 타입이 void인 setName(String name), setAge(), sayHello()라는 메서드를 가진 Person 클래스가 있다고 가정

```java
Person person = new Person();
person.setName("기정");
person.setAge(30);
person.sayHello();
```

- 메서드를 호출할 때마다 새로운 실행문을 사용해야하므로 번거롭고 가독성도 떨어진다.

```java
public class MethodChain {
  public static void main(String[] args) {
    Person giJeong = new Person();
    //기존 방식
    giJeong.setName("기정");
    giJeong.setAge(30);
    giJeong.sayHello();
    
    //메서드 체인잉
    giJeong.setName("기정").setAge(30).sayHello();
  }
}

class Person{
  private String name = "";
  private int age;
  public Person setName(String name){
    this.name = name;
    return this; //인스턴스 스스로를 리탄하게 하여 체이닝하는 방식
  }
  public Person setAge(int age){
    this.age = age;
    return this; //인스턴스 스스로를 리탄하게 하여 체이닝하는 방식
  }
  public void sayHello(){
    System.out.println("이름은 " + name + "이고 나이는 " + age + "입니다.");
  }
}
```

#### 선언위치에 따른 변수의 종류

> 멤버 = 변수 + 메서드

- 인스턴스 변수(인스턴스 멤버)
  - 각 인스턴스의 개별적인 저장공간. 인스턴스마다 다른 값 저장가능
  - 인스턴스 생성 후, `참조변수.인스턴스변수명`으로 접근
  - 인스턴스를 생성할 때 생성되고, 참조변수가 없을 때 가비지컬렉터에 의해 자동으로 제거됨
- 클래스 변수(정적 멤버) - static 키워드 사용
  - 같은 클래스의 모든 인스턴스들이 공유하는 변수
  - 인스턴스 생성없이 `클래스이름.클래스변수명`으로 접근
  - 클래스가 로딩될 때 생성되고 프로그램이 종료될 때 소멸
- 지역 변수(멤버)
  - 메서드 내에 선언되며, 메서드의 종료와 함께 소멸
  - 조건문, 반복문의 블럭`{}` 내에 선언된 지역변수는 블럭을 벗어나면 소멸

```java
public class PracticeCircles {
  public static void main(String[] args) {
    PracticeCircle Circle1 = new PracticeCircle();
    PracticeCircle Circle2 = new PracticeCircle("노랑");
    PracticeCircle Circle3 = new PracticeCircle(80);
    PracticeCircle Circle4 = new PracticeCircle("노랑", 80);
    Circle3.setColor("노랑").setRadius(24).Check();
    System.out.println(Circle2.getColor());
    System.out.println(Circle2.getRadius());
  }
}

class PracticeCircle{
  private int radius;
  private String color = "";
  static private int numberOfCircles = 0;
  PracticeCircle() {
    this.color = "빨강";
    this.radius = 100;
    this.numberOfCircles++;
    this.Print();
  }

  PracticeCircle(int radius) {
    this.color = "빨강";
    this.radius = radius;
    this.numberOfCircles++;
    this.Print();
  }

  PracticeCircle(String color) {
    this.color = color;
    this.radius = 100;
    this.numberOfCircles++;
    this.Print();
  }

  PracticeCircle(String color, int radius) {
    this.color = color;
    this.radius = radius;
    this.numberOfCircles++;
    this.Print();
  }


  public PracticeCircle setColor(String color){
    this.color = color;
    return this;
  }

  public PracticeCircle setRadius(int radius){
    this.radius = radius;
    return this;
  }

  public int getRadius(){
    return this.radius;
  }

  public String getColor(){
    return this.color;
  }

  public void Check(){
    System.out.println(this.radius + " 크기의 " + this.color + "색의 공으로 셋팅 되었습니다.");
  }

  public void Print(){
    System.out.println(this.radius + " 크기의 " + this.color + "색의 공이 생성 되었습니다. 공의 갯수는 총 " + this.numberOfCircles +"개 입니다.");
  }
}
```

