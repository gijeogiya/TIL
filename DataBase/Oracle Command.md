# Oracle Command
1.계정 관련1.1.계정 확인
``
SQL> SHOW USER;
USER은 "SYS"입니다.
```
- 지금 내가 사용한 계정이 뭔지 보여준다.

1.2.모든 계정을 확인
```
SQL>SELECT * FROM all_users;
```
1.3.SYS 계정으로 들어가기
```
SQL>SYS as sysdba
비밀번호 입력 : (그냥 엔터)비밀번호가 필요없는 SYS 계정이다.
```
- 만약 DB가 여러개라서 다른 DB의 SYS 계정으로 접속하려고 하면 @다른D없다고 나온다.
