# Rate Limiting(처리율 제한 장치 설계)
## 개요
- 처리율 제한 장치(Rate Limiter)는 클라이언트 또는 서비스가 보내는 트래픽의 처리율(Rate)을 제어하기 위한 장치이다.   
- 이 기술은 서비스나 애플리케이션에 너무 많은 요청이 한꺼번에 몰리는 것을 방지하여, 서버가 안정적으로 운영될 수 있도록 돕는다.   
## 예시: 특정 기간 내에 전송되는 클라이언트의 요청 횟수를 제한
- 사용자는 초당 2회 이상의 새 글을 올릴 수 없다.
- 같은 IP 주소로는 하루에 10개 이상의 계정을 생성할 수 없다.
- 같은 디바이스로 주당 5회 이상 리워드(Reward)를 요청할 수 없다.
## API 처리율 제한 장치를 두면 좋은점
- DoS(Denial of Service) 공격에 의한 자원 고갈(Resource Starvation)을 방지할 수 있다.
- 비용을 절감할 수 있다. 처리를 제한해 서버를 많이 두지 않고, 우선순위가 높은 API에 더 많은 자원을 할당할 수 있다. 특히 요청 당 비용이 드는 Third Party API를 사용하고 있는 경우, 횟수 제한을 통해 과도한 비용을 막을 수 있다.
- 서버 과부하를 막을 수 있다. 봇, 크롤러 등에서 오는 잘못된 이용 패턴으로 유발된 트래픽을 제한한다.
## 1단계: 문제 이해 및 설계 범위 확정
- 클라이언트 측 제한 장치인가? 서버 측 제한 장치인가?
- 어떤 기준을 통해 호출을 제한하는가? 어떤 제어 규칙을 사용하는가?(e.g. IP, UserID, SessionID)
- 시스템 규모는 어떻게 되는가? (e.g. 사용자의 규모)
- 분산된 환경을 고려해야하는가?
- Rate Limiter가 독립된 서비스로 동작하는가? 서비스 코드에 포함되는가?
- 제한된 경우, 클라이언트에게 알려주어야 하는가?
### 요구사항
- 처리율을 초과하는 요청은 정확하게 제한한다.
- 응답시간: 처리율 제한 장치가 응답시간에 영향을 주면 안된다.
- 가능한 적은 메모리를 사용한다.
- 분산형 처리율 제한: 하나의 처리율 제한 장치를 여러 서버나 프로세스에서 공유해야 한다.
- 예외 처리: 요청이 제한된 경우 사용자가 분명하게 알 수 있어야한다.
- Fault tolerance: 제한 장치가 시스템에 영향을 주어서는 안된다.
## 2단계: 개략적 설계안 제시
- 처리율 제한 장치는 어디에 둘 것인가?
- 서버: API 서버측에 제한 장치를 둔다.
- 미들웨어: API 서버로 가는 요청을 통제한다.
- 제한된 요청이라고 판단되면 서버에 안보내고, 미들웨어 단에서 HTTP 429(Too many requests) 반환한다.
- Cloud MSA 구조에서 보통 API Gateway를 활용합니다: 처리율 제한, SSL termination, 사용자 인증, IP Whitelist
![image](https://github.com/user-attachments/assets/11bb47f5-4b9f-47bc-9f81-38dc5ae647e8)
### 고려사항
- 서버나 미들웨어 어디에 둘 것인가에대한 정답은 없다.
- 프로그래밍 언어, 캐시 서비스 등 기술 스택 점검: 현재 서버 측 구현을 지원하기 충분할 정도록 효율이 높은가 판단한다.
- 사업 필요에 맞는 처리율 제한 알고리즘 찾기: 제3 사업자가 제공하는 게이트웨이를 사용하기로 했다면 선택지가 제한될 수도 있다.
## 처리율 제한 알고리즘
### 토큰 버킷 (Token Bucket) 알고리즘
#### 동작 원리
- 버킷: 이 버킷은 토큰을 저장하는 곳이다. 시스템에 들어오는 각 요청을 처리하기 위해 토큰을 하나씩 사용한다.
- 토큰 추가: 정해진 속도로 버킷에 토큰이 추가된다. 만약 버킷이 가득 차면, 추가되지 않은 토큰은 사라진다.
- 요청 처리: 요청이 들어오면, 버킷에서 토큰을 하나 꺼내 요청을 처리한다. 토큰이 없으면, 요청은 처리될 때까지 기다려야 한다.
![image](https://github.com/user-attachments/assets/3fff8974-8556-46be-a67a-0b1716db5a2c)
#### 장점
- 구현이 쉽다.
- 메모리 사용 측면에서 효율적이다.
- 유연성: 트래픽이 일시적으로 증가하는 경우, 미리 축적된 토큰을 사용해 이를 처리할 수 있다.
- 안정성: 요청이 폭발적으로 증가하는 경우에도 시스템이 정해진 속도로만 처리하기 때문에 시스템이 안정적으로 유지된다.
#### 단점
- 복잡성: 구현과 관리가 상대적으로 복잡할 수 있다. 특히, 분산 시스템에서는 토큰의 동기화와 관리가 더 어려워질 수 있다.
- 토큰 버킷 크기: 버킷의 크기를 적절히 설정하지 않으면, 너무 많은 트래픽을 한꺼번에 처리하려 해서 시스템에 부하를 줄 수 있다.
#### 예시
웹 API에서 초당 최대 100개의 요청을 처리하고 싶다고 가정해보자. 이 경우, 토큰 버킷 알고리즘을 사용하여 초당 100개의 토큰을 버킷에 추가하고, 각 요청을 처리할 때마다 토큰을 하나씩 사용한다. 만약 어느 순간에 150개의 요청이 동시에 들어온다면, 처음 100개의 요청은 즉시 처리되고 나머지 50개는 토큰이 다시 채워질 때까지 대기하게 된다.
