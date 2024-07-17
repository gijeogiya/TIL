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
- 
