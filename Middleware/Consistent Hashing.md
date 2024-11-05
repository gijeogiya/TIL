# Consistent Hashing (안정 해시 설계)
N개의 캐시 서버가 있다고 하자.      
이 서버들에 부하를 균등하게 나누는 보편적 방법은 아래의 해시 함수를 사용하는 것이다.     
> serverIndex = hash(key) % N     
> * N은 서버의 개수
       
![image](https://github.com/user-attachments/assets/96314bcb-177d-40a2-b1f9-0baed8072763)
**이 때 생길 수 있는 문제**      
서버가 추가되거나 기존 서버가 삭제되었을 경우 N 값이 바뀜     
-> 대규모 캐시 미스가 발생하게 됨.      
-> 키 재배치를 진행해야 함.
## 안정 해시
### 정의
- 안정 해시는 해시 테이블 크기가 조정될 때 평균적으로 오직 k/n 개의 키만 재배치하는 해시 기술이다.
- 여기서 k는 키의 개수이고, n은 슬롯(slot)의 개수이다.
- 이와는 달리 대부분 전통적 해시 테이블은 슬롯의 수가 바뀌면 거의 대부분 키를 재배치한다.
### 기본 구현법
안정 해시 알고리즘은 MIT에서 처음 제안되었다. 기본 절차는 다음과 같다.    
- 서버와 키를 균등 분포(uniform distribution) 해시 함수를 사용해 해시 링에 배치한다.
- 키의 위치에서 링을 시계 방향으로 탐색하다 만나는 최초의 서버가 키가 저장될 서버이다.
### 해시 공간과 해시 링
- SHA-1 을 사용한다는 가정하에 설명을 진행한다.
- 해시 함수의 출력 값 범위를 x0 부터 xn 이라고 하자.
- SHA-1의 해시 공간(hash space) 범위는 0 부터 2^160 - 1 까지로 알려져 있다
- 따라서 x0 는 0, xn 은 2^160 - 1 이며, 나머지 x1부터 xn -1 까지는 그 사이 값을 갖게 될 것이다.
![image](https://github.com/user-attachments/assets/799e75d3-c42a-4ecd-84f0-dda319c4632d)
이 해시 공간의 양쪽을 구부려 접으면 해시 링(hash ring)이 만들어진다.
![image](https://github.com/user-attachments/assets/3b714787-848a-41c8-a16f-e810b453d911)
### 해시 서버
해쉬 함수를 이용하여 IP나 이름을 이 링 위의 어떤 위치에 대응시킬 수 있다.     
![image](https://github.com/user-attachments/assets/067b0092-8e47-4d05-8292-ec52a134d916)
### 해시 키
- 나머지 연산 % 는 사용하지 않는다.
- k는 key의 약자이다. 각 키들은 해시 링 위 어느 지점에 배치할 수 있다.
![image](https://github.com/user-attachments/assets/e4a42c92-023e-4a92-9dbb-9836098a6d93)
### 서버 조회
해당 키의 위치로부터 시계 방향으로 링을 탐색해 나가면서 만나는 첫 번째 서버에 키를 저장한다.     
![image](https://github.com/user-attachments/assets/ea55b14f-9cae-4836-9bd4-2508e80d05f1)
### 서버 추가
- 안정 해시에서는 서버를 추가하더라도 키 가운데 일부만 재배치 하면 된다. (나머지 키에는 영향이 없다.)
- 예를 들어 s0 와 s3 사이에 s4 라는 새로운 서버가 추가되었을 때,
- s0와 s4 사이에 있는 키들(여기서는 k0)만 s4로 재배치 하면 된다.
![image](https://github.com/user-attachments/assets/a1f0b28e-8d0f-4b38-944d-918e9f8bd4ec)
### 서버 제거
- 마찬가지로 안정 해시에서는 서버를 제거하더라도 키 가운데 일부만 재배치 하면 된다. (나머지 키에는 영향이 없다.)
- 예를 들어 s1 서버가 제거 되었을 때
- s1에 할당되어 있던 키들(s0와 s1 사이의 키들, 여기서는 k1)만 s2로 재배치 하면 된다.
![image](https://github.com/user-attachments/assets/2395782b-55b7-4b8b-a7c6-1f93f95c973d)
### 기본 구현법의 두 가지 문제
- 서버가 추가되거나 삭제되는 상황을 감안하면 파티션(partition)의 크기를 균등하게 유지하는 게 불가능하다.
- * 파티션 : 인접한 서버 사이의 해시 공간
- 위의 서버 삭제 의 예시에서는 s1이 삭제 되었기 때문에 s2의 파티션이 다른 파티션 대비 거의 두 배로 커지게 된다.
- 해시 값에 따라 배치가 되기 때문에 균등 분포가 달성되기 어려울 수도 있다.
![image](https://github.com/user-attachments/assets/fcb0fe05-ace9-4adb-a8b9-bb120827e40c)
위의 상황을 예시로 들어보면 s0는 아무 데이터도 없는 반면 대부분의 키는 s3에 보관된다.      
### 가상 노드
![image](https://github.com/user-attachments/assets/d1995fce-ef5f-442a-acb2-1957c5b656f9)
- 가상노드를 통해 키의 분포를 더 균등하게 할 수 있다. 표준 편차가 작아져서 데이터가 고르게 분포된다.
- * 표준 편차는 데이터가 어떻게 퍼져 나갔는지를 보이는 척도다.
- * 100~200개의 가상 노드를 사용했을 경우 표준 편차의 값은 평균 5% 사이라고 한다.
- 가상 노드의 개수는 타협적 결정(tradeoff)가 필요하다.
- 가상 노드를 늘리면 표준 편차의 값은 더 떨어지나, 가상 노드 데이터를 저장할 공간은 더 많이 필요하게 된다.
## 마치며
### 안정 해시의 이점은 다음과 같다.
- 서버가 추가되거나 삭제될 때 재배치되는 키의 수가 최소화 된다.
- 데이터가 보다 균등하게 분포하게 되므로 수평적 규모 확장성을 달성하기 쉽다.
- 핫스팟(hotspot) 키 문제를 줄인다. 특정한 샤드(shard)에 대한 접근이 지나치게 빈번하면 서버 과부하 문제가 생길 수 있다. 안정 해시는 데이터를 좀 더 균등하게 분배하므로 이런 문제가 생길 가능성을 줄인다.
### 안정해시가 쓰이는 곳의 예시
- 아마존 다이나모 데이터베이스(DynamoDB)의 파티셔닝 관련 컴포넌트
- 아파치 카산드라(Apache Cassandra) 클러스터에서의 데이터 파티셔닝
- 디스코드(Discord)채팅 어플리케이션
- 아카마이(Akamai) CDN
- 매그래프(Meglev) 네트워크 부하 분산기