# Oracle Sequence
- "testSeq"를 생성했다는 가정을 하자
```oracle
-- 해당 시퀀스의 값을 증가시키고 싶다면
testSeq.NEXTVAL
-- 현재 시퀀스를 알고 싶다면
testSeq.CURRVAL
```
- 위와같이 사용하면 된다.
- 다만 시퀀스를 사용할때 주의해야할 점이 있는데
## NEXTVAL 및 CURRVAL을 사용할 수 있는 경우
 - 서브쿼리가 아닌 SELECT문
 - INSERT문의 SELECT절
 - INSERT문의 VALUE절
 - UPDATE문의 SET절
 
## NEXTVAL 및 CURRVAL을 사용할 수 없는 경우
 - VIEW의 SELECT절
 - DISTINCT 키워드가 있는 SELECT문
 - GROUP BY, HAVING, ORDER BY절이 있는 SELECT문
 - SELECT, DELETE, UPDATE의 서브쿼리
 - CREATE TABLE, ALTER TABLE 명령의 DEFAULT값

## 기본적인 사용방법
```oracle 
-- 해당 시퀀스의 다음값
SELECT testSeq.NEXTVAL FROM DUAL; 
 
-- 해당 시퀀스의 현재값
SELECT testSeq.CURRVAL FROM DUAL; 
 
--INSERT에서의 시퀀스 다음값
INSERT INTO oracleStudy VALUES(testSeq.NEXTVAL, 'studyName' , 'class' , A);
```
- *여기서 주의할점은 SELECT 하는 조회에서도 NEXTVAL를 썼을경우 시퀀스자체의 값을 실제로 증가시키기 때문에 당황하지말자.

## 시퀀스(Sequence) 초기화 방법
- 추가적으로 하는김에 시퀀스값을 초기화 하는 방법에 대해 알아보자.
- 우선 흔하게 인터넷을 통해 배울수 있는 방법은 아래와 같다.
```oracle
--시퀀스의 현재값 확인
SELECT LAST_NUMBER FROM USER_SEQUENCES  WHERE SEQUENCE_NAME = 'TESTSEQ';
 
--시퀀스의 증가값 변동 (현재값이 3일경우 -3으로 처리)
ALTER SEQUENCE testSeq INCREMENT BY -3;
 
--다음값으로 증가값만큼의 처리
SELECT testSeq.NEXTVAL FROM DUAL; 

--현재값을 확인해본다
SELECT testSeq.CURRVAL FROM DUAL; 
 
--시퀀스의 증가값 변동 (원상복구)
ALTER SEQUENCE testSeq INCREMENT BY 1;
```

- 이런식으로 되어있는데 직접 해보게되면 LAST_NUMBER를 조회할때 간혹 이상하게 나오는 경우가있다.
- 그 이유는 시퀀스 설정에 CACHE를 설정해줬다거나 아무설정을 해주지 않았을때 기본 DEFAULT값이 20이 들어갔을 경우다. (20만큼 미리 오라클 내부에서 NEXTVAL이 된 상태로 존재하기때문에 LAST_NUMBER를 했을경우 그 값이 나오는 것이다.)
- 그래서 저 위의 방법은 NOCACHE를 설정해주었거나 다른 DB에서 시퀀스를 초기화할때 사용하면 좋다.
- 아주 간단하게 1. 현재 값을 체크하고
```oracle
SELECT testSeq.CURRVAL FROM DUAL;
```
- 만약 현재값이 3일 경우 INCREMENT BY를 -2만큼 해준다음 NEXTVAL 처리하고 다시 원상복구 시켜주면 초기화가 완료된다.
