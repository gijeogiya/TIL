# Session & Load Balanser
세션은 JVM에 저장된다. 따라서 서버가 분산되어 있다면 단순한 방식대로는 동작하지 않는다. A서버 메모리의 세션 맵과 B서버 메모리의 세션 맵이 다르기 때문이다.
![image](https://github.com/user-attachments/assets/88f26215-5d99-4b74-99e2-3b82b60691b9)   
이를 극복할 수 있는 몇 방안을 간략하게 소개하겠다.
## Sticky Session
![image](https://github.com/user-attachments/assets/df950e77-eb54-4790-9650-437becd56336)   
한 사용자가 처음 세션에 참여한 서버로 접속을 고정시킨다. `유저1`이 `서버B`에 요청을 보냈다면, 세션이 유지되는 동안 `서버B`와 통신을 주고받게 된다.
## Session Clustering
![image](https://github.com/user-attachments/assets/511329a5-cbb2-4aa4-a68b-a354140c21da)   
서버 간에 세션을 복사해 공유한다. 한 서버에서 생성된 세션이 모든 서버에 복사되기에, 어떤 서버에 접속하더라도 같은 세션값을 받을 수 있다. 하지만 `Sticky Session`과 같이 유지 비용이 많이 든다.
## Session Storage DB
![image](https://github.com/user-attachments/assets/5598e728-39eb-4f7c-8bfa-f870a3418c10)   
외부에 세션 저장소를 따로 둔다. 앞선 두 방법 보다 비용 측면에서 나아 보이지만, 분산 서버의 많은 요청이 외부 저장소로 들어갔을 때 부하가 생길 수 있다.
## Token
토큰이란 단어는 아주 광범위하게 쓰인다. 예를 들어 java StringTokenizer의 토큰은 문자열을 자르는 데 이용되는 특정한 문자열이다. jwt의 토큰은 생성 정보와 키, 값 쌍을 인코딩한 문자열이다. 여러 사례를 보고 내가 일반화한 CS의 토큰은 특정 값을 식별하는데 사용되는 키이다.   
토큰 기반 인증은 사용자가 서버에서 발급받은 토큰을 요청마다 함께 주는 방식이다. 얼핏 보면 세션ID를 쿠키로 전달하는 것과 비슷해보이지만, 전달받은 값을 서버에서 처리하는 방식이 다르다. 토큰은 저장소에 접근하지 않고, 서버에서 유효성을 검증한다. 따라서 분산 서버 환경이어도 문제가 없다.   
다만 Access Token과 Refresh Token을 함께 사용하는 경우에는 Refresh Token을 DB에 저장하게 된다. 이번 포스팅에서 마저 다루기엔 내용이 길기에, 대신 잘 정리되어 있는 다른 블로그 포스팅 링크를 남기겠다. 토큰에 대해 알아보며 토큰을 사용한 대표적인 인증 방식인 OAuth도 함께 공부할 필요성을 느껴서 함께 올린다.   
### Session ID는 토큰일까요 아닐까요?
인증 방식과 CS의 토큰의 사례를 생각해보면 `session id == session token`이다
