# Spring Security의 개념
## 배경
- 기존 로그인 기능이 포함된 백엔드 서버를 만들때는, 회원인 경우 CRUD가 가능하도록 JWT를 활용하여 인증/인가를 구현함
- 로그인에 성공하면, 성공한 사용자의 정보와 JWT를 활용하여 토큰을 발급하고 Header에 토큰을 추가해서 Client에게 반환
- Client는 CRUD 할때, Request Header에 토큰을 넣어 요청을 보내고 Service에서 토큰을 검증하고, 토큰으로부터 사용자 정보를 가져와 회원DB에 사용자가 있는지 찾는 과정을 반복함
- 그런데 서비스에 있는 CRUD 메서드는 CRUD 뿐만 아니라 인증/인가와 관련한 로직(토큰 검정과 회원DB 조회)을 함께 수행하고 있음
- 인증/인가 관련 코드가 메서드마다 반복되고 있으며, 하나의 메서드에서 두 개 이상의 로직을 구현하고 있어서 객체지향과 거리가 있음
- 인증/인가 부분을 따로 처리할 수 있는 방법이 없을까?라는 물음에서 Spring Security 프레임워크를 활용하게 됨

## Spring Security란?
- Spring 기반의 어플리케이션 보안(인증, 권한, 인가 등)을 담당하는 Spring 하위 프레임워크
- 스프링 서버에 필요한 인증, 인가를 위해 많은 기능을 제공

## Spring Security 주요 컴포넌트
- Filter
  - 톰캣과 같은 웹 컨테이너에서 관리되는 서블릿의 기술
  - Client 요청이 전달되기 전후의 URL 패턴에 맞는 요청에 필터링을 해줌
  - Spring Security는 요청이 들어오면 Filter를 Chain 형태로 묶어놓은 형태인 ServletFilterChain을 자동으로 구성한 후 거치게 함
- SecurityFilterChain
  - Spring의 보안 Filter를 결정하는데 사용되는 Filter
  - Session, JWT 등 인증방식을 사용할 때 필요한 설정을 서비스 로직 구현으로부터 분리할 수 있는 환경을 제공
  - SecurityFilterChain에는 여러 개의 Security Filter들이 있는데, `UsernamePasswordAuthenticationFilter`만 살펴보자
![image](https://github.com/gijeogiya/TIL/assets/97646078/78af3740-ab77-439a-9a36-1429f47c1cb6)
- UsernamePasswordAuthenticationFilter
  - Form Login 기반에서 username과 password를 확인하여 인증
  - 인증이 필요한 URL 요청이 들어왔을 때 인증이 되지 않았다면 로그인페이지를 반환
- SecurityContextHolder
![image](https://github.com/gijeogiya/TIL/assets/97646078/cd524921-edec-43d7-ab85-d08dfdfd35da)
  - `SecurityContextHolder` : Spring Security로 인증한 사용자의 상세 정보를 저장
  - `SecurityContext` : `SecurityContextHolder`로 접근할 수 있으며, `Authentication` 객체를 가짐
- Authentication
  - 현재 인증된 사용자를 나타내며, `SecurityContext`에서 가져올 수 있음
  - `principal` : 사용자를 식별. username/password 방식으로 인증할 때 보통 UserDetails 인스턴스
  - `credentials` : 주로 비밀번호 정보. 대부분 사용자 인증에 사용한 다음 비움
  - `authorities` : 사용자에게 부여한 권한을 `GrantedAuthority`로 추상화하여 사용
- UserDetailsService
  - username/password 인증방식을 사용할 때, 사용자를 조회하고 검증한 후 UserDetails를 반환
  - 커스텀하여 Bean으로 등록 후 사용 가능
- UserDetails
  - 검증된 UserDetails는 `UsernamePasswordAuthenticationToken` 타입의 `Authentication`을 만들 때 사용 됨
  - 이 인증 객체는 `SecurityContextHolder`에 세팅
  - 커스텀하여 사용 가능
