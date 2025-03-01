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
## 쿠키와 CSRF 문제
- 쿠키에 별도로 설정을 가하지 않는다면, 크롬을 제외한 브라우저들은 모든 HTTP 요청에 대해서 쿠키를 전송하게 된다.
- 그 요청에는 HTML 문서 요청, HTML 문서에 포함된 이미지 요청, XHR 혹은 Form을 이용한 HTTP 요청등 모든 요청이 포함된다.
- **CSRF(Cross Site Request Forgery)**는 이 문제를 노린 공격이다.
1. 공격대상 사이트는 쿠키로 사용자 인증을 수행함.
2. 피해자는 공격 대상 사이트에 이미 로그인 되어있어서 브라우저에 쿠키가 있는 상태.
3. 공격자는 피해자에게 그럴듯한 사이트 링크를 전송하고 누르게 함. (공격대상 사이트와 다른 도메인)
4. 링크를 누르면 HTML 문서가 열리는데, 이 문서는 공격 대상 사이트에 HTTP 요청을 보냄.
5. 이 요청에는 쿠키가 포함(서드 파티 쿠키)되어 있으므로 공격자가 유도한 동작을 실행할 수 있음.
- 바로 아래에서 이야기 할 SameSite는 이 문제를 해결하기 위해 탄생한 기술이다.
## `SameSite` 쿠키
- `SameSite` 쿠키는 앞서 언급한 서드 파티 쿠키의 보안적 문제를 해결하기 위해 만들어진 기술이다.
- 크로스 사이트(Cross-site)로 전송하는 요청의 경우 쿠키의 전송에 제한을 두도록 힌다.
- `SameSite` 쿠키의 정책으로 `None`, `Lax`, `Strict` 세 가지 종류를 선택할 수 있고, 각각 동작하는 방식이 다르다.
  - `None`: `SameSite` 가 탄생하기 전 쿠키와 동작하는 방식이 같다. `None`으로 설정된 쿠키의 경우 크로스 사이트 요청의 경우에도 항상 전송된다. 즉, 서드 파티 쿠키도 전송됩니다. 따라서, 보안적으로도 `SameSite` 적용을 하지 않은 쿠키와 마찬가지로 문제가 있는 방식이다.
  - `Strict`: 가장 보수적인 정책이다. `Strict`로 설정된 쿠키는 크로스 사이트 요청에는 항상 전송되지 않는다. 즉, 서드 파티 쿠키는 전송되지 않고, 퍼스트 파티 쿠키만 전송된다.
  - `Lax`: `Strict`에 비해 상대적으로 느슨한 정책이다. `Lax`로 설정된 경우, 대체로 서드 파티 쿠키는 전송되지 않지만, 몇 가지 예외적인 요청에는 전송된다.
### `Lax` 쿠키가 전송되는 경우
- The Chromium Projects의 SameSite 속성을 소개한 게시물을 보면 다음과 같이 Lax 정책을 설명한다.
> A cookie with "SameSite=Lax" will be sent with a same-site request, or a cross-site top-level navigation with a "safe" HTTP method.
- 그러니까 같은 웹 사이트일 때는 (당연히) 전송된다는 것이고, 이 외에는 Top Level Navigation(웹 페이지 이동)과, "안전한" HTTP 메서드 요청의 경우 전송된다는 것이다.
- Top Level Navigation에는 유저가 링크(`<a>`)를 클릭하거나, `window.location.replace` 등으로 인해 자동으로 이뤄지는 이동, 302 리다이렉트를 이용한 이동이 포함된다. 하지만 <iframe>이나 <img>를 문서에 삽입함으로서 발생하는 HTTP 요청은 "Navigation"이라고 할 수 없으니 `Lax` 쿠키가 전송되지 않고, `<iframe>` 안에서 페이지를 이동하는 경우는 "Top Level"이라고 할 수 없으므로 `Lax` 쿠키는 전송되지 않는다.
- 또한 "안전하지 않은" `POST`나 `DELETE` 같은 요청의 경우, `Lax` 쿠키는 전송되지 않는다. 하지만 `GET`처럼 서버의 서버의 상태를 바꾸지 않을 거라고 기대되는 요청에는 `Lax` 쿠키가 전송된다.
- 이 모든 내용은 서드 파티 쿠키에 한하는 것이고, 퍼스트 파티 쿠키는 `Lax`나 `Strict`여도 전송된다.
## 브라우저의 `SameSite` 구현
- 아마 적극적으로 SameSite 속성을 사용하고 있는 개발자는 많지 않을 거다.
- 우리가 SameSite에 주의를 기울여야 하는 이유는 브라우저들의 동작/정책 등이 변경되고 있기 때문이다.
### `Lax` by default
- 크롬은 SameSite를 가장 적극적으로 적용하고 있는 브라우저이다.
- 원래 SameSite를 명시하지 않은 쿠키는 SameSite가 None으로 동작했지만, 2020년 2월 4일 크롬 80 버전이 배포되면서 SameSite의 기본값이 Lax로 변경되었고, 이 변경사항은 운영되고 있는 웹 서비스들에게 많은 영향을 미쳤다.
- 특히 온라인 결제나 OAuth처럼 구현에 크로스 사이트 간의 페이지 전환이 필요한 경우 이러한 변경사항 때문에 원래 제공하던 기능이 제대로 동작하지 않은 경우도 있었다. 물론 시간이 꽤 지났기 때문에 현재 운영되는 서비스들은 대부분 대응되어 있을 거다.
- 나도 오늘 이런 히스토리를 몰라서 하루종일 삽질했다. (헤맨만큼 내땅이다. 이럴때 쓰는말 맞나???)
### `Secure` 필수 정책
- `SameSite` 속성으로 `None`을 사용하려면 반드시 해당 쿠키는 Secure 쿠키여야한다.
- `Secure` 쿠키는 HTTPS가 적용된(구간 암호화된) 요청에만 전송되는 쿠키이다.
- 크롬에서는 `SameSite=None`으로 `Set-Cookie`를 사용하면 다음과 같이 쿠키 자체가 제대로 설정되지 않는다.
![image](https://github.com/user-attachments/assets/fbb349ca-52c9-4c8b-a24f-e62b9018be55)
## 쿠키의 미래
- 크로미엄 블로그의 Building a more private web: A path towards making third party cookies obsolete라는 글에는 다음과 같은 내용이 있다.
> ... and we have developed the tools to mitigate workarounds, we plan to phase out support for third-party cookies in Chrome.
- 크롬에서는 장기적으로 서드 파티 쿠키에 대한 지원을 단계적으로 제거할 예정이라는 말이다. 결국 미래에는 모든 쿠키가 SameSite=Strict로 설정된 것처럼 동작하게 된다는 의미이다.
- 현재로서는 퍼스트 파티 쿠키가 서드 파티 쿠키의 역할을 모두 대체할 수 없는 상태이다. 가령 어떤 서비스가 gijeong.com와 gijeong.io 두 가지 도메인을 모두 사용해서 운영된다고 생각해보면, 당연히 브라우저는 이 두 도메인을 다른 도메인으로 인식할 것이고, 모든 서드 파티 쿠키가 전송되지 않는다면 이 두 도메인 사이를 왔다갔다 할 때마다 전송되지 않는 쿠키로 인해 문제가 생길 것이다.
- 구글은 이 문제를 해결하기 위해서 First-Party Sets라는 표준을 제안했다. First-Party Sets는 여러개의 도메인을 동일한 사이트로 다룰 수 있도록 만드는 기술이다. gijeong.com에서 "gijeong.io도 같은 서비스를 제공하고 있어!" 라고 브라우저한테 알려주면 브라우저는 이후에는 그 도메인을 같은 사이트로 관리하는 것이다. 하지만 아직 표준으로 합의되지 않았고 반대도 많은 만큼 어떻게 될 지는 모르겠다.
- 확실한 건 앞으로는 점점 더 쿠키를 사용하기 까다로워 질 거라는 사실이다. 지금부터 서드 파티 쿠키를 사용하지 못한다는 전제하에 서비스를 개발하는 게 좋을 것 같다.
