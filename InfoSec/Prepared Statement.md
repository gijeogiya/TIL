# Prepared Statement
## 개요
- SQL Injection 취약점에 대한 대응방안으로 Prepared Statement와 바인딩변수를 이용하도록 권고하고 있다. Prepared Statement를 쓰면 SQL Injection 공격이 불가능할 수 밖에 없는 내부 작동 원리를 알아보자.
## SELECT 문 실행 과정
- 우리가 Web상에서 입력한 쿼리는 DBMS 내부적으로 4가지 과정(parse, bind, excute, fetch)를 거처 결과를 출력한다.
- 특히 쿼리의 문법을 검사하기 위해서는 parse 과정을 거치게 되는데 입력한 쿼리의 결과를 아래 그림과 같이 파싱하여 트리를 생성한다.
![SELECT문 실행 과정](https://github.com/user-attachments/assets/7cb9caf6-6315-408b-bf6d-d9e98e974200)
![SELECT문 파싱 트리](https://github.com/user-attachments/assets/007a5ae8-b8be-4f7e-9fbb-2f43c86c8dd5)
## Statement와 Prepared Statement의 차이(파싱과 바인딩)
- 일반적인 Statement를 사용하여 SELECT 쿼리를 입력했을 때에는 매번 parse부터 fetch까지 모든 과정을 수행한다.
- Prepared Statement를 사용하는 경우에는 효율을 높이기 위해 parse 과정을 최초 1번만 수행하고 이후에는 생략할 수 있다.
- parse 과정을 모두 거친 후에 생성된 결과는 메모리 어딘가에 저장 해두고 필요할 때마다 사용한다.
- 반복적으로 트리를 사용하기 위해서 자주 변경되는 부분을 변수로 선언해 두고, 매번 다른 값을 대입(바인딩)하여 사용한다.​
### 바인딩 사용 예시
전체 학교 학생이 1000명인 학교의 평균점수와 영어점수를 조회하려고 하면, 같은 테이블의 칼럼을 조회하고 학번과 이름만 다른 실행계획이 1000개 생길 것이다. 학번과 이름을 바인드 변수로 지정하면 실행계획은 최초로 1번만 생성하고 1000번 반복하면 실행계획의 생성 시간을 절약할 수 있다. 이렇게 실행계획을 줄이기 위해 다른변수나 값은 넣는 직업을 바인드라고 한다.
- 바인딩 데이터는 SQL 문법이 아닌 내부의 인터프리터나 컴파일 언어로 처리하기 때문에 문법적인 의미를 가질 수 없다. 따라서 바인딩 변수에 SQL공격 쿼리를 입력할지라도 의미있는 쿼리로 동작하지 않는다.​
- Prepared Statement에서 바인딩 변수를 사용하였을 때, 쿼리의 문법 처리과정이 미리 선 수행되기 때문에 바인딩 데이터는 SQL 문법적인 의미를 가질 수 없다. 따라서 Prepared Statement를 사용하면 SQL Injection 공격에 안전하게 구현할 수 있다.
