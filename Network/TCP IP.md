# TCP/IP(Transmission Control Protocol/Internet Protocol)
## TCP/IP
- 인터넷 프로토콜 스위트(Internet Protocol Suite)는 인터넷에서 컴퓨터들이 서로 정보를 주고받는 데 쓰이는 통신규약(프로토콜)의 모음이다. 인터넷 프로토콜 슈트 중 TCP와 IP가 가장 많이 쓰이기 때문에 TCP/IP 프로토콜 슈트라고도 불린다.
- TCP/IP는 패킷 통신 방식의 인터넷 프로토콜인 IP와 전송 조절 프로토콜인 TCP로 이루어져 있다. IP는 패킷 전달 여부를 보증하지 않고, 패킷을 보낸 순서와 받는 순서가 다를 수 있다. TCP는 IP 위에서 동작하는 프로토콜로, 데이터의 전달을 보증하고 보낸 순서대로 받게 해 준다. HTTP, FTP, SMTP 등 TCP를 기반으로 한 많은 수의 애플리케이션 프로토콜들이 IP 위에서 동작하기 때문에, 묶어서 TCP/IP로 부르기도 한다.
- TCP/IP는 하나의 프로토콜이 아닌 TCP와 IP를 합쳐서 부르는 말이다.
- TCP/IP를 사용하겠다는 것은 IP 주소 체계를 따르고 IP Routing을 이용해 목적지에 도달하며 TCP의 특성을 활요해 송신자와 수신자의 논리적 연결을 생성하고 신뢰서을 유지할 수 있도록 하겠다는 것을 의미한다.
- TCP/IP를 말한다는 것은 송신자가 수신자에게 IP주소를 사용하여 데이터를 전달하고 그 데이터가 제대로 갔는지, 너무 빠르지는 않는지, 제대로 받았다고 연락은 오는지에 대한 이야기를 하는 것이다.

## OSI 7 Layer 에서의 TCP/IP
### Transport Layer(4 Layer)
- 송신자와 수신자의 논리적 연결(Connection)을 담당하는 부분으로 신뢰성 있는 연결을 유지할 수 있도록 도와준다.
- Endpoint(사용자) 간의 연결을 생성하고 데이터를 얼마나 보냈는지 얼마나 받았는지 제대로 받았는지 등을 확인한다.
- TCP(Transmission Control Protocol)와 UDP(User Datagram Protocol)가 대표적
### Network Layer(3 Layer)
- IP(Internet Protocol)가 활용되는 부분으로 한 Endpoint(사용자)가 다른 Endpoint(사용자)로 가고자 할 경우, 경로와 목적지를 찾아준다.
- 이를 Routing이라고 하며 대역이 다른 IP들이 목적지를 향해 제대로 찾아갈 수 있도록 돕는 역할을 한다.
![TCP/IP를 사용하는 Browser와 Server의 통신](https://github.com/user-attachments/assets/d5afaab6-4c3c-47bc-8c69-8209ead26cb9)
- 우리가 인터넷에서 무언가 다운로드할 때 중간에 끊기거나 빠지는 부분 없이 완벽하게 받을 수 있는 이유도 TCP의 이러한 특성, 다시 말해 데이터가 빠지지 않고 제대로 전달되었는지 챙기는 꼼꼼함 덕분이다.
- 그렇기 때문에 HTTP, HTTPS, FTP, SMTP 등과 같이 데이터를 안정적으로 모두 보내는 것이 중요한 프로토콜들이 기반된다.
- TCP를 기반으로 하는 프로토콜들은 차후 언급할 TCP의 '3-way handshake'를 거친 후, 각자 프로토콜(Layer 7)에 기반한 교환 과정을 실시한다는 뜻이다.
![HTTPS의 통신과정](https://github.com/user-attachments/assets/ca4f095a-b77a-40a4-8334-9c9ae7d6ed9a)
- 위 이미지는 TCP 기반의 프로토콜인 HTTPS의 'SSL Handshake'를 도식화한 것이다.
- TCP는 Layer 4이고 HTTPS는 Layer 7이다.
- 파란색 상자는 TCP의 '3-way handshake'이고 노란색 상자는 HTTPS의 'SSL Handshake'이다.
- HTTPS는 TPC 기반의 프로토콜이기 때문에 'SSL Handshake'를 하기에 앞서 '3-way handshake'를 실시한다.
## TCP의 개요
- 전송 제어 프로토콜(Transmission Control Protocol, TCP)은 인터넷 프로토콜 스위트(IP)의 핵심 프로토콜 중 하나로, IP와 함께 TCP/IP라는 명칭으로도 널리 불린다.
- TCP는 근거리 통신망이나 인트라넷, 인터넷에 연결된 컴퓨터에서 실행되는 프로그램 간에 일련의 옥텟을 안정적으로, 순서대로, 에러 없이 교환할 수 있게 한다.
- TCP는 전송 계층에 위치한다. 네트워크의 정보 전달을 통제하는 프로토콜이자 인터넷을 이루는 핵심 프로토콜의 하나이다.
- TCP는 웹 브라우저들이 월드 와이드 웹에서 서버에 연결할 때 사용되며, 이메일 전송이나 파일 전송에도 사용된다.
- TCP는 OSI 7 Layer 중 4계층에 해당한다.
- IP가 패킷들의 관계를 이해하지 못하고 그저 목적지를 제대로 찾아가는 것에 중점을 둔다면 TCP는 통신하고자 하는 양쪽 단말(Endpoint)이 통신할 준비가 되었는지, 데이터가 제대로 전송되었는지, 데이터가 가는 도중 변질되지는 않았는지, 수신자가 얼마나 받았고 빠진 부분은 없는지 등을 점검한다.
- 이런 정보는 TCP Header에 담겨 있으며 SYN, ACK, FIN, RST, Source Port, Destination Port, Sequence Number, Window size, Checksum과 같은 신뢰성 보장과 흐름 제어, 혼잡 제어에 관여할 수 있는 요소들도 포함되어있다.
- IP Header와 TCP Header를 제외한 TCP가 실을 수 있는 데이터 크기를 '세그먼트(Segment)'라고 부른다.
![TCP Header의 구조](https://github.com/user-attachments/assets/d75d24ad-7746-4159-aa42-bdbdc03dc8c8)
- TCP는 IP의 정보 뿐만 아니라 Port를 이용하여 연결한다.
- 한쪽 단말(Endpoint)에 도착한 데이터가 어느 입구(Port)로 들어가야 하는지 알아야 연결을 시도할 수 있기 때문이다.
- 양쪽 단말(Endpoint)이 HTTP로 이루어진 문서를 주고받고자 할 경우 데이터 통신을 하려면 Endpoint의 80 Port로 연결해야 한다.
- 거대한 부산항에 도착했을 때 화무선인 나의 데이터가 상항(화물이 정박하는 항)에 들어가야지 어선항(어선이 정박하는 항)에 들어가면 안되는 것 처럼 말이다.
## TCP의 작동(3-way handshake)
-

