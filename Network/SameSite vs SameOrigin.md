# SameSite vs SameOrigin
> 웹 개발을 공부하다 보면 origin이 달라서 발생하는 CORS 관련 이슈를 접하는 일이 잦습니다. 이와 관련해서는 일전에 포스팅으로 한번 정리한 적도 있습니다. 그러나 최근 스터디에서 쿠키와 관련된 이야기가 나오면서 그렇다면 쿠키는 same origin일 때만 세팅할 수 있는가, 라는 질문이 나왔는데 MDN의 쿠키 세팅 설명에 따르면, 아무것도 세팅하지 않은 상태에선 동일한 호스트(서브도메인도 제외)만 허용한다. 이와 관련한 부분은 Domain 옵션인데, 이곳에 특정 호스트를 명시하게 되면 오히려 해당 호스트의 same-site를 모두 허용해줄 수 있기 때문에 더 제약이 없어진다.   
## Same Origin
- 오리진이 같다는 걸 이해하려면 오리진이 무엇인지 파악하면 쉽다.
- same site에 비해서 좀 더 엄격하다.
- 어떤 사이트의 url을 구성하는 것은 여러 가지가 있다.
- 오리진이 같다는 것은 url에서 scheme(protocol), host(domain), port가 동일하다는 것을 의미한다.
- scheme은 http, https 같은 프로토콜 명시 영역, host는 우리가 흔히 '주소'라고 부르는 사이트의 도메인(이름), port는 :(콜론) 뒤에 따라붙는 숫자이다.
- 도메인이 같더라도 포트가 다르면 다른 사이트인 경우다.
- 그리고 http의 기본 포트는 80, https의 기본 포트는 443으로 포트가 명시되지 않은 사이트는 앞에 적힌 scheme에 따라 80, 443 포트를 생략하여 적을 수 있는 것이다.
```
http://example.com/app1/index.html
http://example.com/app2/index.html
```
- 예를 들어 위의 두 url은 same origin이다.
- 포트 80은 생략되고 있고, 나머지 scheme, host가 동일하다.
```
http://example.com/app1
https://example.com/app2
```
- 그와 반대로 동일한 도메인명을 가지고 있지만 scheme이 다르기 때문에 위의 둘은 origin이 동일하지 않다.
- 참고로 cors와는 별개의 이슈지만, https 프론트와 api 통신을 하려면 서버 또한 https 대응이 되어야 한다.
```
http://example.com:3000/index.html
http://example.com:5000/index.html
```
- 이 둘도 포트 번호가 다르기 때문에 다른 origin이다.
## Same Site
- 반면 same site의 기준은 다르다.
- 서브도메인이 이 모든 혼동의 시작이었는데, 결론적으로 보자면 서브도메인은 오리진은 다르지만 same site이다.
![image](https://github.com/user-attachments/assets/a093ac76-befb-40d7-a90f-cae0927f6170)
- 보통 same stie라 하면, Top-Level-Domain(TLD), 즉 .com, .kr 같은 최상위 도메인과 그 바로 앞까지를 포함하는 부분이 두 개의 다른 url에 동일하게 보이는 경우를 의미한다.
```
https://my.example.com
https://your.example.com
```
- 이 둘은 오리진은 다르겠지만 (엄연히 도메인이 다릅니다) same-site로 볼 수 있습니다.
- 그래서 쿠키 세팅과 관련된 옵션에서 도메인 옵션을 example.com으로 설정해둔다면 서로 쿠키를 설정해줄 수 있다.
- 하지만 좀 더 엄격하게 본다면, 단순히 TLD와 그 앞까지만이 아니라 Public Suffix List에 명시된 기준을 참고하여 어느 범위까지 동일할 때 same site로 판단할지를 결정한다.
- 이런 리스트를 굳이 관리하게 된 이유는 .co.kr 같이 세 번째 자리부터 등록이 가능한 경우는 이미 kr앞에 co가 추가되어 있어서 same-site의 범위가 너무 넓어지고, 이렇게 되면 쿠키를 모든 co.kr사이트에 등록할 수 있게 되어버리기 때문이다.
## 마치며
- CORS가 SOP와 분리해서 생각할 수 없는 것처럼 same-site도 쿠키와 따로 이해하는 것이 무의미하다는 느낌을 많이 받았다.
- 결국 위에서 얘기한 same-site를 판별하는 Public Suffix List를 참조하는 로직도 쿠키 세팅을 고민하다가 나오게 된 개념이다.
