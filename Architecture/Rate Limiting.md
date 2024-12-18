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
- Cloud MSA 구조에서 보통 API Gateway를 활용한다: 처리율 제한, SSL termination, 사용자 인증, IP Whitelist
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
### 노출 버킷 (Leaky Bucket) 알고리즘
#### 동작 원리
- 버킷: 버킷은 들어오는 요청(물)을 저장하는 역할을 한다.
- 노출(Leak): 버킷에 구멍이 나 있어서 일정한 속도로 물이 빠져나간다. 이 빠져나가는 물은 시스템이 처리할 수 있는 요청을 의미한다.
- 과부하: 버킷(버퍼)가 가득 차면, 새로운 요청은 버릴 수 있다. 이는 네트워크 혼잡 상황에서 시스템이 넘치지 않게 하는 역할을 한다.
![image](https://github.com/user-attachments/assets/bc909e79-8fe9-4e00-b164-31ed196e5763)
#### 장점
- 큐의 크기가 제한되어 있어 메모리 사용량 측면에서 효율적이다.
- 균일한 처리율: 시스템이 일정한 속도로 요청을 처리하므로, 트래픽 폭증 시에도 안정적이다.
- 간단한 구현: 노출 버킷 알고리즘은 구현하기가 비교적 간단하며, 이해하기 쉽다.
#### 단점
- 유연성 부족: 일정한 속도로만 요청을 처리할 수 있으므로, 일시적인 트래픽 증가에 유연하게 대응하기 어렵다.
- 버퍼 오버플로우: 요청이 많이 들어올 경우 버킷이 가득 차서 새로운 요청을 버려야 할 수 있다. 이는 요청 손실을 의미한다.
#### 예시
- 네트워크 트래픽 관리: 노출 버킷 알고리즘은 네트워크 라우터에서 패킷을 균일하게 전송하기 위해 사용될 수 있다. 네트워크의 처리율을 넘어서는 패킷은 버킷에서 기다리게 된다.
- API 요청 제한: 웹 서비스에서 초당 요청 수를 제한하기 위해 사용될 수 있다. 초당 100개의 요청만 처리하도록 설정된 서비스의 경우, 이 알고리즘이 적합하다.
### 고정 윈도우 카운터 (Fixed Window Counter) 알고리즘
#### 동작 원리:
- 시간 윈도우 설정: 고정 윈도우 카운터는 전체 시간을 동일한 크기의 '윈도우'로 나눈다. 예를 들어, 하루를 24개의 1시간짜리 윈도우로 나눌 수 있다.
- 카운터: 각 윈도우마다 하나의 카운터가 있다. 요청이 들어올 때마다 해당 윈도우의 카운터가 1씩 증가한다.
- 요청 제한: 각 윈도우에 설정된 한계에 도달하면, 그 윈도우에서는 더 이상 요청을 받지 않는다. 새 윈도우가 시작될 때까지 기다려야 한다.
![image](https://github.com/user-attachments/assets/b12419e1-8603-4569-8114-0b0f889a6193)
#### 장점
- 단순성: 구현하기 쉽고 이해하기 간단하다. 복잡한 알고리즘이 필요 없는 작은 시스템이나 애플리케이션에 적합할 수 있다.
- 성능: 카운터만 업데이트하면 되기 때문에, 매우 빠르고 효율적이다.
#### 단점
- 버스트 트래픽 처리 어려움: 윈도우가 바뀔 때마다 요청 한도가 초기화되므로, 윈도우가 바뀌는 순간에 요청이 몰리면 시스템에 큰 부하가 발생할 수 있다.
- 정확한 제한 어려움: 정확한 초 단위로 요청을 제한하기 어렵다. 예를 들어, 1분 윈도우에서 60개의 요청을 허용하는 경우, 첫 10초에 모든 요청이 몰릴 수도 있다.
![image](https://github.com/user-attachments/assets/3d60fef9-c4cb-4f5c-8c17-73b9b45d2239)
#### 예시
웹사이트에서 사용자가 게시물을 업로드할 수 있는 횟수를 하루에 24회로 제한한다고 가정해보자. 고정 윈도우 카운터를 사용하여 하루를 24개의 1시간 윈도우로 나누고, 각 윈도우마다 1회의 업로드만 허용한다. 사용자는 매시간마다 최대 1개의 게시물을 업로드할 수 있으며, 그 이상은 다음 시간까지 기다려야 한다.    
고정 윈도우 카운터 알고리즘은 그 구현의 단순성 때문에 많은 시스템에서 널리 사용되고 있다. 하지만 실제 사용 시에는 그 한계와 단점을 고려하여, 시스템의 요구사항과 트래픽 패턴에 맞게 적절히 조정하거나 다른 알고리즘과 결합하여 사용하는 것이 좋다. 초보자들도 이 원리를 이해하고 적용해보면, 시스템의 트래픽을 보다 효과적으로 관리할 수 있을 것이다.   
### 이동 윈도우 로그 (Sliding Window Log) 알고리즘
#### 동작 원리
- 이동 윈도우 로그 알고리즘은 시간의 흐름에 따라 요청을 유연하게 처리할 수 있는 방법이다. 이 알고리즘은 윈도우의 고정된 크기를 유지하면서 시간이 지남에 따라 윈도우를 '슬라이딩' 시키는 방식으로 작동한다.
- 로그 기록: 각 요청이 들어올 때, 그 요청의 타임스탬프를 로그에 기록한다. 타임스탬프 데이터는 보통 Redis의 정렬 집합(sorted set)같은 캐시에 보관한다.
- 이동 윈도우: 현재 시간을 기준으로 과거 일정 시간(예: 1분) 동안의 요청만을 고려한다. 시간이 지나면서 이 윈도우는 계속 앞으로 이동한다.
- 윈도우 업데이트: 새로운 요청이 들어올 때마다 윈도우를 업데이트하여, 오래된 요청을 윈도우에서 제거하고 최근 요청을 포함시킨다.
![image](https://github.com/user-attachments/assets/90514b30-a3e5-49a9-a2a4-e0352dd0e478)
![image](https://github.com/user-attachments/assets/eb2428d2-8f05-4148-adde-8d8e485a5931)
#### 장점
- 유연성: 이동 윈도우 로그는 시간이 지남에 따라 요청을 더 유연하게 처리할 수 있어, 순간적인 트래픽 증가에도 잘 대응할 수 있다.
- 정밀한 제어: 어느 순간의 윈도우를 보더라도 허용되는 요청의 개수는 시스템의 처리율 한도를 넘지 않는다.
#### 단점
- 자원 소모: 각 요청의 타임스탬프를 저장하고 관리해야 하므로, 많은 요청을 처리하는 시스템에서는 메모리 사용량이 증가할 수 있다.
- 구현 복잡성: 이동 윈도우 로그 알고리즘은 다른 방법에 비해 구현이 복잡할 수 있으며, 정확한 시간 관리와 로그 처리가 필요하다.
#### 예시
실시간 채팅 애플리케이션에서 사용자가 초당 보낼 수 있는 메시지 수를 제한하고 싶다고 가정해 보자. 이동 윈도우 로그 알고리즘을 사용하여, 사용자가 지난 10초 동안 보낸 메시지 수를 추적하고, 이 숫자가 설정된 한도를 넘으면 추가 메시지를 일시적으로 차단할 수 있다. 시간이 지나면서 윈도우가 이동하고, 사용자는 새로운 윈도우 내에서 다시 메시지를 보낼 수 있다.    
이동 윈도우 로그 알고리즘은 특히 시간에 따라 변하는 트래픽 패턴을 가진 시스템에서 유용하다. 이를 통해 시스템은 순간적인 부하에도 안정적으로 서비스를 제공할 수 있으며, 사용자에게 일관된 서비스 품질을 보장할 수 있다. 초보자들은 이 원리를 이해하고 적용함으로써, 시스템의 성능과 사용자 경험을 크게 향상시킬 수 있을 것이다.
### 이동 윈도우 카운터 (Sliding Window Counter) 알고리즘
- 이동 윈도우 카운터 알고리즘은 처리율을 제한하고, 시스템의 부하를 관리하는 데 사용되는 방법이다. 이 알고리즘은 특히 동적인 웹 애플리케이션과 서비스에서 유용하게 사용된다.
#### 동작 원리
- 이동 윈도우 카운터는 이름에서 알 수 있듯이, 시간의 '윈도우'를 이용하여 요청의 수를 계산하고 제한한다.
- 시간 윈도우: 시간을 작은 단위로 나누어 각 단위마다 요청 수를 세는 카운터를 둔다.
- 이동: 윈도우는 시간이 지남에 따라 '이동'한다. 즉, 새로운 시간 단위가 시작될 때마다 최신 요청을 반영하여 카운터를 업데이트한다.
- 요청 제한: 설정된 시간 동안 허용된 최대 요청 수를 넘으면, 추가 요청은 거부되거나 지연된다.
![image](https://github.com/user-attachments/assets/df247656-3d87-4d24-a02b-dfba7b5bc4e0)
#### 장점
- 이전 시간대의 평균 처리율에 따라 현재 윈도우의 상태를 계산하므로 짧은 시간에 몰리는 트래픽에 잘 대응한다.
- 정밀한 제어: 시간 단위로 요청을 세밀하게 관리할 수 있어, 순간적인 트래픽 증가에도 유연하게 대응할 수 있다.
- 효율적인 자원 사용: 고정 윈도우 카운터에 비해 더 많은 요청을 처리할 수 있으며, 자원을 보다 효율적으로 사용한다.
#### 단점
- 구현 복잡성: 이동 윈도우 카운터는 구현이 복잡할 수 있으며, 시간 관리와 카운터 업데이트에 주의가 필요하다.
- 메모리 사용량: 각 시간 단위마다 카운터를 유지해야 하므로, 많은 요청을 처리하는 시스템에서는 메모리 사용량이 증가할 수 있다.
#### 예시
온라인 투표 시스템에서 사용자가 1분 동안 최대 10번만 투표할 수 있도록 설정한다고 가정해 보자. 이동 윈도우 카운터를 사용하여, 각 사용자의 투표 요청을 1분간의 윈도우로 추적한다. 사용자가 1분 동안 10번 투표하면, 추가 요청은 다음 1분이 시작될 때까지 기다려야 한다.    
이동 윈도우 카운터 알고리즘은 특히 요청의 수를 시간에 따라 정밀하게 제어해야 하는 시스템에서 유용하다. 초보자들은 이 알고리즘의 원리를 이해하고 적용함으로써, 시스템의 트래픽을 보다 효과적으로 관리하고 사용자에게 안정적인 서비스를 제공할 수 있을 것이다.    
## 개략적인 아키텍처
### 처리율 제한 알고리즘의 기본 아이디어
처리율 제한의 핵심은 '카운터'라는 간단한 아이디어에 기반한다. 시스템은 들어오는 모든 요청을 추적하고, 이 카운터 값이 설정한 한도를 초과하면 요청을 거부한다.    
### 카운터의 보관
이 카운터를 관리하는 효율적인 방법 중 하나는 메모리상에서 동작하는 캐시를 사용하는 것이다. 이는 빠른 접근과 시간 기반 만료 정책을 제공하기 때문에, 처리율 제한 장치에 이상적이다.
### Redis 사용 예
- Redis는 메모리 내 저장소로, 처리율 제한 구현에 자주 사용된다. 주요 명령어로는 **INCR**과 **EXPIRE**가 있다.
- INCR: 메모리에 저장된 카운터의 값을 1만큼 증가시킨다.
- EXPIRE: 카운터에 타임아웃 값을 설정한다. 설정된 시간이 지나면 카운터는 자동으로 삭제된다.
![image](https://github.com/user-attachments/assets/eafd7a38-1ae2-488c-8c10-9f9fbe4a0286)
#### 동작 원리
1. 클라이언트가 미들웨어 요청을 보낸다.
2. 미들웨어는 Redis에서 해당 카운터 값을 확인하여 요청 한도에 도달했는지 검사한다.
3. 한도에 도달한 경우 요청을 거부한다.
4. 한도에 도달하지 않았다면, 요청을 API 서버로 전달하고 카운터 값을 1 증가시킨 후 Redis에 저장한다.
### 처리율 제한을 회피하는 방법
처리율 제한을 효과적으로 관리하려면 몇 가지 전략을 고려할 수 있다.    
- 클라이언트 측 캐싱을 사용하여 필요한 API 호출 수를 줄인다.
- 처리율 제한의 한계를 이해하고, 짧은 시간에 너무 많은 요청을 보내지 않도록 한다.
- 예외나 에러를 처리하는 코드를 도입하여 클라이언트가 예외적 상황으로부터 gracefully 복구가 될 수 있도록 한다.
- 재시도 로직을 구현할 때는 충분한 백오프(back-off) 시간을 둔다.
### API 최적화
가능한 경우, 데이터를 효율적으로 요청하기 위해 API 호출을 최적화한다. 예를 들어, 대량의 데이터를 한 번에 가져오는 대신 필요한 데이터만 선택적으로 요청하거나, 여러 작업을 한 번의 API 호출로 결합할 수 있다.    
### 멀티 쓰레딩/비동기 처리
클라이언트에서 멀티 쓰레딩이나 비동기 호출을 사용하여 API 사용을 최적화하고, 서버 응답을 기다리는 동안 다른 작업을 수행할 수 있다. 그러나 이 방법은 서버에 부담을 줄 수 있으므로 적절한 백오프와 재시도 전략이 필요하다.   
### 주의해야 할 점
- 처리율 제한 정책 이해: 처리율 제한을 회피하는 것이 아니라 정책을 이해하고 존중하는 것이 중요하다. 처리율 제한은 일반적으로 서비스의 안정성을 보장하고 모든 사용자에게 공정한 사용을 보장하기 위해 존재한다.
- 서버 부하 고려: 과도한 재시도나 높은 처리율 요청은 서버에 부담을 줄 수 있다. 서비스 제공자와의 긴밀한 소통을 통해 적절한 사용 한도를 설정하고, 필요하다면 제한을 완화하기 위한 방안을 협의하는 것이 좋다.
- 분산 시스템 활용: 여러 클라이언트 또는 서비스 인스턴스를 통해 요청을 분산시킬 수 있다. 그러나 이는 API 제공자의 정책에 따라 제한될 수 있으므로 주의가 필요하다.
- 모니터링 도구 사용: API 사용률, 에러율, 재시도 횟수 등을 모니터링하여 시스템의 성능을 지속적으로 관찰하고, 필요한 조치를 취할 수 있다.

