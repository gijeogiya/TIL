# JavaScript와 Ajax
## Contents
### Part 01: Ajax 웹 어플리케이션이 제시하는 새로운 제안
1. Ajax란 무엇인가?
   1. Ajax란 용어의 탄생
   2. Ajax를 이루는 구성 요소
   3. Ajax의 비동기적 통신의 구조 (데이터의 흐름)
2. Ajax를 사용한 웹 페이지 작성
   1. XMLHttpRequest 객채의 개요 및 작성 방법
   2. 대표적인 Ajax 라이브러리
   3. 기업에서 공개하고 있는 웹 어플리케이션 API
### Part 02: Ajax를 위한 자바스크립트
1. 자바스크립트에 대한 기본 설명
   1. 자바스크립트란 무엇인가?
   2. 자바스크립트의 버전
   3. 자바스크립트의 기술 방법
2. 문장의 구조
3. 데이터 타입
   1. 기본 데이터 타입(primitive type)
      1. 숫자 타입
      2. 문자열 타입
      3. 불리언(boolean) 타입
      4. null 타입
   2. 레퍼런스 타입(reference type)
      1. 객체 참조
      2. 배열(Array)
4. 변수
5. 연산자
   1. 산술 연산자
   2. 비교 연산자
   3. 논리 연산자
   4. 대입 연산자
   5. 문자열 결합 연산자
   6. 비트 연산자
   7. 괄호 연산자 및 객체 참조 연산자
   8. new 연산자
   9. this 연산자
   10. 조건 연산자
   11. typeof() 연산자
   12. void() 연산자
   13. delete 연산자
   14. instanceof 연산자
   15. in 연산자
6. 함수(Function)
   1. 사용자 정의 함수(User defined function)
   2. 내장 함수
      1. alert() 함수
      2. confirm() 함수
      3. prompt() 함수
      4. eval() 함수
      5. escape() 함수와 unescape() 함수
      6. inNaN() 함수
      7. isFinite() 함수
      8. parseInt() 함수와 parseFloat() 함수
7. 선언문과 제어문
   1. 선언문과 제어문의 기본 사용 방법
   2. var문
   3. function문
   4. with문
   5. if문
   6. else if문
   7. switch문
   8. for문
   9. for in문
   10. while문
   11. do while문
   12. break문
   13. continue문
   14. 레이블문
   15. return문
   16. try-catch-finally문
   17. throw문
8. 이벤트와 이벤트 핸들러
   1. 이벤트
      1. Click 이벤트
      2. DblClick 이벤트
      3. DragDrop 이벤트
      4. KeyDown 이벤트
      5. KeyPress 이벤트
      6. KeyUp 이벤트
      7. MouseDown 이벤트
      8. MouseMove 이벤트
      9. MouseOut 이벤트
      10. MouseOver 이벤트
      11. MouseUp 이벤트
      12. Move 이벤트
      13. Resize 이벤트
   2. 이벤트 핸들러
      1. onAbort
      2. onBlur
      3. onChange
      4. onClick
      5. onError
      6. onFocus
      7. onLoad
      8. onMouseOut
      9. onMouseOver
      10. onReset
      11. onSelect
      12. onSubmit
      13. onUnload
9. 객체(Object)
   1. navigator 객체
   2. mimeType 객체
   3. plugin 객체
   4. screen 객체
   5. event 객체
   6. Window 객체
   7. Frame 객체
   8. document 객체
   9. History 객체
   10. Location 객체
   11. Link 객체
   12. Anchor 객체
   13. Form 객체
       1. 폼 객체의 속성들
       2. Button 객체
       3. Checkbox 객체
       4. FileUpload 객체
       5. Hidden 객체
       6. Password 객체
       7. Radio 객체
       8. Reset 객체
       9. Submit 객체
       10. Text 객체
       11. Select 객체
       12. Textarea 객체
   13. Area 객체
   14. Area 객체
   15. Image 객체
   16. Layer 객체
   17. Applet 객체
   18. embeds 배열(embeds array)
   19. Date 객체
   20. Math 객체
   21. String 객체
   22. Array 객체
   23. Function 객체
   24. Object 객체
   25. Boolean 객체
   26. Number 객체
   27. RegExp 객체
10. 객체 지향 자바스크립트
   1. prototype 프로퍼티 사용
   2. 자바스크립트에서 정보 은닉
11. prototype.js에 대해서
   1. prototype.js의 개요
      1. 왜 prototype.js가 필요한 것일까?
      2. prototype.js란 무엇인가?
   3. prototype.js의 주요 API
      1. 클래스의 정의
      2. prototype.js의 DOM API
### Part 03: Ajax를 위한 Dynamic HTML
1. DHTML(DynamicHTML)의 개요
   1. Dynamic HTML은 무엇인가?
   2. DOM과 자바스크립트
2. DOM의 주요 인터페이스 및 메소드와 프로퍼티의 사용
   1. 노드(Node)
   2. Domcument 인터페이스
   3. Element 인터페이스
   4. DOM에서 자주 사용되는 프로퍼티(속성)
      1. 엘리먼트.id
      2. 엘리먼트.class
      3. 엘리먼트.tagName
      4. 엘리먼트.length
      5. 엘리먼트.lang
      6. 엘리먼트.innerHTML
      7. 엘리먼트.outerHTML
      8. 엘리먼트.innerText
      9. 엘리먼트.outerText
   5. DOM에서 자주 사용되는 메소드
      1. document.getElementById(id 속성값)
      2. document.getElementByName(엘리먼트명)
      3. document.getElementByTagName(엘리먼트명)
      4. 엘리먼트.getAttribute(속성명)
      5. 엘리먼트.setAttribute(속성명)
      6. 엘리먼트.removeAttribute(속성명)
      7. 엘리먼트.getAttributeNode(속성 노드명)
      8. document.createElement(생성할 엘리먼트명)
3. CSS(Cascading Style Sheet)
   1. CSS의 개요
   2. CSS의 작성 위치
   3. CSS의 작성 규칙 및 사용 방법
   4. CSS의 속성과 속성값
      1. 색상과 배경(Colors and Backgrounds)지정
      2. 폰트(Fonts) 지정
      3. 텍스트(Text) 지정
      4. 테이블(Table) 지정
      5. 박스 모델(Box model)지정
   5. CSS에서의 가시성(visibility)와 위치(positioning)에 관련한 속성
      1. display 프로퍼티
      2. visibility 프로퍼티
      3. position 프로퍼티
      4. z-index 프로퍼티
4. DOM & CSS & HTML 활용 예제
   1. 선택한 항목에 대한 입력필드를 생성
   2. 버튼을 클릭해서 페이지의 스타일 변경
   3. 사용자의 선택에 의한 페이지 구조 변경
   4. 키보드에서 입력받아 페이지의 내용과 스타일 변경
   5. RICO 툴킷을 사용한 콘텐츠의 위치 이동
   6. 이벤트 발생시 팝업영역에 내용 표시
   7. 검색어 자동 완성 기능 구현
5. XMLHttpRequest(XHR) 객체를 사용한 서버와의 통신
   1. 서버에 요청보내기
      1. XMLHttpRequest(XHR) 객체를 사용하여 서버에 요청보내기
      2. HTTP 메소드
      3. GET 방식으로 요청보내기
      4. POST 방식으로 요청보내기
   2. 서버로 부터의 응답 결과 처리
      1. 응답 결과를 문자열로 처리
      2. 응답 결과를 XML로 처리
      3. 응답 결과를 JSON으로 처리
### Part 04: Ajax와 Javascript, DB를 연동한 실무 프로그래밍
1. 서버와 연도하는 Ajax 예제 프로그램
   1. 사용자의 선택에 따른 입력 폼 생성
   2. 온라인 설문지 작성
   3. 블로그 같은 느낌의 페이지의 구조 및 스타일 변경
2. 데이터베이스를 사용한 서버와 연동하는 예제 
