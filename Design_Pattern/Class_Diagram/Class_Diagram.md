# Class Diagram

클래스 다이어그램



## 기호와 의미



![Screen Shot 2022-03-29 at 6.32.52 PM](C:\Users\msg01\Downloads\Screen Shot 2022-03-29 at 6.32.52 PM.png)

![Screen Shot 2022-03-29 at 6.33.04 PM](C:\Users\msg01\Downloads\Screen Shot 2022-03-29 at 6.33.04 PM.png)

### 상자

- 상자는 클래스를 의미
- 프로토콜이면 상단에 <<protocol>> (interface와 동일한 개념)
- 상자의 최상단은 class의 이름
- 상자의 두번째 박스에는 property
- 상자의 세번째 박스에는 method



### 화살표

- Open arrowhead: 상속을 의미. "inherits from", "is a"로 읽으면 됨.
- Plain arrowhead: property를 의미. "has a"로 읽으면 됨. 여러개를 갖는 경우 1...*를 화살표 옆에 표시. (ex. Address를 가질 경우 Address 내부에 국가, 시도, 도로명 주소, 우편번호, 유선번호, 동, 호, 층 등 다양한 요소를 한번에 가지는 property)
- 점선의 Open arrowhead: Protocol 구현을 의미. "implements" or "conforms to"로 읽으면 됨
- 점선의 Plain arrowhead: 의존성, 사용을 의미. "uses", "delegates to" 등으로 읽을 수 있음. 1) weak property or delegate. 2) 함수의 파라미터 3) 사라지는 커플링이나 콜백



### 참고

[draw.io](https://draw.io)



