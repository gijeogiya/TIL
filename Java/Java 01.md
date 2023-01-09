# Java 01: 자바 시작하기

**2023.01.09**

## 자바 시작하기
### 자바 소개
#### 소개
- 객체지향 프로그래밍을 배우기 가장 적합한 언어
- 비교적 데이터형을 까다롭게 관리
- JRE는 실행 환경
- JDK는 개발+실행 환경
- API = 라이브러리
- 멀티스레드 제공
- 우리는 Java 17 버전을 사용할 예정
- 개발 환경은 IntelliJ를 사용할 예정
#### 특징
- 객체 지향 언어이다.
- 함수형 코딩을 지원한다.
- 플랫폼 독립적이다.
- 분산 처리를 지원한다.
- 멀티스레딩을 지원한다.
#### 활용 분야
- PC On 프로그램(IntelliJ 등) 개발
- 웹 어플리케이션은 물론 CRM, ERP, SCM 등 기업용 애플리케이션
- 안드로이드 어플리케이션 개발
## 자바 기초 문법
```java
public class Main {
  public static void main(String[] args) {
    System.out.println("hello")
    ;
  }
}
```

### 주석

`//`
`/* */`
`/** */`

### 식별자
#### 규칙
- 문자, 언더바`_`, `$`로 시작해야 한다. 한글로도 가능하며, 영문자는 대소문자 구분
- `+`, `-` 등 연산자를 포함하면 안된다.
- 자바 키워드를 사용하면 안된다.
- 길이 제한이 없다.
#### 자바 키워드
데이터 타입, 접근 지정자, 제어문, 클래스와 객체, 예외 처리, 기타 등
#### 관례
- 변수와 메서드는 모두 소문자로 표기
- 클래스와 인터페이스는 첫글자를 대문자로 표기
- 상수는 전체를 대문자로 표기. 단 복합 단어일 경우 언더바`_`로 연결
### 데이터 타입
#### 의미
- 값과 값을 다룰 수 있는 연산의 집합을 의미
- 기본형: 8개, **실제 값을 저장**
- 참조형: 기본형을 제외한 나머지, **메모리 주소를 저장**
#### 기억 공간 크기 및 기본 값
- 1비트 : 2진수, 1자리
- 2바이트: 8비트
### 변수
#### 의미
- 프로그램은 기억 공간에 데이터를 보관하고, 각 기억 공간을 변수로 구분
- 변수는 데이터를 담는 상자와 같은 것으로 종류가 다양한데, 이를 구분하려고 데이터 타입을 사용 -> 자바는 변수는 하나의 변수에 다양한 타입의 값을 저장할 수가 없음
#### 리터럴
- 프로그램 내부에서 값을 정의해 변수를 초기화할 수 있는데, 그 값을 리터럴
- 리터럴에 붙이는 접두사와 접미사
- 정수, 실수 등
#### 문자
문자(`''`)와 문자열(`""`)은 다름
숫자 0은 유니코드 48이다

```java
public class DatatypeDemo {
  public static void main(String[] args) {

    char a1 = 'A';
    char a2 = 65;
    char a3 = '\u0041';
    System.out.println(a1);
    System.out.println(a2);
    System.out.println(a3);

    char ga1 = '가';
    char ga2 =  '\uac00';

    boolean c = true;
    boolean g = false;

    System.out.println(ga1);
    System.out.println((int)ga1);
    System.out.println(ga2);
    System.out.println(++ga2);

    System.out.println(c + "가 아니라면 " + g + "입니다.");
  }
}

```

```java
public class NumberTypeDemo {
  public static void main(String[] args) {
    int mach = 340;
    int distance = mach * 60 * 60;
    System.out.println("소리가 1시간 동안 가는 거리 : " + distance + "m");

    double radius = 10.0;
    double area = radius * 3.14;
    System.out.println("반지름이 " + radius + "인 원의 넓이 : " + area);
  }
}

```

```java
public class VarDemo {
  public static void main(String[] args) {
    var i = 100;
    var s = "korea";
    System.out.println(i);

    int a = 100;
    int b;
    final double PI;
    PI = 3.14159;
    b = 200;
    System.out.println(b);
  }
}
```



#### 상수: 한번만 값을 저장 가능한 변수
- 프로그램 실행 중 변경할 수 없는 데이터를 담는 변수
- 예를 들어 원주율 값(3.14169)이나 빛의 속도(3x10^8m/s) 등
- 상수 이름은 변수와 구분하려고 모두 대문자로 표기
- 반드시 `final` 키워드로 지정
#### 상수와 리터럴
- 리터럴: 그 자체로 값을 의미하는 것
- 상수와 리터럴은 기존의 상수와 같다. 즉 같은 개념임
- 자바에서 상수를 한번만 값을 저장할 수 있는 변수라고 했기 때문에 구분하는 것임
- `int score = 100;` 여기서 `100`이 리터럴, `final int MAX = 200;` `200`은 리터럴, `MAX`는 상수
#### 변수와 리터럴의 타입 불일치
- 범위가 변수 > 리터럴 인 경우 OK
- 범위가 변수 < 리터럴 인 경우 Error
### 타입 변환(형변환)
#### 형변환: 변수 또는 상수의 타입을 다른 타입으로 변환하는 것
- 자동 타입 변환과 강제 타입 변환: (타입)피연산자 등이 있음
- **값 손실이 있는가**가 자동 형변환 가능 여부에 가장 중요한 기준
- 값 손실이 있는 경우는, 강제로 타입 변환 가능
```java
public class TypeDemo {
  public static void main(String[] args) {
    int i = 'A'; // int(4byte) > char(2byte), (int)char
    double d = 3.14f; // double(8byte) > float(4byte), (double)float
    int ie = 10_000_000_000; //int 범위 20억을 벗어난 오류
    long l = 3.14f; //long 값의 범위 < float 값의 범위
    float f = 3.14; //float 값의 범위 < double 값의 범위
    byte b = 100;
    byte be = 128; // -128~127 범위를 벗어남
    int a = 100;
    byte be1 = a;
    byte be2 = (byte)a; // 범위 안에 있고, 강제 형변환을 해서 OK
  }
}
```

```java
public class TypeTransDemo {
  public static void main(String[] args) {
    int a = 3;
    char c = '3';
    System.out.println((char)(a+'0'));
    System.out.println(c-'0');
    System.out.println(((Object)((char)(a+'0'))).getClass().getSimpleName());

    String s = "3";
    String s1 = "3.14";
  }
}
```



### 기본 입출력

#### 화면에 데이터 출력
- `printIn()`: 내용을 출력한 후 행을 바꾼다.
- `print()`: 내용을 출력만 하고 행은 바꾸지 않는다.
- `printf()`: 포맷을 지정해서 출력한다. `System.out.printf("포맷 명시자", 변수명)`
#### 키보드로 데이터 입력
- 프로그램의 첫 행에 다음을 추가해 Scanner 클래스의 경로 이름을 컴파일러에 알린다. (`import java.util.Scanner`; //화면으로부터 데이터를 입력 받는 기능을 제공하는 클래스)
- 키보드로 데이터를 입력 받기 위해 System.in 객채와 ...
- `in.nextInt()`: int 타입 변수 입력받기
- `in.nextLine()`: 문자열 입력받기
- `Integer.parseInt()`: 문자열을 int 타입으로 변환

```java
import java.util.Scanner;

public class ScannerInput {
  public static void main(String[] args) {
    Scanner in;
    in = new Scanner(System.in);

    int x = in.nextInt();
    int y = in.nextInt();
    System.out.println(x + " 곱하기 " + y + " 은 " + x * y + " 입니다.");
    System.out.printf("%d 곱하기 %d 은 %d 입니다.", x, y, x*y);

    String s1 = in.nextLine();
    String s2 = in.nextLine();
    int i1 = Integer.parseInt(s1);
    int i2 = Integer.parseInt(s2);
    System.out.printf("%s 곱하기 %s 은 %d 입니다.", s1, s2, i1 * i2);
  }
}
```

### 연산자
#### 종류
- 여러 연산자들의 우선순위가 있다.
- 증감, 산술, 시프트, 부호, 비교, 비트, 논리, 조건, 대입 순
#### 산술 연산자
- 피연사자의 데이터 타입에 따라 결과 값이 다른데, 연산할 두 피연산자의 데이터 타입이 다르면 큰 범위의 타입으로 일치시킨 후 연산 수행
- 산술 변환: 연산 전에 피연산자의 타입을 일치시키는 것
- 단, 피연사자의 타입이 int보다 작은 타입이면 int로 변환된다.
- 나누기 연산에서는 분모를 주의!(`NaN`: Not a Number 또는 `Infinity`: 무한대)

```java
public class ArithmeticDemo {
  public static void main(String[] args) {
    int result1 = 5/0; //Exception in thread "main" java.lang.ArithmeticException: / by zero
    System.out.println(result1);

    double result2 = 5/0.0;
    double result3 = 5 % 0.0;

    if(Double.isInfinite(result2) || Double.isNaN(result3)){
      System.out.println("산술연산을 할 수 없습니다.");
    } else {
      System.out.println(result2);
      System.out.println(result2+1);
      System.out.println(result3);
      System.out.println(result3+1);
    }

    // 25를 2로 나눈 나머지는 1 입니다.
    int number1 = 25;
    int number2 = 2;
    System.out.printf("%d를 %d로 나눈 나머지는 %d 입니다.", number1, number2, number1 % number2);
  }
}
```

#### 비교 연산자

- 비교 연산자는 논리 타입을 제외한 기초 타입에만 사용할 수 있지만 `==`와 `!=`는 모든 기초 타입에 사용

#### 논리 연산자

- 논리 연산자는 피연산자의 조건을 결합해서 true와 false를 조사하며, 논리 타입에만 사용
- `^` : XOR

- 쇼트서킷: 논리 연산에서 앞만 보고 결과가 정해지면 뒤에는 연산 해보지도 않음

#### 비트/시프트 연산자

- 비트 연산자와 시프트 연산자는 정수 타입에만 사용

- 웹 개발에서는 잘 사용하지 않음

#### 대입 연산자

- 대입 연산자는 오른쪽에 있는 연산식의 결과 값을 왼쪽에 있는 변수에 대입

- 오른쪽이 `=`로 끝난다.

#### 부호/증감 연산자

`++(변수);` : 전위 증가

`(변수)++;` : 후위 증가

```java
public class SignIncrementDemo {
  public static void main(String[] args) {
    int i = 5, j= 5, x = 5, y =5;
    int res1 = i++ * x;
    int res2 = ++j * y;

    System.out.println(i); // i = 6
    System.out.println(res1); // 5 * 5 = 25, res1 = 25
    System.out.println(j); // j = 6
    System.out.println(res2); // 6 * 5 = 25, res2 = 30
  }
}
```

#### 조건 연산자

- 조건 연산자(?:)는 조건식이 true이면 결과 값은 연산식1의 값이 되고 false이면 결과 값은 연산식2의 값이 됨(삼항연산자)
- 비교적 논리구조가 간단한 경우에 사용한다.

```java
public class TernaryOperatorDemo {
  public static void main(String[] args) {
    int x = 1;
    int y;
    y = (x == 1) ? 10 : 20;
    System.out.println(y); // 10
    y = (x > 1) ? x++ : x + 20;
    System.out.println(x); // 1
    System.out.println(y); // 21
  }
}
```

#### 우선순위

- 하나의 식에 연산자가 둘 이상 있을 때 어떤 연산을 먼저 수행할지를 **자동으로 결정**하는 것
- 상식선에서 해결이되지만 헷갈리면 괄호`()`를 활용하여 우선순위를 강제하자!

#### 결합 규칙

- 우선 순위가 같은 연산자가 있을 때, 어던 것을 먼저 적용할지를 정하는 것
- 기본적으로는 대부분 왼쪽에서 오른쪽이고, <u>단항과 대입연산자만 오른쪽에서 왼쪽임</u>

#### 연산자와 우선순위

- 산술 > 비교 > 논리 > 대입 의 순서, 대입이 제일 마지막에 수행된다.
- 단항(1) > 이항(2) > 삼항(3) 의 순서