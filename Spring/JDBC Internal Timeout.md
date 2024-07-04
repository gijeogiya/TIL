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
- TransactionTimeout은 프레임워크(Spring, EJB Container)나 애플리케이션 레벨에서 유효한 타임아웃이다.
- TransactionTimeout은 "StatementTimeout x N(Statement 수행 수) + α(가비지 컬렉션 및 기타)"라고 할 수 있다.
- 전체 Statement 수행 시간을 허용할 수 있는 최대 시간 이내로 제한하려 할 때 TransactionTimeout을 사용한다.
- Statement 한 개를 수행할 때 0.1초가 필요하다면, 몇 개 안 되는 Statement를 수행할 때에는 문제가 없다. 그러나 Statement 10만 개를 수행할 때에는 일만 초(약 7시간)가 필요하다. TransactionTimeout은 이런 경우에 사용할 수 있다.
- 실 구현체로 EJB CMT(Container Managed Transaction)가 가장 대표적인 예이다.
- Spring에서 제공하는 TransactionTimeout은 매우 단순하다. 해당 Transaction의 시작 시간과 경과 시간을 기록하면서, 특정 이벤트 발생 시 경과 시간을 확인하여 타임아웃 이상일 경우 예외(Exception)를 발생하도록 하고 있다.
- Spring에는 Transaction Synchronization방식이라고 하여 Connection을 ThreadLocal에저장해 두고 사용한다.
- ThreadLocal에 Connection 저장 시 Transaction의 시작 시간과 타임아웃 시간을 같이 기록하고, Proxy Connection을 사용하여 Statement를 생성하는 작업을 시도할 경우 경과 시간을 체크하여 예외를 발생시키도록 구현되어있다.
- 수행 시간이 200ms인 Statement가 5개 이하이고 기타 부수적인 비즈니스 로직 처리 시간이나 프레임워크 동작 시간이 100ms일 경우, TrasactionTimeout시간은 1100ms((200 x 5)+100) 이상으로 설정해야 한다.
## StatementTimeout
- Statement 하나가 얼마나 오래 수행되어도 괜찮은지에 대한 한계 값이다.
- JDBC API인 Statement에 타임아웃 값을 설정하며, 이 값을 바탕으로 JDBC 드라이버가 StatementTimeout을 처리한다.
- JDBC API인 java.sql.Statement.setQueryTimeout(int timeout) 메서드로 설정한다.
- StatementTimeout 시간은 애플리케이션 특성에 따라 지정하기 때문에 이에 대한 설정 권장 값은 없다.
## JDBC 드라이버의 StatementTimeout 동작 방식
### Oracle JDBC Statement의 QueryTimeout
![Oracle JDBC Statement의 QueryTimeout 동작 과정](https://github.com/gijeogiya/TIL/assets/97646078/d90c4bcf-9254-4118-b1e7-f54c3d949c78)
1. Connection.createStatement() 메서드를 호출하여 Statement를 생성한다.
2. Statement.executeQuery() 메서드를 호출한다.
3. Statement는 자신의 Connection을 사용하여 Oracle DBMS로 쿼리를 전송한다.
4. Statement는 타임아웃 처리를 위해 OracleTimeoutPollingThread(classloader별로 1개 존재)에 Statement를 등록한다.
5. 타임아웃이 발생한다.
6. OracleTimeoutPollingThread는 OracleStatement.cancel() 메서드를 호출한다.
7. Connection을 통해 취소(cancel) 메시지를 전송하여 수행중인 쿼리를 취소한다.
### jTDS(Microsoft SQL Server) Statement의 QueryTimeout
![jTDS(Micsofot SQL Server) Statement의 QueryTimeout의 동작 과정](https://github.com/gijeogiya/TIL/assets/97646078/07c6e4e7-7e05-453e-b615-678fb71b370c)
1. Connection.createStatement() 메서드를 호출하여 Statement를 생성한다.
2. Statement.executeQuery() 메서드를 호출한다.
3. Statement는 내부 Connection을 사용하여 Microsoft SQL DBMS로 쿼리를 전송한다.
4. Statement는 타임아웃 처리를 위해 TimerThread에 Statement를 등록한다.
5. 타임아웃이 발생한다.
6. TimerThread는 JtdsStatement 객체 내부의 TdsCore.cancel() 메서드를 호출한다.
7. ConnectionJDBC을 통해 취소 메시지를 전송하여 수행중인 쿼리를 취소한다.
### MySQL JDBC Statement의 QueryTimeout(5.0.8 버전)
![MySQL JDBC Statement의 QueryTimeout의 동작 과정(5.0.8 버전)](https://github.com/gijeogiya/TIL/assets/97646078/4040e584-f091-48d3-abe4-ae30c4b9de2c)
1. Connection.createStatement() 메서드를 호출하여 Statement를 생성한다.
2. Statement.executeQuery() 메서드를 호출한다.
3. Statement는 내부 Connection을 사용하여 MySQL DBMS로 쿼리를 전송한다.
4. Statement는 타임아웃 처리를 위해 새로운 타임아웃 처리용 스레드를 생성한다. 5.1.x 버전에서는 Connection에 한 개의 스레드가 할당되는 것으로 변경되었다.
5. 스레드에 타임아웃 처리를 등록한다.
6. 타임아웃이 발생한다.
7. 타임아웃 처리 스레드가 Statement와 동일한 설정의 Connection을 생성한다.
8. 생성된 Connection을 사용하여 취소 쿼리(KILL QUERY "connectionId")를 전송한다.
### CUBRID JDBC Statement의 QueryTimeout
![CUBRID JDBC Statement의 QueryTimeout의 동작 과정](https://github.com/gijeogiya/TIL/assets/97646078/4e61a5d0-b05a-4669-9306-8894e7993309)
1. Connection.createStatement() 메서드를 호출하여 Statement를 생성한다.
2. Statement.executeQuery() 메서드를 호출한다.
3. Statement는 내부 Connection을 사용하여 CUBRID DBMS로 쿼리를 전송한다.
4. Statement는 타임아웃 처리를 위해 새로운 타임아웃용 스레드를 생성한다.
5. 스레드에 타임아웃 처리를 등록한다.
6. 타임아웃이 발생한다.
7. 타임아웃 처리 스레드가 Statement와 동일한 설정의 Connection을 생성한다.
8. 생성된 Connection을 사용하여 취소 메시지를 전송한다.
## JDBC 드라이버의 SocketTimeout
- JDBC Driver Type4는 소켓을 사용하여 DBMS에 연결하는 방식이고, 애플리케이션과 DBMS 사이의 ConnectTimeout 처리는 DBMS에서 하지 않는다.
- JDBC 드라이버의 SocketTimeout 값은 DBMS가 비정상으로 종료되었거나 네트워크 장애(기기 장애 등)가 발생했을 때 필요한 값이다.
- TCP/IP의 구조상 소켓에는 네트워크의 장애를 감지할 수 있는 방법이 없다. 그렇기 때문에 애플리케이션은 DBMS와의 연결 끊김을 알 수 없다. 이럴 때 SocketTimeout이 설정되어 있지 않다면 애플리케이션은 DBMS로부터의 결과를 무한정 기다릴 수도 있다(이러한 Connection을 Dead Connection이라고 부르기도 한다).

- 이러한 상태를 방지하기 위해 소켓에 타임아웃을 설정해야 한다. SocketTimeout은 JDBC 드라이버에서 설정할 수 있다. SocketTimeout을 설정하면 네트워크 장애 발생 시 무한 대기 상황을 방지하여 장애 시간을 단축할 수 있다.
- 단, SocketTimeout 값을 Statement의 수행 시간 제한을 위해 사용하는 것은 바람직하지 않다. 그러므로 SocketTimeout 값은 StatementTimeout 값보다는 크게 설정해야 한다. SocketTimeout값이 StatementTimeout보다 작으면, SocketTimeout이 먼저 동작하므로 StatementTimeout 값은 의미가 없게 되어 동작하지 않는다.

SocketTimeout에는 아래 두 가지 옵션이 있고, 드라이버별로 설정 방법이 다르다.

- Socket Connect 시 타임아웃(connectTimeout): Socket.connect(SocketAddress endpoint, int timeout) 메서드를 위한 제한 시간
- Socket Read/Write의 타임아웃(socketTimeout): Socket.setSoTimeout(int timeout) 메서드를 위한 제한 시간

- CUBRID, MySQL, jTDS (Microsoft SQL Server), Oracle JDBC 소스를 모두 확인해 본 결과 네 개의 드라이버에서는 위의 두 가지 API를 사용함을 확인할 수 있었다.
## OS 레벨 SocketTimeout
- SocketTimeout이나 ConnectTimeout을 설정하지 않으면 네트워크 장애가 발생해도 애플리케이션이 대부분 이를 감지할 수 없다. 따라서 연결이 되거나 데이터를 읽을 수 있을 때까지 애플리케이션이 무한정 기다리게 된다. 그러나 서비스에서 발생한 실재 장애 상황에서는 30분 후에 애플리케이션(WAS)이 재연결을 시도하여 문제가 해결되는 경우가 많다. OS에서도 SocketTimeout 시간을 설정할 수 있기 때문이다.
- 리눅스 서버에서는 SocketTimeout을 30분으로 설정해 두고 있었다. 해당 설정 값을 통해 OS 레벨에서 네트워크 연결 끊김을 확인하는 것이다. 문제가 발생한 리눅스 서버의 KeepAlive 체크 수행 주기가 30분이므로 SocketTimeout 설정을 0으로 해도 네트워크 장애로 인한 DBMS 연결 장애 지속 시간이 30분을 넘지 않는 것이다. Linux 서버에서 KeepAlive 체크 수행 주기는 tcp_keepalive_time로 조정할 수 있다.
- 네트워크 장애로 인해 애플리케이션이 대기 상태로 빠지는 경우는 대부분 애플리케이션이 Socket.read() 메서드를 호출하고 있을 때이다. 그러나 네트워크 구성이나 장애 유형에 따라 매우 드물게 Socket.write() 메서드를 실행하는 도중 대기 상태에 빠지는 경우가 있다.
- 애플리케이션에서 Socket.write() 메서드를 호출하면 OS 커널 버퍼에 데이터를 기록한 후 바로 제어권을 애플리케이션에 반환한다. 즉 커널 버퍼에 값을 제대로만 기록하면 Socket.write() 메서드 실행은 언제나 성공한다. 그러나 특수한 네트워크 장애로 OS 커널 버퍼가 가득차면 Socket.write() 메서드도 대기 상황에 빠질 수 있다. 이 경우 OS는 일정 시간 동안 패킷 재전송을 시도하다고 한계 값에 도달하면 에러를 발생시킨다. 이 기사에서 예로 든 서버에서는 해당 값이 대략 15분으로 설정되어 있었다. 이 값은 Linux 서버의 tcp_retries2로 조절할 수 있다.
