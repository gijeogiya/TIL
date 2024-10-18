# WAS(Web Application Server)
## WAS(Web Application Server)의 정의
- 개발된 Web Application을 설치(배포) 및 실행하고 Client에서 온 요청을 처리 및 결과를 전달하는 서버
- 복잡한 연산을 처리하며 Database 및 외부 서비스와 상호작요하면서 비즈니스 로직을 처리
## WAS(Web Application Server)의 역할
- WAS는 Container라는 공간을 생성하여  안에 Application을 설치(배포) 및 실행하여 서비스를 제공한다.
- Client 요청에 따라 Application의 개발 된 로직이 실행되며 로직에 필요한 Data는 DB에 요청한다.
- 외부 시스템과 연동 및 통신하기도 하는데 이 기능을 API(Application Programming Interface)라고 한다.
- DB에 요청해서 회신 된 모든 Data는 Heap Memory에 저장된다.
- 사용 중인 Data는 Heap에 계속 유지되고 있으나 사용 완료된 Data는 GC(Garbafe Collector)에 의해 정리 된다.
- WEB에서 온 요청을 로직 처리 후 종료(Colse)처리 될 때까지 유지되는 것을 Session(세션)이라 한다.
![WAS 종류](https://github.com/user-attachments/assets/d36a3fda-2255-4fdd-bf76-1709d47017f3)
![WAS 역할](https://github.com/user-attachments/assets/bb24b139-af12-4527-948f-c311869c89b0)
![WAS 프로세스](https://github.com/user-attachments/assets/afcc9e59-b41d-4871-9004-fc23b96c5a84)

## WAS(Web Application Server)의 특징
### Thread Pool Or Connection Pool
- WEB과 WAS를 연결하는 Thread Pool은 동일 및 MIN/MAX를 동일하게 설정하는 것을 권고한다.
- WAS-DB간의 연결방식은 Application에서 Source 설정하는 방식이 있으나, 성능 및 관리 문제로 지양한다.
- WAS에 DB와 연결하는 DBCP(or JDBC) 기능이 있으며 연결 및 Connection 수 설정 등을 관리 할 수 있다.
### Heap Memory
- Heap Memory란 물리 메모리(RAM) 공간을 동적으로 할당 Container에서 메모리로 활용하는 공간이다.
- Heap Memory의 용량이 클 수록 성능 및 Data 관리에 용이하다.
- 다만 너무 크다면 메모리를 정리하는 GC 실행 시 프로세스의 멈춤 현상이 오래 간다.
- 일정 용량 이상만 설정하는 것을 권고하며 그 이상 필요 시 Container를 추가하여 이중화 하는 것을 권고한다.
- Heap Memory 이상의 데이터가 발생 시, Out of Memory Error가 발생하며 WAS가 종료되므로 관리가 필요하다.
### GC(Garbage Collector)
- GC는 Heap Memory 사용 중에 불필요하거나 사용완료 된 Data를 정리하는 기능이다.
- Heap은 Young과 Old 영역으로 나뉘어져 있고, 각각 Minor GC와 Full GC가 일어난다.
- Full GC는 Old 영역의 Data를 정리하며, Full GC 시 프로세스가 멈추므로 GC관리가 필요하다.
![image](https://github.com/user-attachments/assets/6cda2dbf-85d4-45c5-b322-02b672aa296f)

