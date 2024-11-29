# Cookie & SameSite
- 쿠키는 아주 예전부터 쓰였던 기술이지만, 요즘에는 보안이나 개인정보보호 문제 때문에 쿠키에 SameSite 같은 속성이 추가되기도하고 브라우저가 쿠키를 다루는 방식도 점차 바뀌어가고 있다.
- 쿠키에 대한 기본적인 이해를 바탕으로 SameSite 속성은 왜 나온 것인지, 브라우저들은 어떻게 동작하고 있는지 알아보자
## 쿠키
- 쿠키는 브라우저에 데이터를 저장하기 위한 수단 중 하나입니다. 브라우저에서 서버로 요청을 전송할 때 그 요청에 대한 응답에 `Set-Cookie` 헤더가 포함되어있는 경우, 브라우저는 `Set-Cookie` 에 있는 데이터를 저장하고, 이 저장된 데이터를 쿠키라고 부른다.
![image](https://github.com/user-attachments/assets/fc865cf2-6d59-4b45-9272-e17d18817d15)
- Set-Cookie 헤더가 포함된 경우, normal 이라는 이름의 쿠키에 yes라는 값이 저장된다.
- 이렇게 저장된 쿠키는 다음에 다시 그 브라우저에서 서버로 요청을 보낼때, Cookie라는 헤더에 같이 전송된다.
- 서버에서는 이 헤더를 읽어서 유저를 식별하는 등 필요한 구현을 할 수 있다.
![image](https://github.com/user-attachments/assets/5d53002b-db79-491e-af68-19702581bd48)
- 쿠키는 이렇게 동작하기 때문에 주로 서버에서 사용자를 식별하기 위한 수단으로 사용되어 왔다.
- 애초에 쿠키가 만들어진 목적 자체가 이런 일을 하는 것이기도 한다.
- Set-Cookie 헤더로 세션 ID를 넣어둔 뒤에, 이 후 요청부터 전송될 Cookie 헤더의 세션 ID를 읽어 어떤 사용자가 보낸 요청인지 판단하는 식이다.
## 쿠키에 대한 `Domain` 설정
- 쿠키가 유효한 사이트를 명시하기 위해 쿠키에 도메인을 설정할 수 있다.
![image](https://github.com/user-attachments/assets/f63cab06-2f21-4a84-bcd5-49840d58d927)
- 이렇게 도메인이 설정된 쿠키는 해당 도메인에서만 유효한 쿠키가 된다.
- 위에서 normal 쿠키는 localhost를 대상으로 쿠키가 설정되었기 때문에, localhost를 대상으로 한 요청에만 normal 쿠키가 전송된다.
- 쿠키에 별도로 명시된 도메인이 없다면 기본값으로 쿠키를 보낸 서버의 도메인으로 설정된다.
## 퍼스트 파티 쿠키와 서드 파티 쿠키
- 그리고 이렇게 설정된 도메인을 기준으로 퍼스트 파티 쿠키(First-party cookies)와 서드 파티 쿠키(Third-party cookies)가 나뉘어 진다.
- 우리는 `gijoeng.com`에 접속한 상태이다. 만약 `gijoeng.com`에서 `example.com`이 제공하는 이미지인 `example.com/image.png`를 사용하고 있다고 가정해보자
- 이 경우 사용자는 seob.dev에 접속해 있지만 브라우저에서는 example.com/image.png로 요청을 보낼 것 이다.
- 아래와 같은 HTML 코드로 나타낼 수 있다.
```html
<html>
  <head>
    <title>gijoeng.com</title>
    <meta property="og:url" content="https://seob.dev/" />
  </head>
  <body>
    <img src="https://example.com/image.png" />
  </body>
</html>
```
- 이 때 사용자가 example.com에 대한 쿠키를 가지고 있다면, 해당 쿠키가 example.com을 운영하는 서버로 같이 전송된다.
- 이 때 전송되는 쿠키를 서드 파티 쿠키라고 부른다. 그러니까, 서드 파티 쿠키는 사용자가 접속한 페이지와 다른 도메인으로 전송하는 쿠키를 말한다.
- Referer 헤더와 쿠키에 설정된 도메인이 다른 쿠키라고도 말할 수 있다.
- 그렇기 때문에 사용자가 `gijoeng.com`에 걸려있는 `example.com` 링크를 클릭한 경우에 전송되는 쿠키도 서드 파티 쿠키로 취급된다. 이 때 Referer는 `gijoeng.com`이기 떼문이다.
```html
<html>
  <head>
    <title>gijoeng.com</title>
    <meta property="og:url" content="https://seob.dev/" />
  </head>
  <body>
    <!-- 아래 링크를 클릭한 경우에 전송되는 쿠키들은 서드 파티 쿠키로 취급된다. -->
    <a href="https://example.com/">링크</a>
  </body>
</html>
```
- 퍼스트 파티 쿠키는 반대로 이해하면 간단하다.
- 퍼스트 파티 쿠키는 사용자가 접속한 페이지와 같은 도메인으로 전송되는 쿠키를 말한다.
- 같은 쿠키라도 사용자가 접속한 페이지에 따라 퍼스트 파티 쿠키로도 부를 수 있고, 서드 파티 쿠키로도 부를 수 있다.
- 앞서 말한 예제에서 `example.com`에 설정된 쿠키는 사용자가 `gijoeng.com`에 접속해 있을 때는 서드 파티 쿠키였지만, `example.com`에 접속해 있을때는 퍼스트 파티 쿠키이다.
