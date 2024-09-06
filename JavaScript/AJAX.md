# AJAX (Asynchronous Javascript And XML)
- Ajax는 웹 페이지 전체를 다시 로딩하지 않고도, 웹 페이지의 일부분만을 갱신할 수 있게 해준다.
- Ajax를 이용하면 백그라운드 영역에서 서버와 통신하여, 그 결과를 웹 페이지의 일부분에만 표시할 수 있다.
      
Ajax를 통한 웹 브라우저와 웹 서버 간의 통신 절차는 다음과 같다.      
1. 사용자에 의한 요청 이벤트가 발생
2. 요청 이벤트가 발생하면 이벤트 핸들러에 의해 자바스크립트가 호출
3. 자바스크립트는 XMLHttpRequest 객체를 사용하여 서버로 요청을 보냄
4. 서버는 전달받은 XMLHttpRequest 객체를 가지고 요청을 처리
5. 서버는 처리한 결과를 HTML, XML 또는 JSON 형태의 응답 데이터를 생성 웹 브라우저에 전달
6. 이때 전달되는 응답은 새로운 페이지를 전부 보내는 것이 아니라 필요한 데이터만을 전달한다.
7. 서버로부터 전달받은 데이터를 가지고 웹 페이지의 일부분만을 갱신하는 자바스크립트를 호출. 결과적으로 웹 페이지의 일부분만이 다시 로딩되어 표시된다.
## XMLHttpRequest 객체
XMLHttpRequest 객체는 **웹 브라우저가 서버와 데이터를 교환**할 때 사용된다. 웹 브라우저가 백그라운드에서 계속해서 서버와 통신할 수 있는 것은 바로 이 객체를 사용하기 때문이다.
```javascript
// 1. XMLHttpRequest객체 생성
var httpRequest = new XMLHttpRequest(); 

// 2. onreadystatechange 등록
httpRequest.onreadystatechange = function() {
	// XMLXttpRequest 객체의 현재 상태와 서버 상의 문서 존재 유무를 확인
    if (httpRequest.readyState == XMLHttpRequest.DONE && httpRequest.status == 200 ) {
    	console.log(httpRequest.responseText); // 서버에 요청하여 응답으로 받은 데이터를 문자열로 반환
    }
};

// 3. GET 방식으로 요청을 보내면서 데이터를 동시에 전달함
httpRequest.open("GET", "서버URL", true);
httpRequest.send();
```
