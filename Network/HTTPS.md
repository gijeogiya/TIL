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
## Server Key Exchange / ServerHello Done
- 'Server Key Exchange'는 Server의 공개키가 SSL 인증서 내부에 없는 경우, Server가 직접 전달함을 의미
- 공개키가 SSL 인증서 내부에 있을 경우 Server Key Exchange는 생략됨
- 인증서 내부에 공개키가 있다면 Client가 CA(Certificate Authority, 인증기관)의 공개키를 통해 인증서를 복호화한 후 Server의 공개키를 확보할 수 있음. 그래고 Server가 행동을 마쳤음을 전달
![Server Key Exchange](https://github.com/gijeogiya/TIL/assets/97646078/57fa3e48-33ff-4642-8bc0-cea18c629171)
위의 경우, 키 교환 알고리즘이 Diffie-Hellman(DH, DHE 등) 알고리즘이기에 키 교환 재료를 서로 교환하므로 'Server Key Exchange'를 발생시킴
## Client Key Exchange
- 대칭키(비밀키, 데이터를 실제로 암호화하는 키)를 Client가 생성하여 SSL 인증서 내부에서 추출한 Server의 공개키를 이용해 암호화한 후 Server에 전달
- 여기서 전달된 '대칭키'가 바로 SSL Handshake의 목적이자 가장 중요한 수단인 데이터를 실제로 암호화할 대칭키(비밀키)
- 이제 키를 통해 Client와 Server가 교환하고자 하는 데이터를 암호화함
![Client Key Exchange](https://github.com/gijeogiya/TIL/assets/97646078/f13e3159-743a-4024-ac09-ab6cc602f41f)
- Client가 데이터를 암호화할 대칭키(비밀키)를 보낸다고 했는데 'EC Diffie-Hellman Client Params', 즉 키를 생성할 재료를 보냄
- 키교환 알고리즘을 RSA가 아닌 Diffie-Hellman(DH, DHE 등) 알고리즘과 타원곡선 암호인 ECDHE(Elliptic Curve DHE)을 사용하게 된다면 Client가 데이터를 암호화할 대칭키(비밀키)를 보내는 것이 아니라 대칭키(비밀키)를 생성할 재료를 Client와 Server가 교환하게 됨
- 서로 교환한 각자의 재료를 합쳐 동일한 대칭키를 만들 수 있음
- Diffie-Hellman(DH, DHE 등)과 타원곡선 암호인 ECDHE(Elliptic Curve DHE)의 특징
- RSA 키교환 알고리즘을 사용하게 되면 Client가 대칭키(비밀키)를 생성하여 인증서 내부에 들어 있던 서버의 공개키로 암호화 한 후 전달하게 됨
## ChangeCipherSpec / Finished
- Client, Server 모두가 서로에게 보내는 Packet으로 교환할 정보를 모두 교환한 뒤 통신할 준비가 다 되었음을 알리는 패킷
- 'Finished' Packet을 보내어 SSL Handshake를 종료하게 됨
![ChangeCipherSpec](https://github.com/gijeogiya/TIL/assets/97646078/279434b1-bfdf-4d40-ae6f-e5decf7442c9)
## SSL Handshake 요약
1. ClientHello: 암호화 알고리즘 나열 및 전달
2. ServerHello: 암호화 알고리즘 선택
3. Server Cerificate: 인증서 전달
4. Client Key Exchange: 데이터를 암호화할 대칭키 전달
5. Client / Server Hello Done: 정보 전달 완료
6. Finished: SSL Handshake 종료
- 과정이 끝나면 Client와 Server는 데이터를 암호화할 동일한 대칭키(비밀키)를 갖게됨
- 서로에게 각자 갖고 있는 동일한 대칭키를 통해 데이터를 암호화하여 전송하거나 데이터를 복호화함

## 서버에서의 알고리즘 선택
- 웹서버 등은 인바운드 포트, 아웃바운드 포트 마다 알고리즘 정책을 달리 할 수 있다.
- 보안적으로 민간한 통신의 경우 높은 버전의 TLS 알고리즘을 강제하면 보안성을 강화 할 수 있다.
