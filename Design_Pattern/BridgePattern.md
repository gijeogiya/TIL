# Bridge Pattern
## Bridge Pattern이란?
- 추상적인 것과 구체적인 것을 분맇여 연결하는 패턴
- 하나의 계층 구조일 떄 보다 각기 나누었을 때 독립적인 계층 구조로 발전 시킬 수 있다.
![image](https://github.com/gijeogiya/TIL/assets/97646078/5cc46e8e-eac1-4f0f-89e6-d7d88ea52cb7)
![image](https://github.com/gijeogiya/TIL/assets/97646078/f31ce41a-e9dc-434c-be85-534564b70efd)
## 장단점
### 장점
- 추상적인 코드를 구체적인 코드 변경 없이도 독립적으로 확장할 수 있다.
- 추상적인 코드과 구체적인 코드를 분리하여 수 있다.
### 단점
- 계층 구조가 늘어나 복잡도가 증가할 수 있다.
## 실무에서 어떻게 쓰이나?
- Java
  - JDBC API, DriverManger와 Driver
  - SLF4J, 로깅 퍼사드와 로거
- Spring
  - Portable Service Abstraction
