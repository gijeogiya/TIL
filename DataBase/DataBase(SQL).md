# DataBase

- 데이터베이스는 **체계화된 데이터의** 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
- 즉, **몇 개의 자료 파일을 조직적으로** 통합하여 **자료 항목의 중복을 없애고 자료를 구조화하여** 기억시켜 놓은 **자료의 집합체**

## 관계형 데이터베이스(RDB)

- Relational Database
- **키(key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 DB**
- 관계형 모델에 기반

### 스키마(schema)

- 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 **명세를 기술한** 것

### 테이블(Table)

- 열과 행으로 이루어진 데이터의 집합

#### 열(Column)

- 각 열에는 고유한 데이터 형식이 지정됨

#### 행(Row)

- 실제 데이터가 저장되는 형태

### 기본키(Primary Key)

- 각 행(레코드)의 고유 값
- 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용됨

## 관계형 데이터베이스 관리 시스템(RDBMS)

- Relational Database Management System
- **관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미**
- MySQL, SQLite, ORACLE, 등

## SQL

- Structured Query Language
- 관계형 데이터베이스 관리시스템의 **데이터 관리를** 위해 설계된 **특수 목적 프로그래밍 언어**
- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리



### Data Manipulation Language

- **INSERT**

  ```
  INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
  ```

- **SELECT**

  ```
  SELECT column1, column2, ... FROM table_name;
  ```

  - **LIMIT**

    ```
    SELECT column1, column2, ... FROM table_name LIMIT number OFFSET number;
    ```

    - 쿼리에서 반환되는 행 수를 제한
    - 특정 행부터 시작해서 조회하기 위해 **OFFSET** 키워드와 함께 사용하기도 함
    - OFFSET
      - 동일 오브젝트 안에서 오브젝트 처음부터 주어진 요소나 지점까지의 **변위차(위치 변화량)를** 나타내는 정수형

  - **WHERE**

    ```
    SELECT rowid, name FROM classmates WHERE address='서울';
    ```

    - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

  - **DISTINCT**

    ```
    SELECT DISTINCT column FROM table_name;
    ```

    - 조회 결과에서 중복 행을 제거
    - DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

- **UPDATE**

  ```
  UPDATE table_name SET col1=val1, col2=val2, ... WHERE condition;
  ```

  - 기존 행의 데이터를 수정
  - **SET** clause에서 테이블의 각 열에 대해 새로운 값을 설정

- **DELETE**

  ```
  DELETE FROM table_name WHERE condition;
  ```

  - 테이블에서 행을 제거

  - SQLite는

     

    기본적으로 id를

     

    재사용

    - AUTOINCREMENT : **SQLite가** 사용되지 않은 값이나 이전에 삭제된 값을 재사용하는 것을 방지

### Aggregate Functions

- **집계 함수**
- 값 집합에 대한 계산을 수행하고 단일 값을 반환
  - 여러 행으로부터 하나의 결과값을 반환하는 함수
- **SELECT** 구문에서만 사용됨
- Examples
  - 테이블 전체 행 수를 구하는 **COUNT(\*)**
  - age column 전체 평균 값을 구하는 **AVG(age)**
  - **MAX(), MIN(), SUM()**

### LIKE

```
SELECT * FROM users WHERE phone_number LIKE '02-%';
```

- 패턴 일치를 기반으로 데이터를 조회하는 방법

- SQLite는

   

  패턴 구성을 위한

   

  2개의 wildcards를

   

  제공

  - %: 0-N개 문자가 존재
  - _: 반드시 이 자리에 한 개의 문자가 존재

### ORDER BY

```
SELECT * FROM table_name ORDER BY column1, column2, ... DESC;
```

- 조회 결과 집합을 정렬
- **SELECT** 문에 추가하여 사용
- 정렬 순서
  - ASC: 오름차순 (*default*)
  - DESC: 내림차순

### GROUP BY

```
SELECT column1, aggreate_function(column2) FROM table_name GROUP BY col1, col2;
```

- 행 집합에서 요약 행 집합을 만듦
- **SELECT** 문의 *optional* 절
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
- 문장에 WHERE 절이 포함된 경우 **반드시 WHERE 절 뒤에 작성해야 함**

### ALTER TABLE

```
ALTER TABLE oldTableName RENAME TO newTableName;
ALTER TABLE table_name ADD COLUMN column_name datatype [NOT NULL DEFAULT value];
```

- 3가지 기능
  - table 이름 변경
  - 테이블에 새로운 column 추가
  - column 이름 수정