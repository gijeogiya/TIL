# Spring MVC의 구조
## 도식도
![image](https://github.com/user-attachments/assets/03379ba9-1e8b-4ff9-8530-f8c4e04c4300)
## 기능
1. 클라이언트가 서버에 요청을 하면, Front Controller인 DispatcherServlet 클래스가 요청을 받는다.
2. DispatcherServlet은 프로젝트 파일 내의 servlet-context.xml 파일의 @Controller 인자를 통해 등록한 요청 위임 컨트롤러를 찾아 매핑(mapping)된 컨트롤러가 존재하면 @RequestMapping을 통해 요청을 처리할 메소드로 이동한다.
3. 컨트롤러는 해당 요청을 처리한 Service(서비스)를 받아 비즈니스 로직을 서비스에게 위임한다.
4. Service는 요청에 필요한 작업을 수행하고, 요청에 대해 DB에 접근해야 한다면 DAO에 요청하여 처리를 위임한다.
5. DAO는 DB 정보를 DTO를 통해 받아 서비스에게 전달한다.
6. 서비스는 전달받은 데이터를 컨트롤러에게 전달한다.
7. 컨트롤러는 Model(모델) 객체에게 요청에 맞는 View 정보를 담아 DispatcherServlet에게 전송한다.
8. DispatcherServlet은 ViewResolver에게 전달받은 View 정보를 전달한다.
9. ViewResolver는 응답할 View에 대한 JSP를 찾아 DispatcherServlet에게 전달한다.
10. DispatcherServlet은 응답할 뷰의 Render를 지시하고 뷰는 로직을 처리한다.
11. DispatcherServlet은 클라이언트에게 Rending된 뷰를 응답하며 요청을 마친다.
