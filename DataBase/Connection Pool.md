# Connection Pool
## DB Connection
- DB를 사용하기 위해 DB와 애플리케이션 간 통신을 할 수 있는 수단
- DB Connection은 Database Driver와 Database 연결 정보를 담은 URL이 필요함
- Java의 DB Connection은 JDBC를 주로 이용하는데, URL 타입을 사용함
![image](https://github.com/user-attachments/assets/0d735956-b70f-4864-922b-42cbd0330018)
## DB Connection 구조
- 2Tier - 클라이언트로서의 자바 프로그램(JSP)이 직접 데이터베이스 서버로 접근하여 데이터를 액세스하는 구조
- 3Tier - 자바 프로그램과 데이터베이스 서버 중간에 미들웨어 층을 두어, 그 미들웨어 층에게 비즈니스 로직 구현부터 트랜잭션 처리, 리소스 관리 등을 전부 맡기는 구조이다.
## JDBC
- Java Database Connectivity의 약어로 자바 언어로 다양한 종류의 관계형 데이터베이스에 접속하고 SQL문을 수행하여 처리하고자 할 때 사용되는 표준 SQl 인터페이스 API이다.
- 원래라면 DB마다 연결 방식과 통신 규격이 따로 있기 때문에 프로그램을 DB와 연결한다면, 해당 DB와 관련된 기술적 내용을 배우고 DB가 변경될 시 많은 변경 사항이 존재한다.
- 하지만 각 DBMS에 맞는 JDBC를 받아주게 되면 쉽게 DBMS를 변경할 수 있게 된다.
- 즉, DBMS 종류(MySQL, MsSQL, Oracle 등)에 상관 없이 하나의 JDBC API를 사용해서 데이터베이스 작업을 처리할 수 있게 된다. JDBC API를 사용하는 애플리케이션의 대략적인 구조는 다음과 같다.
![image](https://github.com/user-attachments/assets/64338d68-2baf-4a92-87f5-c2a0525a9213)
- 자바 애플리케이션에서 데이터베이스에 접근하기 위해서는 JDBC API를 이용해서 데이터베이스에 접근하고, JDBC API는 JDBC 드라이버를 거쳐 데이터베이스와 통신을 한다.
## Connection Pool
```java
Connection conn = null;
PreparedStatement  pstmt = null;
ResultSet rs = null;

try {
    sql = "SELECT * FROM T_BOARD"

    // 1. 드라이버 연결 DB 커넥션 객체를 얻음
    connection = DriverManager.getConnection(DBURL, DBUSER, DBPASSWORD);

    // 2. 쿼리 수행을 위한 PreparedStatement 객체 생성
    pstmt = conn.createStatement();

    // 3. executeQuery: 쿼리 실행 후
    // ResultSet: DB 레코드 ResultSet에 객체에 담김
    rs = pstmt.executeQuery(sql);
    } catch (Exception e) {
    } finally {
        conn.close();
        pstmt.close();
        rs.close();
    }
}
```
- 위와 같이 자바에서 DB에 직접 연결해서 처리하는 경우 JDBC Driver를 로드하고 커넥션 객체를 받아와야 한다. 그러면 매번 사용자가 요청을 할 때마다 드라이버를 로드하고 커넥션 객체를 생성하여 연결하고 종료하기 때문에 매우 비효율적이다. 이런 문제를 해결하기 위해서 커넥션 풀을 사용한다.
## 커넥션 풀(DBCP)의 개념
- 웹 컨테이너(WAS)가 실행되면서 일정량의 Connection 객체를 미리 만들어서 pool에 저장했다가, 클라이언트 요청이 오면 Connection 객체를 빌려주고 해당 객체의 임무가 완료되면 다시 Connection 객체를 반납 받아서 pool에 저장하는 프로그래밍 기법이다.
- Container 구동 시 일정 수의 Connection 객체를 생성하게 되며 클라이언트의 요청에 의해 애플리케이션이 DBMS 작업을 수행해야 하면, Connection Pool에서 Connection 객체를 받아와 작업을 진행한다. 이후 작업이 끝나면 Connetion Pool에 Connection 객체를 반납한다.
![image](https://github.com/user-attachments/assets/bb7b2172-852f-4ff2-9066-5d65a6f417fa)
## 커넥션 풀(DBCP)의 동작 원리
### Hikari CP가 동작하는 방식
![image](https://github.com/user-attachments/assets/9e33a17f-9edf-46fe-be7c-56a9d02fb824)
- Thread가 Connection을 요청하면 Connection Pool의 각자의 방식에 따라 유휴 Connection을 찾아서 반환한다. Hikari CP의 경우, 이전에 사용했던 Connection이 존재하는지 확인하고, 이를 우선적으로 반환하는 특징이 있다.
![image](https://github.com/user-attachments/assets/4d458ad3-0274-4c4a-9da7-4c24356f6e81)
- 가능한 Connection이 존재하지 않으면, HandOffQueue를 Polling하면서 다른 Thread가 Connection을 반납하기를 기다린다. (지정한 TimeOut 시간까지 대기하다가 시간이 만료되면 예외를 던진다.)
![image](https://github.com/user-attachments/assets/43c0ca6f-4092-4332-9cf5-6a5fb9e0fd9a)
- 최종적으로 사용한 Connection을 반납하면 Connection Pool이 Connection 사용 내역을 기록하고, HandOffQueue에 반납된 Connection을 삽입한다.
-이를 통해 HandOffQueue를 Polling하던 Thread는 Connection을 획득하고 작업을 이어나간다.
## 커넥션 풀(DBCP)의 장점
- DB 접속 설정 객체를 미리 만들어 연결하여 메모리 상에 등록해 놓기 때문에 불필요한 작업(커넥션 생성, 삭제)이 사라지므로 클라이언트가 빠르게 DB에 접속이 가능하다.
- DB Connection 수를 제한할 수 있어서 과도한 접속으로 인한 서버 자원 고갈 방지가 가능하다.
- DB 접속 모듈을 공통화하여 DB 서버의 환경이 바뀔 경우 쉬운 유지 보수가 가능하다.
- 연결이 끝난 Connection을 재사용함으로써 새로 객체를 만드는 비용을 줄일 수 있다.
## 커넥션 풀(DBCP)의 유의 사항
### 동시 접속자가 많을 경우
- 너무 많은 DB 접근이 발생할 경우에는 커넥션은 한정되어 있기 때문에 쓸 수 있는 커넥션이 발납될 때까지 기다려야 한다. 너무 많은 커넥션을 생성할 시에는 커넥션 또한 객체이므로 많은 메모리를 차지하게 되고, 프로그램의 성능을 떨어뜨리는 원인이 된다.
- 즉, WAS에서 커넥션 풀을 크게 설정하면 메모리 소모가 큰 대신 많은 사용자가 대기 시간이 줄어 들고, 반대로 커넥션 풀을 작게 설정하면 그 만큼 대기 시간이 길어진다. 따라서 사용량에 따라 적정량의 커넥션 객체를 생성해 두어야 한다.
### Connection Pool이 커지면 성능은 무조건 좋아질까?
그렇지 않다. Connection의 주체는 Thread이므로 Thread와 함께 고려해야 한다.
- Thread Pool 크기 < Connection Pool 크기
  - Thread Pool에서 트랜잭션을 처리하는 Thread가 사용하는 Connection 외에 남는 Connection은 실질적으로 메모리 공간만 차지하게 된다.
- Thread Pool 크기와 Connection Pool 모두 크기 증가
  - Thread 증가로 인해 더 많은 Context Switching이 발생한다.
  - Disk 경합 측면에서 성능 한계가 발생한다.
    - 데이터베이스는 하드 디스크 하나 당 하나의 I/O를 처리하므로 블로킹이 발생한다.
    - 즉, 특정 시점부터는 성능적인 증가가 Disk 병목으로 인해 미비해진다.
따라서 데이터베이스 입자에서 Connection은 Thread와 어느 정도 일치한다고 볼 수 있다. Connection이 많다는 의미는 데이터베이스 서버가 Thread를 많이 사용한다는 것을 의미하고, 이에 따라 Context Switching으로 인한 오버헤드가 더 많이 발생하기 때문에 Connection Pool을 아무리 늘리더라도 성능적인 한계가 존재한다.

### Connection Pool의 크기는 얼마나 적절할까?
- Hikari CP의 공식 문서에 의하면, `1 connections = ((core_count) * 2) + effective_spindle_count)` 로 정의하고 있다.
![image](https://github.com/user-attachments/assets/8976c4ba-f43b-4f6c-b981-928555001548)
- core_count는 현재 사용하는 서버 환경에서의 CPU 개수를 의미한다.
  - core_count * 2 를 하는 이유는 Context Switching 및 Disk I/O와 관련이 있다.
    - Context Switching으로 인한 오버헤드를 고려하더라도 데이터베이스에서 Disk I/O(혹은 DRAM이 처리하는 속도)보다 CPU 속도가 월등히 빠르다.
    - 그러므로, Thread가 Disk와 같은 작업에서 블로킹되는 시간에 다른 Thread의 작업을 처리할 수 있는 여유가 생기고, 여유 정도에 따라 멀티 스레드 작업을 수행할 수 있게 된다. Hikari CP가 제시한 공식에서는 계수를 2로 선정하여 Thread 개수를 지정하였다.
- effective_spindle_count는 기본적으로 DB 서버가 관리할 수 있는 동시 I/O 요청 수이다.
  - 하드 디스크 하나는 spindle 하나를 갖는다.
  - 디스크가 16개 있는 경우, 시스템은 동시에 16개의 I/O 요청을 처리할 수 있다.
## 커넥션 풀(DBCP)의 종류
### commons-dbcp
- 아파치에서 제공하는 대표적인 커넥션 풀 라이브러리이다.
![image](https://github.com/user-attachments/assets/cb3ec88c-9607-4749-b995-830ac53208d3)
![image](https://github.com/user-attachments/assets/afd8b1ea-d58f-45f5-9f64-20fd796a0cc1)
위의 예시에서는 8개의 커넥션을 최대로 활용할 수 있는 상태이며, 4개는 사용 중이고 4개는 대기 중인 상태이다.
- maxActive ≥ initialSize
  - 최대 커넥션 개수는 초기에 생성할 커넥션 개수와 같거나 크게 설정해야 한다.
- maxActive = maxIdle
  - maxActive 값과 maxIdle 값은 같은 것이 바람직하다. 만약 둘의 값이 아래와 같다고 가정해 보자.
  - maxActive = 10, maxIdle = 5
    - 항상 커넥션을 동시에 5개는 사용하고 있는 상황에서 1개의 커넥션이 추가로 요청된다면 maxActive = 10이므로 1개의 추가 커넥션을 데이터베이스에 연결한 후 pool은 비즈니스 로직으로 커넥션을 전달한다.
    - 이후 비즈니스 로직이 커넥션을 사용한 후 pool에 반납할 경우, maxIdle = 5에 영향을 받아 커넥션을 실제로 닫아버리므로 일부 커넥션을 매번 생성했다 닫는 비용이 발생할 수 있다.
커넥션 개수와 관련된 가장 중요한 성능 요소는 일반적으로 커넥션의 최대 개수이다. 4개 항목의 설정 값 차이는 성능을 좌우하는 중요 변수는 아니다.

maxActive 값은 DBMS의 설정과 애플리케이션 서버의 개수, Apache, Tomcat에서 동시에 처리할 수 있는 사용자 수 등을 고려해서 설정해야 한다. DBMS가 수용할 수 있는 커넥션 개수를 확인한 후에 애플리케이션 서버 인스턴스 1개가 사용하기에 적절한 개수를 설정한다. 사용자가 몰려서 커넥션을 많이 사용할 때는 maxActive 값이 충분히 크지 않다면 병목 지점이 될 수 있다. 반대로 사용자가 적어서 사용 중인 커넥션이 많지 않은 시스템에서는 maxActive 값을 지나치게 작게 설정하지 않는 한 성능에 큰 영향이 없다.

Commons DBCP에서는 DBMS에 로그인을 시도하고 있는 커넥션도 사용 중인 것으로 간주한다. 만약 DBMS에 로그인을 시도하고 있는 상태에서 무한으로 대기하고 있다면, 애플리케이션에서 모든 커넥션이 사용 중인 상태가 돼 새로운 요청을 처리하지 못할 수도 있다. 이런 경우 장애 확산을 최소화하려면 Microsoft SQL Server의 JDBC 드라이버에서 설정하는 loginTimeOut 속성같은 JDBC 드라이버별 타임아웃 속성을 설정하는 것이 좋다.
### tomcat-jdbc-pool
- tomcat에 내장되어 사용되고 있다.
- Apache Commons DBCP 라이브러리를 바탕으로 만들어져 있다.
- Spring boot 2.0.0 하위 버전에서 사용하는 기본 DBCP이다.
### HikariCP
- 스프링 부트 2.0부터 default JDBC connection pool이다.
- zero-overhead의 특징을 갖는다.
  - overhead: 어떤 처리를 하기 위해 들어가는 간접적인 처리 시간 및 메모리

![image](https://github.com/user-attachments/assets/78a07fa0-fd2e-48ea-8b02-268535c1e3d2)
Springboot 환경에서는 application.properties에서 간단하게 HikariCP의 설정을 할 수 있다.
![image](https://github.com/user-attachments/assets/7a6d1bd4-4212-4f54-9f26-a9b77b9c216a)
HikariCP의 연결 정보 외에 원하는 Connection Pool의 크기, 시간과 관련된 설정 등을 작성할 수 있다.
## 요약
- JDBC는 자바 애플리케이션이 데이터베이스에 접근할 수 있도록 만든 JAVA에서 제공하는 API이다.
- 하나의 JDBC로 어떤 DBMS든 각 벤더마다 제공되는 JDBC 드라이버를 통해 연결 할 수 있다.
- 커넥션 풀이란 JDBC 실행 과정 중에서 생성되어야 할 Connection 객체를 미리 만들어서 pool 이란 곳에서 저장을 해두는 기법이다.
- 장점은 불필요한 과정(Connection객체를 생성,삭제)을 줄여서 성능을 높일 수 있다.
- WAS에서 커넥션 풀을 크게 설정하면 메모리 소모가 큰 대신 많은 사용자가 대기 시간이 줄어들고, 반대로 커넥션 풀을 적게 설정하면 그 만큼 대기 시간이 길어진다. 따라서 사용량에 따라 적정량의 커넥션(Connection)객체를 생성해두어야 한다.
