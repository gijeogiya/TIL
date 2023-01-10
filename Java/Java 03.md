# Java 03: 문자열, 배열, 열거타입

**2023.01.10**

## 문자열, 배열, 열거타입

### 문자열

#### 문자열의 선언과 생성

- 문자열 리터럴은 내부적으로 new String()을 호출해 생성한 객체이다.
- 따라서 s1은 new String(“안녕, 자바!”)를 호출해서 생성한 객체를 가리킨다.
- 그러나 내용이 같은 문자열 리터럴이라면 더 이상 새로운 String 객체를 생성하지 않은 채 기존 리 터털을 공유. 따라서 s1과 s2는 동일한 String 객체를 가리킨다.

#### 문자열 비교

`==`와 `!=` 연산자는 두 문자열의 내용을 비교하는 것이 아니라 동일한 객체인지 검사

- String 클래스에서 제공하는 문자열 비교 메서드

  | 메서드                           | 설명                                                         |
  | -------------------------------- | ------------------------------------------------------------ |
  | int compareTo(String s)          | 문자열을 사전 순으로 배교해 정수 값을 반환                   |
  | int compareToIgnore(String s)    | 대/소문자를 무시, 문자열을 사전순으로 비교                   |
  | boolean equals(String s)         | 주어진 문자열 s와 현재 문자열을 비교 후 true/false 반환      |
  | booleam equalsToIgnore(String s) | 대/소문자를 무시, 주어진 문자열 s와 현재 문자열을 비교 후 true/false 반환 |

```java
public class StringCompare {
  public static void main(String[] args) {
    String s1 = "hello java";
    String s2 = "hello java";
    String s3 = new String("hello java");
    String s4 = new String("hello java");

    System.out.println(s1 == s2); //true
    System.out.println(s1.equals(s2)); //true

    System.out.println(s3 == s4); //false
    System.out.println(s3.equals(s4)); //true

    // 결론: 문자열이 같은지 비교하려면 String.equals() 메서드를 사용해야한다.

    s1 = s3;
    System.out.println(s1.equals(s3)); //true
    System.out.println(s1 == s3); //true
  }
}
```

#### 문자열 조작

- String 클래스에서 제공하는 메서드

![image-20230110101606493](C:\Users\LDCCHRD_\Desktop\Java 03.assets\image-20230110101606493.png)

```java
public class StringCompare {
  public static void main(String[] args) {
  
    String s1 = "hello java";
    String s2 = "";
    String s3 = " ";
    String s4 = null;

    System.out.println(s1.toUpperCase()); //HELLO JAVA
    System.out.println(s1.charAt(4)); //o
    System.out.println(s1.substring(0, 3)); //hel
    System.out.println(s2.isEmpty()); //true
    System.out.println(s3.isEmpty()); //false
    System.out.println(s4.isEmpty()); //NullPointerException Error
      
    //문자열 다룰 때는 NullPointerException Error를 주의. 문자열의 초기값은 ""을 줘야 한다.

  }
}
```

#### 텍스트 블록

- 자바 15부터 추가된 기능
- 멀티 라인의 문자열을 이스케이프 시퀀스(escape sequence) 없이 허용
- 소스 코드 작성을 편리하게 하고 코드의 가독성을 제고
- `""" ~ """` 코드 사이에 있는 문자열을 이스케이프 문자나 스트링 조합 연산 없이 String 객체로 인식
- 블록을 시작하는 `"""` 뒤에는 문자열이 바로 나오면 컴파일 에러가 발생. 기존 문자열 리터럴과 구분 하기 위하여 `"""` 후에 한 라인을 띄운 후 문자열을 작성해야 텍스트 블록으로 인식
- 이중 인용부호`“`가 필요할 경우 기존 방식의 `\＂`과 달리 `\`없이 텍스트 블록에서는 바로 인식
-  개행 문자인 `\n` 없이 텍스트 블록에서는 바로 엔터 값을 인식
-  텍스트 블록에서 유일하게 `\`는 이스케이프 시퀀스로 인식되기 때문에 해당 값을 반영하길 원하면 기존처럼 `\\`로 작성
-  텍스트 블록도 String 객체이기 때문에 String 클래스가 제공하는 모든 연산 사용 가능
-  텍스트 블록에서 들여쓰기 규칙은 블록을 종료하는 `"""`의 위치에 의해 결정

### 배열

배열은 변수들을 연속된 집합체로 모아 놓은 것으로 동일한 이름을 사용하며 인덱스로 각 항목을 구분한다.

#### 배열의 선언과 생성

- 배열의 선언: 실제는 배열 변수의 선언, 배열을 다루기 위한 참조변수의 선언

`int[] scores;`, `int scores[];`

~~int scores[5];~~ : 불가능

- 배열의 선언과 생성: 실제는 배열 변수의 선언과 초기화, 배열의 생성은 저장공간이 만들어짐을 의미
- scores = new int[5];
  - int 값을 저장할 수 있는 5개의 저장공간을 만들어준다.
  - 5개의 저장공간의 주소(예. 0x100)를 참조변수 score에 대입한다.

![image-20230110103751929](C:\Users\LDCCHRD_\Desktop\Java 03.assets\image-20230110103751929.png)

- 한번에 하려면 `int[] score = int[5]`처럼 선언&생성 하면 된다.

#### 배열의 초기화

- 배열의 각 요소에 처음으로 값을 저장하는 것
- 배열은 기본적으로 기본값으로 자동 초기화가 된다.(int의 경우 0으로 자동 저장)
- 초기화하는 값에 규칙이 있다면 반복문으로 모든 요소에 특정값을 대입시켜 초기화할 수 있지만 `{}` 를 사용해 초기화한다.

```java
public class ArrayInit1 {
  public static void main(String[] args) {
    
    int[] s1 = {10, 20, 30, 40, 50};
    
    int[] s2 = new int[]{10, 20, 30, 40, 50};
    
    int[] s3;
    s3 = new int[]{10, 20, 30, 40, 50};
    
    int[] s4;
    s4 = {10, 20, 30, 40, 50}; // 컴파일에러 주소 들어갈 곳에 배열을 집어넣으면 안됨
  }
}
```

- s4에는 주소가 들어가야하므로 오류가 남



#### 배열 원소의 접근

- `배열이름[인덱스];` 인덱스는 각 요소(저장공간)에 자동으로 부여되는 일련번호로 `0`부터 배 열의 `길이-1` 까지가 인덱스의 범위이다.

- 배열의 크기
  - 배열이 생성될 때 배열의 크기가 결정 (즉, 한번 생성되면 그 길이를 바꿀 수 없다.)
  - 배열의 length 필드가 배열의 크기를 나타냄. 예를 들어 scores가 가리키는 배열의 크기는 scores.length(int형 상수, 변경불가)

#### 배열의 출력

```java
public class ArrayInit2 {
  public static void main(String[] args) {

    int[] scores = new int[];

    System.out.println(scores); //[I@776ec8df : 주소값이 출력됨

    for(int i = 0; i < 5; i++){
      System.out.println(scores[i]); // 0만 5개가 나옴
    }
  }
}
```

```java
public class ArrayInit3 {
  public static void main(String[] args) {

    int[] scores = new int[]{10, 20, 30, 40, 50};

    //for 문 사용
    for(int i = 0; i < scores.length; i++){
      System.out.print(scores[i]); //1020304050
    }

    //for each문 사용
    for (int e: scores
         ) {
      System.out.print(e); //1020304050
    }

      
    char[] c = {'a', 'b', 'c'};

    System.out.println(c); //abc: 문자열의 관해서는 주소값이 문자열이 나옴
    for (char j: c
    ) {
      System.out.print(j); //abc
    }
  }
}
```

- `Arrays.toString(arr)`를 사용하면 배열의 요소를 출력할 수 있다.

```java
import java.util.Arrays;

public class ArrayInit {
  public static void main(String[] args) {

    int[] scores = new int[]{10, 20, 30, 40, 50};

    System.out.println(Arrays.toString(scores)); //[10, 20, 30, 40, 50]
  }
}
```

### 문자열 배열

- String[] name = new String[3]; // 3개의 문자열을 담을 수 있는 배열을 생성
- String[] name = {”Kim”, “Lee”, “Park”}; 과 같은 방식으로 선언과 초기화 가능.

![image-20230110112619674](C:\Users\LDCCHRD_\Desktop\Java 03.assets\image-20230110112619674.png)

### 다차원 배열

- 배열의 배열
- `int[][] scores = new int[3][5]`
- `int[][] scores = {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}}`

### 배열 응용

#### 배열을 위한 반복문

- for~each 반복문 : JDK 5부터 도입된 것으로 for 문을 개선한 방식. 특정 원소를 나타내기 위한 인 덱스를 사용하지 않는다.

#### 최대값과 최소값 찾기

```java
import java.util.Arrays;

public class MinMaxArray {
  public static void main(String[] args) {
    int[] arr = {40, 60, 20, 30};

    //직접 작성
    int max = arr[0];
    int min = arr[0];
    for(int i = 1; i < arr.length; i++){
      if(arr[i] > max) max = arr[i];
      if(arr[i] < min) min = arr[i];
    }
    System.out.println(max); //60
    System.out.println(min); //20

    //Arrays 내 메서드 사용
    Arrays.sort(arr);
    System.out.println(Arrays.toString(arr)); //[20, 30, 40, 60]
    System.out.println(arr[3]); //60
    System.out.println(arr[0]); //20
  }
}
```

#### shuffle과 로또번호 생성

```java
int arr[] = {1, 2, 3, 4, 5, 6};
Collections.shuffle(Arrays.asList(arr));
```

#### 참조형 매개변수

- 메서드의 인수로 배열 전달 (Read & Write)

```java
public class IncrementArray {
  public static void main(String[] args) {
    int[] x = {0};
    System.out.println("메서드 호출 전 x[0] ==> " + x[0]); //0
    increment(x);
    System.out.println("메서드 호출 후 x[0] ==> " + x[0]); //1
  }

  public static void increment(int[] n) {
    System.out.println("메서드 안에서의 n[0] ==> " + n[0]); //0
    n[0]++;
    System.out.println("메서드 안에서의 n[0] ==> " + n[0]); //1
  }
}
```

#### 메인 메서드 매개변수 전달

![image-20230110124916035](C:\Users\LDCCHRD_\Desktop\Java 03.assets\image-20230110124916035.png)

```java
public class ArgsArray {
  public static void main(String[] args) {
    if(args.length > 0) {
      System.out.println(args[0]); //권기정
    }
  }
}
```

![image-20230110131623309](C:\Users\LDCCHRD_\Desktop\Java 03.assets\image-20230110131623309.png)

```java
public class ArgsArray {
  public static void main(String[] args) {
    if(args.length > 0) {
      for(int i = 0; i < Integer.parseInt(args[1]); i++) {
        System.out.println(args[0]); // 권기정! x 3
      }
    }
  }
}
```

#### 가변 개수 인수

- JDK 5부터는 메서드에도 데이터 타입이 같은 가변 개수(variable length)의 인수를 전달 가능

`데이터타입... 변수`

- 한 개의 가변 개수 매개변수만 사용 가능하며 가변 개수 매개변수는 마지막에 위치
-  가변 개수 인수를 가진 메서드를 호출하면 내부적으로 배열을 생성하여 처리

```java
public class VarArgs {
  public static void main(String[] args) {
    printSum(1, 2, 3, 4, 5);
    printSum(10, 20, 30);
  }
  public static void printSum(int... v){
    int sum = 0;
    for (int num: v
         ) {
      sum += num;
    }
    System.out.println("전체 숫자의 합은 " + sum);
  }
}
```

#### 객체의 배열

- 객체 배열은 객체를 참조하는 주소를 원소로 구성
- 예를 들어 Ball 클래스의 객체로 구성된 배열을 선언하고 초기화
- `Ball[] balls = new Ball[5];`: 5개의 Ball 객체를 생성하는 것이 아니라 5개의 Ball 객체를 참조할 변수를 준비하는 것이다.
- 생성자를 호출하여 Ball 객체를 생성해야함.

```java
public class Constructor {
  public static void main(String[] args) {
//    Circle2 c1 = new Circle2(); //20.0, 파랑
//    Circle2 c2 = new Circle2(3.0); //6.0, 빨강
//    Circle2 c3 = new Circle2("노랑"); // 5.0, 노랑
//    System.out.println(c1.color);
//    System.out.println(c1.radius);
//    System.out.println(c2.color);
//    System.out.println(c2.radius);
//    System.out.println(c3.color);
//    System.out.println(c3.radius);
    Circle2[] c = new Circle2[5];
    for(int i = 0; i < 3; i++){
      c[i] = new Circle2();
      c[i].color="빨강";
      c[i].radius=3.0;
    }
    for(int i = 0; i < c.length; i++){
      System.out.println(c[i]); //Circle2@4eec7777, null 등 주소값이 나옴
      System.out.println(c[i].color); // 빨강
      System.out.println(c[i].radius); // 3.0
    }
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

#### 매개변수로 객체 전달

- 매개변수로 객체 전달이 가능하다.

#### 열거 타입

- 열거형(enum)
- 관련된 상수들을 같이 묶어 놓은 것,  Java는 타입에 안전한 열거형을 제공함
- 열거형의 조상: java.lang.Enum
- 선언: `enum 열거타입이름 { 상수목록 }`

![image-20230110132749104](C:\Users\LDCCHRD_\Desktop\Java 03.assets\image-20230110132749104.png)

- 필요성
  - 제한된 수의 일이나 사건 등에 대하여 숫자로 표현
  - 제한된 사건에 대하여 숫자 대신에 상수를 정의해서 부여
  - 자바 5부터 열거 타입을 제공

#### 열거 타입과 응용

- 일종의 클래스 타입인 열거 타입도 생성자, 필드 및 메서드를 가질 수 있다.
- 열거 타입 상수는 생성자에 의한 인스턴스이다.
- 이때 생성자, 필드 및 메서드와 열거 타입 상수를 구분하기 위하여 다음과 같이 열거 타입 상수 뒤 에 반드시 세미콜론을 추가해야 한다.