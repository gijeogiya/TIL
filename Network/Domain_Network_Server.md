# DNS(Domain Network Server)
- 도메인 <-> IP 호스팅
- Q. Chrome 브라우저에 네이버 주소를 입력했을 떄 일어나는 일
- UDP 프로토콜
- 1. 브라우저 캐시 확인
  2. hosts 파일 검색
  3. OS 캐시 확인 = DNS Cache Table
* - hosts file과 OS/DNS Cache는 실시간으로 동기화 된다.
  4. 라우터 캐시 확인
  5. ISP(인터넷 서비스 공급자: KT, Skt... 등등)캐시 확인
  - 'nslookup' DNS에 IP를 질의하는 명령어
  6. Local DNS Server "권한이 없는 응답"
  DNS 서버끼리는 TCP로 연결되어 동기화됨
