# NVL
## 기능
- Oracle의 NVL 함수는 널 처리 함수로 사용된다.
- 데이터 값이 null 값일 때 임의 설정값으로 처리하는 데 사용된다.
- NVL 함수의 구문은 NVL(대상데이터, NULL일때 데이터)이다.
- 값이 null인 경우 두 번째 인자로 지정한 값으로 대체된다.
- 예를 들어, NVL 함수를 사용하여 salary가 null인 행의 급여를 0으로 처리할 수 있다.
- NVL 함수는 SELECT 문에서 사용되어 NULL 값이 있는 열을 원하는 값으로 대체할 수 있다.
- 예를 들어, DEPT_CODE 열과 MGR_EMP_NO 열을 선택하면서, MGR_EMP_NO가 NULL인 경우 0으로 대체하는 예제가 있다.
- 이 외에도 NVL2, NULLIF, COALESCE 같은 함수들이 있으며, 이들은 각각 다른 조건에 따라 값을 대체하거나 비교하는 데 사용된다.
## 사용에 있어 리스크
- 대상데이터의 값이 NULL인 경우가 너무 많은 경우 값을 바꾸는데 소요되는 시간이 크다.
- 두 개 이상의 데이터를 사용하는 경우에 인텍스를 타지 않아서 성능이 하락한다.
