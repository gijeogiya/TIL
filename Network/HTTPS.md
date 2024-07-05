# HTTPS
## SSL Handshake(TLS Handshake)
- HTTPS 통신과정에서 송신자와 수신자가 암호화 통신을 하기 위한 **방법**과 **수단**에 대해 공유하는 것
- 데이터를 암화화할 대칭키(비밀키)를 타인에게 노출시키지 않고 Client가 Server에게 전송하기 위해 협상을 벌이는 것
- 협상과정에는 SSL 인증서 전달, 대칭키(비밀키) 전달, 암호화 알고리즘 결정, SSL/TLS 프로토콜 결정 등이 포함됨
![SSL Handshake의 과정](https://github.com/gijeogiya/TIL/assets/97646078/4eed041b-5ea5-4878-b6b5-2a4df526b08a)
- 파란색 칸과 노란색 칸은 네트워크 상에서 전달되는 IP Packet을 표현
- 맨 윗줄의 SYN, SYN ACK, ACK는 TCP Layer의 3-way handshake로 HTTPS가 TCP 기반의 프로토콜이기 때문에 암호화 협상(SSL Handshake)에 앞서 연결을 생성하기 위해 실시하는 과정
- 아래 노라색 상자의 패킷들이 SSL Handshake
1. 암호화 알고리즘(Cipher Suite) 결정
2. 데이터를 암호화할 대칭키(비밀키) 전달
## Client Hello
- Client가 Server에 연결을 시도하며 전송하는 패킨
- 자신이 사용가능한 Cipher Suite 목록, Session ID, SSL Protocol Version, Random Byte 등을 전달
![ClientHello Packet](https://github.com/gijeogiya/TIL/assets/97646078/72c6230c-5adf-4758-8d1b-612c043063b5)
![Chiper Suite의 구성](https://github.com/gijeogiya/TIL/assets/97646078/31435b03-29ed-4d11-b88f-800af958540f)
## Server Hello
- Client가 보내온 ClientHello Packet을 받아 Cipher Suite 중 하나를 선택한 다음 Client에게 이를 알림
![ServerHello Packet](https://github.com/gijeogiya/TIL/assets/97646078/60a6983e-492b-4431-871b-4129e9f6dcb1)
## Certificate
- Server가 자신의 SSL 인증서를 Client에게 전달
- 인증서 내부에는 Server가 발행한 공개키(단, 개인키는 Server가 소유)가 들어있음
- Client는 Server가 보낸 CA(Certificate Authority, 인증기관)의 개인키로 암호화된 이 SSL 인증서를 이미 모두에게 공개된 CA(Certificate Authority, 인증기관)의 공개키를 사용하여 복호화함
- 복호화에 성공하면 이 인증서는 CA(Certificate Authority, 인증기관)가 서명한 것이 맞는 것이니 진짜임이 증명됨
- Client는 데이터 암호화에 사용한 대칭키(비밀키)를 생성한 후 SSL 인증서 내부에 들어 있던(Server가 발행한) 공개키를 이용하여 암호화 하여 Server에게 전송
![Certificate Packet](https://github.com/gijeogiya/TIL/assets/97646078/c81fd3ce-d8d5-4a0c-a5d8-9159773e9062)

