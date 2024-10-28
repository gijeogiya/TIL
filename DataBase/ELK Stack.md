# ELK(ElasticSearch, Logstash, Kibana) Stack
## ELK 란?
 - 현재 4차산업시대에서 데이터는 가장 중요한 자산중 하나로 손꼽힌다.
- 빅 데이터는 통상적으로 사용되는 데이터 수집, 관리 및 처리 소프트웨어의 수용 한계를 넘어서는 크기의 데이터를 말한다.
- 빅 데이터의 사이즈는 단일 데이터 집합의 크기가 수십 테라바이트에서 수 페타바이트에 이르며, 그 크기가 끊임없이 변화하는 것이 특징이다.
![image](https://github.com/user-attachments/assets/e6f62e59-e21f-40f6-90ae-94086666df99)
- ELK는 위 그림과 같이, 분석 및 저장 기능을 담당하는 ElasticSearch, 수집 기능을 하는 Logstash, 이를 시각화하는 도구인 Kibana의 앞글자만 딴 단어이다.
- ELK는 접근성과 용이성이 좋아 최근 가장 핫한 Log 및 데이터 분석 도구이다.
![image](https://github.com/user-attachments/assets/9f5f9b3f-a1a4-4666-a08b-f5545d203b9c)
### ElasticSearch
- ElasticSearch는 Lucene 기반으로 개발한 분산 검색엔진으로, Logstash를 통해 수신된 데이터를 저장소에 저장하는 역할을 담당
- 데이터를 중심부에 저장하여 예상되는 항목을 검색하고 예상치 못한 항목을 밝혀낼 수 있다.
- 정형, 비정형, 위치정보, 메트릭 등 원하는 방법으로 다양한 유형의 검색을 수행하고 결합할 수 있다.
### Logstash
- 오픈소스 서버측 데이터 처리 파이프라인으로, 다양한 소스에서 동시에 데이터를 수집하고 변환하여 stash 보관소로 보낸다.
- 수집할 로그를 선정해서, 지정된 대상 서버(ElasticSearch)에 인덱싱하여 전송하는 역할을 담당하는 소프트웨어
### Kibana
- 데이터를 시각적으로 탐색하고 실시간으로 분석 할 수 있다.
- 시각화를 담당하는 HTML + Javascript 엔진이라고 보면 된다.
## ELK Stack 이란?
![image](https://github.com/user-attachments/assets/7933d00b-2b2b-42f5-9e05-025a10264f85)
- ELK 솔루션에서 Beats 추가되면서 ELK Stack이라고 불린다.
- Beats : 서버에 에이전트로 설치하여 다양한 유형의 데이터를 ElasticSearch 또는 Logstash에 전송하는 오픈 소스 데이터 발송자다.
