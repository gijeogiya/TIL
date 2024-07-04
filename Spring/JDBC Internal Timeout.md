# JDBC Internal Timeout
## JDBC
- JDBC는 DBMS에 접근하기 위한 표준 API이다.
- JDBC Type4 드라이버는 Java로만 작성되어 있으며(pure java), Java 애플리케이션에서 소켓을 이용해 DBMS와 통신한다.
![JDBC Type4 드라이버의 DBMS 통신 구조](https://github.com/gijeogiya/TIL/assets/97646078/02523b5a-6c41-401d-bdac-bf0ea9c8edfb)
- Type4 드라이버는 소켓을 통해 바이트 스트림(byte stream)을 처리하기 때문에 HttpClient 같은 네트워크 라이브러리와 근본적으로 동작이 같다.
- 많은 CPU자원을 소모하고, ResponseTime의 손해가 있으며, 다른 네트워크 라이브러리가 가지고 있는 장애 포인트를 동일하게 가지고 있다.
- Type4 드라이버는 SocketTimeout 값을 제대로 설정하지 않으면 동일한 장애가 발생할 수 있다.
## WAS와 DBMS의 통신 시 타임아웃 계층
![타임아웃 계층](https://github.com/gijeogiya/TIL/assets/97646078/25297763-b83a-44f6-bacc-b247871ac6f9)
- 상위 레벨의 타임아웃은 하위 레벨의 타임아웃에 의존성을 가지고 있다.
- 위 레벨의 타임아웃이 정상으로 동작해야 상위 레벨의 타임아웃도 정상으로 동작한다.
- 예를 들어, JDBC Driver SocketTimeout이 정상으로 동작하지 않으면, 그보다 상위 레벨의 타임아웃인 StatementTimeout과 TransactionTimeout도 정상으로 동작하지 않는다.
- StatementTimeout은 네트워크 연결 장애에 대한 타임아웃을 담당하는 것이 아니다.
- StatementTimeout은 Statement 한 개의 수행 시간을 제한하는 기능만 담당하기 떄문에 네트워크 장애에 대비하는 타임아웃은 JDBC Driver SoecketTimeout이 처리해야 한다.
- JDBC Driver SocketTimeout은 OS의 SocketTimeout 설정에 영향을 받는다. (네트워크 장애시, StatementTimeout 시간을 3분으로 설정했는데 30분 후에 복구가 된 예시)
- DBCP Connection Pool이 타임아웃 계층과 분리되어 있으며, DBCP는 Connection을 생성하고 관리하는 일을 하고 타임아웃 처리에는 관여하지 않는다.
- DBCP 내부에서 Connection을 생성하거나 Connection 유효성을 확인하려 Validation Query를 보낼 때에는 SocketTimeout이 영향을 주지만 애플리케이션에 직접적인 영향을 주지는 않는다.
- 단, 애플리케이션 로직에서 DBCP에 getConnection() 메서드를 호출할 때 Connection을 애플리케이션이 얻을 때까지의 타임아웃을 지정할 수 있다. 하지만 이것은 JDBC의 ConnectTimeout과는 무관하다.
![각 레벨 별 타임아웃](https://github.com/gijeogiya/TIL/assets/97646078/d8b98030-85b5-4b42-a70b-16505b9060d8)
## TransactionTimeout
