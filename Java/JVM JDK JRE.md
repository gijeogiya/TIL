# JVM JDK JRE
## JVM JDK JRE 개념 요약
- JDK가 JRE, JVM을 포함하고, JRE는 JVM을 포함한다. (JDK > JRE > JVM)
     
![image](https://github.com/user-attachments/assets/9cdf1b2e-2f34-455f-bb32-17a86ca49dbc)
1. JVM (Java Virtual Machine)
     - Java는 OS에 종속적이지 않기 때문에, JVM을 이용하여 여러 종류의 운영체제에서 Java 프로그램을 실행할 수 있다.
2. JRE (Java Runtime Environment)
     -  JVM과 자바 프로그램을 실행(동작)시킬 때 필요한 라이브러리 API를 함께 묶어서 배포되는 패키지로, 
     - JVM이 원활하게 잘 작동할 수 있도록 환경을 맞춰주는 역할 한다.
3. JDK (Java Development Kit)
     - 개발자들이 자바로 개발할 때 사용되는 소프트웨어 개발 키트로, 자바 컴파일러를 포함하고 있다.
## JVM (Java Virtual Machine)
![image](https://github.com/user-attachments/assets/6d70135e-244e-431e-9634-5e22b4bb9096)
- Java는 JVM이 구동될 수 있는 환경이라면 모두 실행이 가능하므로 높은 이식성을 보인다. (반면 C언어는 OS별로 다른 컴파일이 필요하므로, 이식성이 낮다.)
- Java가 OS에 종속적이지 않다는 특징이 있기 때문에 자바코드로 작성된 프로그램은 JVM을 활용하여 CPU나 운영체제 등 환경에 상관없이 독립적으로 동작할 수 있다.
### Java 프로그램 실행과정
![image](https://github.com/user-attachments/assets/793f8c32-4506-407d-a41d-1271116fc269)
1. 자바 소스코드를 작성한다 (Example.java)
2. 컴파일러를 통해 JVM이 인식할 수 있는 Byte code(바이트 코드)의 클래스 파일을 생성한다. (Example.class)
3. JVM은 클래스 파일의 바이트 코드를 Binary Code(바이너리 코드)로 변환하여 프로그램을 수행한다.
##  JRE (Java Runtime Environment)
- JVM과 자바 프로그램을 실행(동작)시킬 때 필요한 라이브러리 API를 함께 묶어서 배포되는 패키지이다. (JDK를 설치하면 JRE가 포함되어 함께 설치된다.)
- JRE는 그 자체로 특별한 기능을 하기보다는 JVM이 원활하게 잘 작동할 수 있도록 환경을 맞춰주는 역할을 수행한다.
## JDK (Java Development Kit)
- JDK 에는 Java 개발 시 필요한 라이브러리들과 개발 도구들이 포함되어 있으며 개발자들이 Java로 개발할 때 사용된 소프트웨어 개발 키트라고 생각하면 된다. (ex. Oracle JDK, Open JDK, Azul Zulu 등)
### JDK 디렉토리 구성요소 예시
![image](https://github.com/user-attachments/assets/80768c16-189d-4483-b5e4-c60e6fc74ffe)
1. bin폴더 : 자바 개발, 실행에 필요한 도구와 유틸리티 명령
  - javac.exe : 자바 컴파일러로 자바 소스를 바이트 코드로 컴파일
  - java.exe : 자바 인터프리터로 컴파일러가 생성한 바이트 코드를 해석하고 실행
2. include폴더: 네이티브 코드 프로그래밍에 필요한 C언어 헤더 파일
3. lib폴더: 실행에 필요한 라이브러리 클래스들
