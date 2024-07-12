# Cipher Suite(암호문의 집합)
## 배경지식 정리
- SSL Handshack는 암호화 알고리즘 결정과 대칭키(비밀키) 전달을 위해 사용
- SSL Handshack의 첫 단계, Client가 'Client Hello'로 협상을 시작할 때 자신이 사용 가능한 'Cipher Suite'를 쭉 나열
- Server가 'Server Hello'를 통해 자신이 고른 'Cipher Suite'을 전달
- SSL Handshake의 첫 협상 단계인 'Client Hello'와 'Server Hello'에서 'Cipher Suite'가 가장 먼저 언급되는 것을 통해 'Cipher Suite'의 중요성을 알 수 있다.

## Cipher Suite
- Cipher: 암호
- Suite: 세트, 모음
- 암호를 모아 만든 집합소
![Cipher Suite](https://github.com/user-attachments/assets/47581545-861b-43fa-beba-3551aaea89a8)
## SSL/TLS Protocol
- SSL Handshake에 기반이 되는 SSL/TLS Protocol의 버전을 의미
- 보통 SSL v3, TLS v1.0, TLS v1.1, TLS v1.2등이 있고 Cipher Suite에서는 SSL 혹은 TLS로 표기됨
- Client Hello Packet에서 Version 항목을 통해 확인 할 수 있음
- 최근 Google Chrome에서 TLSv1.0, TLSv1.1의 지원을 종료하겠다는 발표가 있었음. 해당 버전의 프로토콜을 빼게 되면 해당 프로토콜과 연결된 Cipher Suite는 사용할 수 없음
![TLS Version 확인](https://github.com/user-attachments/assets/fb4e4f30-951f-4267-8552-a1071ed1b562)
## 키 교환 방식(키 교환 알고리즘)
- SSL Handshake의 **목표**이자 데이터를 암호화하는 실질적인 키인 **대칭키(비밀키)**를 서버에게 전달하기 위한 방법(알고리즘) 선택을 의미
- 주로 ECDHE, RSA 등이 사용됨
### RSA와 Diffie-Hellman(DH)
#### RSA(로널드 라이베스트(R), 아디 샤미르(S), 레너드 애들먼(A) 이름의 앞글자) 암호
