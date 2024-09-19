# PBR(Policy Based Routing)
- 데이터가 전달되는 과정에서 서로 다른 네트워크들을 통과해야 하는 경우가 생길 수 있다.
- 여러 네트워크들의 연결을 담당하고 있는 라우터 장비가 데이터의 목적지가어디인지 확인하여 빠르고 정확한 길을 찾아 전달하는 기술을 라우팅이라고 한다.
- 라우팅을 설정하는 방법으로는 Static, OSPF, BGP, EIGRP, RIP 등이 있지만 그 중에서도 특정 정책 기반으로 라우팅을 하는 PBR에 대해 알아보자.
- 정적 경로 라우팅 (Static 등)이나 동적인 라우팅 (OSPF 등)은 패킷의 목적지 주소만 참조하여 라우팅 경로를 결정한다.
- PBR을 사용할 경우 정책 필터로 데이터 패킷을 라우팅하여 Route map을 이용해 특정 조건에 해당하는 패킷을 라우팅 테이블과 상관없이 관리자가 원하는 곳으로 전송하게 하는 기능을 말한다.
- 패킷의 출발지 또는 출발지 및 목적지 주소에 따라 원하는 경로를 선택할 수 있기 때문에 경우에 따라 유용하게 사용 가능하다.
1. 일반적인 정적 경로로 라우팅 하여 설정할 경우
![image](https://github.com/user-attachments/assets/7ab9626c-f123-4962-b692-b9051d807d81)
- 위와 같은 그림에서 Router1의 default Routing을 ip route 0.0.0.0 0.0.0.0 1.1.1.2로 설정할 경우, Router1에서 Router3로 통신했을 경우 데이터 전송은 AD 값이 가장 낮은 Static으로 통신이 되어 Router1 -> Router2 -> Router3 순서로 통신을 하게 된다.
- 설정 예시 ip route [ 목적지의 주소 ] [ 서브넷 마스크 ] [ address | interface ]
- * AD : 라우팅 프로토콜에서 라우팅의 우선 순위를 결정하기 위한 값
2. PBR을 설정하여 특정 데이터의 통신 경로를 변경하는 경우
- Route map은 패킷이 어떤 Next-hop Router로 Routing 될 것인지를 결정하는데, 이때 최단 경로가 아닌 다른 방법으로 Routing을 하고 싶은 경우 PBR을 사용할 수 있다.
- 필요에 따라 규칙을 생성하여 원하는 패킷을 다른 경로로 통신할 수 있게끔 PBR을 이용하여 아래 그림과 같이 설정할 수 있다.
![image](https://github.com/user-attachments/assets/e8c1341f-33c7-4a79-b125-2be3aba5562d)

