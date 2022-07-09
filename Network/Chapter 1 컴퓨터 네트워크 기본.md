# Chapter 1 : 컴퓨터 네트워크 기본

## The Network Edge

### Connection-oriented Service

#### TCP

**전송 제어 프로토콜**(**T**ransmission **C**ontrol **P**rotocol)

- reliable, in-order byte-stream data transfer
- flow control
- congestion control



### Connectionless Service

#### UDP

**사용자 데이터그램 프로토콜**(**U**ser **D**atagram **P**rotocol)

- unreliable data transfer
- no flow control
- no congestion control



## The Network Core

### Circuit Switching

End-end resources reserved for "call"



### Packet Switching: Statistical Multiplexing

ex) Internet

Packet switching allows more users to use network! (효율적)



#### router의 역할

- 패킷 검사
- 최적 경로 탐색



#### Delay in packet-switched networks

- nodal processing (processing delay)
  - router에서 패킷 검사에 소요되는 시간 (router 성능을 개선하면 딜레이가 줄어든다.)
- queueing (queueing delay)
  - 큐 대기 시간 (트래픽에 의해 정해진다. 정책적으로 개선)
  - 큐보다 넘치게 되면 패킷 유실(packet loss)이 일어난다.
- Transmission delay
  - 큐에서 나가는 과정의 시간 (band 폭이 클 수록 딜레이가 줄어든다.)
- Propagation delay
  - 빛의 속도



#### TCP에서 Data Loss가 일어나면 어떡하는가?

- Data 재전송
  - TCP(최초의 전송자)가 재전송하는 방법을 사용함
  - 직전 router가 재전송하는 방법을 사용하지는 않음. 모든 기능적인 메커니즘은 Edge에 밀어 넣고 중간 부분은 단순노동하도록 설계되어 있다(router는 no brain, TCP에 모든 지능이 있다.)



