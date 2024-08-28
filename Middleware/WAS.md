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
  
