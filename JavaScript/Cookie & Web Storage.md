# Cookie & Web Storage
- 쿠키와 웹 스토리지(웹 스토리지는 두개로 나눠진다. Local Storage, Session Storage)에 대한 이야기는 화면을 다루는 개발에서 자주 등장한다.
- 이는 웹 클라이언트에 무언가를 저장하기 위해 쿠키와 웹 스토리지를 사용하기 때문이라 생각한다.
- 이때 저장할 무언가로는 로그인 정보가 될 수도 있고 해당 웹 사이트에 언어 정보가 될수도 있을 것이다.

## 관련한 면접 빈출 질문들
- Cookie와 Web Storage에 대해 비교 설명해주세요.
- Cookie와 Web Storage 각각의 장,단점이 존재하는데 그에 대해 설명해주세요.
- 세션과 쿠키에 대해 설명해주세요. (사실 세션과 쿠키는 이번 포스팅에서 중점을 둘 저장소와는 또 다른 
내용이지만 세션과 쿠키를 어디에 저장하느냐를 이어 설명할 때 스토리지 개념이 나올 수 있다고 본다.)
- 로그인 처리는 어떻게 하셨는지 설명해주세요.
- 토큰을 받아와 어디에 저장했나요?

## 쿠키와 웹 스토리지는 왜 사용하는걸까?
- HTTP 프로토콜은 비연결성(Connectionless)과 비상태성(Stateless) 이라는 특성을 가지고 있다.
- 비연결성은 서버에 연결 후 request 에 response 를 받으면 연결을 바로 끊어버리는 특성이고,
- 비상태성은 통신이 끝나면 상태를 유지하지 않는 특징이다.

- 즉, 비연결성이라는 특성 때문에 연결이 끊어지고 나면 클라이언트와 서버 사이에 통신이 끝난 것이기 때문에 상태를 유지하지 않게 되는 것이다. 이것이 왜 문제가 될까? 예를 들어,
1. A가 옷이 사고 싶어져서 항상 자주가는 사이트에 접속을 했다.
2. A는 그 사이트에 들어가자마자 로그인하기를 눌렀고 로그인에 성공했다.
3. 그런데 실제로 옷을 구매하려고 하니 로그인 했던 상태가 유지되지 않아 다시 로그인을 해야한다.

- 이러한 비연결성과 비상태성을 보완하고자 서버에 새로운 요청을 보낼 때 유지하고싶은 상태들을 클라이언트에 저장해두는 것이다.
- HTML5가 나오기 전까지는 쿠키가 상태를 저장하는 주된 방법이었으나 HTML5가 나온 후에는 HTML5가 지원하는 웹 스토리지(Local Storage, Session Storage)에도 상태를 저장해둘 수 있게 되었다.

## 쿠키
쿠키는 현재 사이트를 이용하는 사용자가 로그인을 했던 사용자면 로그인을 유지시켜 주고, 사용자가 설정해 둔 환경설정(예를 들어, 오늘동안 팝업 보지 않기, 사이트 언어를 한국어로 설정하기)등을 기억하며 사용자가 해당 사이트를 다시 접속하게 됐을 때 이전에 설정해 둔 그대로의 모습을 보여주게된다.       

![image](https://github.com/user-attachments/assets/5e57aa8b-4267-43d7-aec8-22e1589c907e)

클라이언트에 저장돼있는 쿠키 값들은 Inspect - Application - Cookie에서 확인할 수 있다.      

![image](https://github.com/user-attachments/assets/c1b67475-da19-44f9-9a04-b71eaa972543)

## 쿠키의 특징
쿠키는 document.cookie 을 이용해 클라이언트에서 직접 값을 만들어 낼수도 있지만 주로 웹 서버에서 만들어진다.      
### 예시
1. 사용자가 로그인 request를 보내면 서버는 사용자에 로그인 요청에 대해 HTTP response를 보낸다.
   - 이 서버의 응답 헤더에 Set-Cookie에는 인증된 사용자의 정보가 담겨있고 이는 브라우저에 저장된다.
2. 사용자가 동일한 사이트(동일한 도메인)에서 새로운 request를 보내려 하면 브라우저는 HTTP request 헤더에 인증된 사용자의 정보가 담긴 쿠키 값을 자동으로 추가하여 보낸다.
3. 서버는 헤더에 담겨 날라온 인증된 사용자의 정보를 확인하고 사용자를 식별하게 된다.

