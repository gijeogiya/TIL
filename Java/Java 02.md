# Java 02: 제어문과 메서드

**2023.01.09**

## 제어문과 메서드

### 제어문

- Flow control statement
- 필요성

#### 조건문 - If 문

- 블록 `{}`

- 여러 문장을 하나로 묶어주는 것

```
  if (조건식)
  { // 블록의 시작
  	System.out.println(~~~) // 들여쓰기하여 가독성을 보장해주자
  } // 블록의 끝
```

- 단순 if 문

- if ~ else 문

- 다중 if 문 (`else if` 사용)

- 중첩 if 문: 주의!*`{}`를 생략하게 되면 indentation이 있더라도 else 블록은 가까운 if 문과 연결됨

```java
import java.util.Scanner;

public class NestedIfDemo {
  public static void main(String[] args) {

    System.out.print("성적을 입력해주세요! : ");
    Scanner in;
    in = new Scanner(System.in);
    int score = in.nextInt();
    String grade = "F";

    if (score >= 90) {
      if (score >= 95) {
        grade = "A+";
      } else {
        grade = "A0";
      }
    } else {
      grade = "B";
    }
    System.out.println(grade);
  }
}
```

#### 조건문 - switch문

```java
switch(변수) {
	case 상수1 : 0개 이상의 실행문 // break문 과 같은 실행무닝 없으면 다음 케이스로 계속해서 넘어가면서 확인
	...
	default : 0개 이상의 실행문 //선택 사항
}
```

##### 개선된 switch문

- 자바 14부터는 기존 switch 문도 연산식, 다중 case 레이블, yield 예약어를 허용
- `case 조건들 -> 실행문` 문장을 이용하면 여러개의 조건을 콤마를 이용해서 기술, 가독성이 좋아짐
- 개선된 switch문에서는 break문을 사용할 수 없음
- yield는 코드 블록 여부와 상관없이 사용 가능
- `case 문장: ` 자체가 블록의 역할을 함

```java
import java.util.Scanner;

public class VendingMachine {
  public static void main(String[] args) {
    System.out.print("제품코드를 입력해주세요!(A, B, C) : ");
    Scanner in = new Scanner(System.in);
    String prod = in.nextLine();

    // 기존
    switch (prod) {
      case "A", "a" -> System.out.println("콜라 입니다.");
      case "B", "b" -> System.out.println("사이다 입니다.");
      case "C", "c" -> System.out.println("생수 입니다.");
    }
  }
}
```

```java
import java.util.Scanner;

public class VendingMachine {
  public static void main(String[] args) {
    System.out.print("제품코드를 입력해주세요!(A, B, C) : ");
    Scanner in = new Scanner(System.in);
    String prod = in.nextLine();

    // 리턴이 있는 경우
    String prodName = switch (prod) {
      case "A", "a" -> "콜라";
      case "B", "b" -> "사이다";
      case "C", "c" -> "생수";
      default -> "제품 없음";
    };
    System.out.println(prodName + " 입니다.");
  }
}
```

```java
import java.util.Scanner;

public class VendingMachine {
  public static void main(String[] args) {
    System.out.print("제품코드를 입력해주세요!(A, B, C) : ");
    Scanner in = new Scanner(System.in);
    String prod = in.nextLine();

    // yield 사용
    String prodName = switch (prod) {
      case "A", "a" : yield "콜라";
      case "B", "b" : yield "사이다";
      case "C", "c" : yield "생수";
      default : yield "제품 없음";
    };
    System.out.println(prodName + " 입니다.");
  }
}
```

- Switch 문 연산식의 주의 사항

  - 가능한 모든 값에 대하여 일치하는 case 레이블이 없으면 오류가 발생

  - 다음 코드에서 변수 n의 모든 가능한 값은 정수이므로 오류 발생

    ```
    static String howMany(int n) {
    	return switch(n){
    		case 1 -> "1개"
    		case 2 -> "2개"
    	}
    }
    ```

#### 반복문 - while 문

- while 문: 조건을 만족시키는 동안 블록`{}`을 반복 - 반복 횟수 모를때 사용

#### 반복문 - for 문

```java
public class WhileDemo {
  public static void main(String[] args) {
      
    // for 문 사용
    for (int i = 1; i < 5; i++) {
      System.out.print(i);
    }

    // while 문 사용
    int j = 1;
    while (j < 5) {
      System.out.print(j++);
    }

    // do while 문 사용
    int k = 1;
    do {
      System.out.print(k++);
    } while (k < 5);

  }
}
```

```java
public class While2Demo {
  public static void main(String[] args) {
    
    // for 문 사용
    for (int row = 2; row < 10; row++) {
      for (int col = 1; col < 10; col++) {
        System.out.print(row * col + " ");
      }
      System.out.println("");
    }

    // while 문 사용
    int row2 = 2;
    int col2 = 1;
    while (row2 < 10) {
      while (col2 < 10) {
        System.out.print(row2 * col2++ + " ");
      }
      System.out.println("");
      row2++;
      col2 = 1;
    }
    
  }
}
```

#### 분기문 - break 문

- 분기부를 적어주지 않으면 가장 가까운 while문을 빠져나옴
- 분기부를 기재하면 해당 부분을 빠져나옴

#### 분기문 - continue 문

- while 문에서는 조건식을 바라보며 스킵
- for 문에서는 증감식을 바라보며 스킵

### 메서드

#### 필요성

- 중복 코드를 줄이고 코드를 재사용할 수 있다.
- 코드를 모듈화해 가독성을 높이므로 프로그램의 품질을 향상시킨다.

#### 메서드를 사용하지 않았을 때 예시 코드

```java
public class Method1Demo {
  public static void main(String[] args) {
    int sum = 0;
    for (int i = 0; i <= 10; i++)
      sum += i;
    System.out.println("합(1~10) : " + sum);

    sum = 0;
    for (int i = 10; i <= 100; i++)
      sum += i;
    System.out.println("합(10~100) : " + sum);

    sum = 0;
    for (int i = 100; i <= 1000; i++)
      sum += i;
    System.out.println("합(100~1000) : " + sum);
  }
```

#### 메서드를 사용했을 때 예시 코드

```java
public class Method2Demo {
  public static void main(String[] args) {
    printSum(1, 10);
    printSum(10, 100);
    printSum(100, 1000);
  }
  public static int printSum(int x, int y) {
    int sum = 0;
    for (int i = x; i <= y; i++)
      sum += i;
    System.out.println("합(" + x + "~"+ y + ") : " + sum);

    return sum;
  }
}
```

#### 메서드의 구조

- 헤더: `접근 지정자` + `객체를 생성하지 않고 실행 여부` + `반환 타입` + `메서드 이름` + `매개변수 목록`
- 본체: `지역 변수`를 사용한다. `반환 타입`과 리턴하는 `데이터의 타입`이 같아야 한다.

#### 메서드 호출과 반환

메서드를 호출하면 제어가 호출된 메서드(callee)로 넘어갔다가 호출된 메서드의 실행을 마친 후 호출한 메서드(caller)로 다시 돌아온다. 단, return 문을 사용하면 다음과 같이 메서드의 실행 도중 에도 호출한 메서드로 제어를 넘길 수 있다.

#### 매서드의 매개변수

- 메서드의 정의: 메소드는 클래스 영역 안에서만 정의 가능
- 메서드의 호출: 메서드의 이름(값1, 값2, ...)

#### 스택

- 스택: 밑이 막힌 상자, 넣는 순서대로 위에 차곡차곡 쌓인다. 밑이 막혀있기 때문에 꺼낼때는 위에 있는 것부터 꺼낸다.
- 호출 스택(call stack): 메서드 수행에 필요한 메모리가 제공되는 공간. 메서드가 호출되면 호출스택에 메모리할당, 종료되면 해제됨

#### 매개변수

- 기본형 매개변수
  - 8개 기본형을 매개변수로 하는 메서드, 변수의 값을 읽기만 함(read only)
  - 값 전달(call by value)
- 참조형 매개변수
  - 기본형 이외의 변수를 매개변수로 하는 메서드, 변수의 값을 읽고 변경할 수 있다.(read & write)
  - 주소 전달(call by address)

```java
public class CallbyValue {
  public static void main(String[] args) {
    MyMath m = new MyMath();
    long res1 = m.add(2L, 3L);
    System.out.println(res1);
  }
}

class MyMath {
  long add(long a, long b) { return a+b; }
  long sub(long a, long b) { return a-b; }
  long mul(long a, long b) { return a*b; }
  long div(long a, long b) { return a/b; }
}
```

#### 오버로딩

- 메서드 시그너처(Method Signature) : 메서드 이름, 매개변수의 개수, 매개변수의 타입과 순서를 의미
- 메서드 이름은 같지만 메서드 시그니처가 다른 메서드를 정의하는 것을 메서드 오버로딩(Method Overloading)이라고 한다.