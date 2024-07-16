# Transaction Isolation(트랜잭션과 격리성)
- DB는 트랜잭션 단위로 처리된다.
- 유명한 **All Or Nothing**이 DB의 트랜잭션에서 나온 이야기이다.
- DB를 이용할 때는 트랜잭션과 격리성(Isolation)에 대해서 잘 알아야한다.
## 트랜잭션(Transaction)
### 예시
- 로직중에 DB table에 정보를 insert하는 로직이 있다.
- Table은 정규화 되어있으며 A, B, C 테이블에 차례대로 테이터를 Insert한다고 하려고 한다.
- 테이블이 쪼개져 있으므로 테이블간의 데이터 정합성을 유지하는게 중요하다.
- 만약 A, B에는 Insert하고 C에 Insert 하기전 서버가 에러 또는 특정 작업에 의해 정상적으로 처리하지 못하는 상황이 되었다고 하자.
- 그렇다면 결과적으로 이 데이터는 믿을 수 없는 데이터가 된다.
- 이를 해결하기 위한 방법으로 DB는 **All Or Nothing 전략**을 취한다.
- 즉, A, B, C에 정상적으로 Insert하거나 아무곳도 Insert하지 않는 것이다.
- DB에서는 이 전략을 취하기 위해 트랜잭션이라는 단위를 사용한다.
- 트랜잭션 단위는 나누어지지 않는 최소한의 단위라고 정의한다.
- 위 로직에 트랜잭션이 적용되면 오류가 났다면 A, B에 ㅑnsert한 것을 Rollback함으로써 Nothing으로 전략을 취한다.
### 트랜잭션(Transaction)
트랜잭션은 4가지의 특징을 가진다. 이를 앞글자만따서 **ACID**라고 부른다.
#### 원자성(Atomicity)
- 트랜잭션은 더 이상 분해가 불가능한 업무의 최소단위이므로, 전부 처리되거나 아예 하나도 처리되지 않아야 한다.
#### 일관성(Consistency)
- 일관된 상태의 데이터베이스에서 하나의 트랜잭션을 성공적으로 완료하고 나면 그 데이터베이스는 여전히 일관된 상태여야 한다.
- 트랜잭션 실행의 결과로 데이터베이스 상태가 모순되지 않아야 한다.
#### 격리성(Isolation)
- 실행 중인 트랜잭션의 중간결과를 다른 트랜잭션이 접근할 수 없다.
#### 영속성(Durability)
- 트랜잭션이 일단 그 실행을 성공적으로 완료하면 그 결과는 데이터베이스에 영속적으로 저장된다.
## 트랜잭션 격리성(Transaction Isolation)
- 격리성은 "실행 중인 트랜잭션의 중간결과를 다른 트랜잭션이 접근할 수 없다."라는 정의를 가지고 있다.
- 막연하게 접근할 수 없다라기 보다는 일반적으로 접근 레벨이 있으며 DB에 따라 설정이 가능하다.
- 이런 격리성은 강하게 처리할 수 있으며 반대로 약하게 처리할 수도 있다.
### 격리성으로 인해 나타날 수 있는 문제점
격리성으로 인해 나타날 수 있는 문제점은 일반적으로 Dirty Read, Non-Repeatable Read, Phantom Read 3가지라고 이다.
#### Dirty Read
- Dirty Read는 다른 트랜잭션에 의해 수정됐지만 아직 커밋되지 않은 데이터를 읽는 것을 말한다.
![Dirty Read](https://github.com/user-attachments/assets/5e84e6e0-1d15-45dc-88a9-dede1750f577)
- Transaction_1이 정상처리되지 않고 Rollback될 수 있다. 이럴 경우 그 값을 이미 읽은 Transaction_2는 잘못된 값을 가지고 본인의 로직을 처리하는 상태에 놓이게 된다.
#### Non-Repeatable Read
Non-Repeatable Read는 한 트랜잭션 내에서 같은 Key를 가진 Row를 두 번 읽었는데 그 사이에 값이 변경되거나 삭제되어 결과가 다르게 나타나는 현상을 말한다.
![Non-Repeatable Read](https://github.com/user-attachments/assets/74856727-605e-4678-9036-cc5b0180dcc3)
#### Phantom Read
- 한 트랜잭션 내에서 같은 쿼리를 두 번 수행했는데, 첫 번째 쿼리에서 없던 유령(Phantom) 레코드가 두 번째 쿼리에서 나타나는 현상을 말한다.
![Phantom Read](https://github.com/user-attachments/assets/c07917d5-0953-4fc6-998c-8e4318d9717d)
- Phantom Read와 Non-Repeatuable Read를 햇갈릴 수 있다.
- Non-Repeatable Read는 1개의 Row의 데이터의 값이 변경되는 것이며 Phanton Read는 다건을 요청하는 것에 대해서 데이터의 값이 변경되는 것이다.
### 지정할 수 있는 격리성 수준
아래의 4개의 격리수준은 ANSI/ISO SQL 표준(SQL92)에서 정의한 내용이다.
#### Read Uncommitted
- 트랜잭션에서 처리 중인 아직 커밋되지 않은 데이터를 다른 트랜잭션이 읽는 것을 허용한다.
- 해당 수준에서는 Dirty Read, Non-Repeatable Read, Phantom Read가 일어날 수 있다.
- 이 설정은 정합성에 문제가 있기 때문에 권장하는 설정은 아니다.
#### Read Committed
- 트랜잭션이 커밋되어 확정된 데이터만 다른 트랜잭션이 읽도록 허용한다.
- 따라서 Dirty Read의 발생가능성을 막는다.
- 커밋 되지 않은 데이터에 대해서는 실제 DB 데이터가 아닌 Undo 로그에 있는 이전 데이터를 가져오는 것이다.
- 하지만 Non-Repeatable Read와 Phanton Read에 대해서는 발생 가능성이 있다.
#### Repeatable Read
- 트랜잭션내에서 삭제, 변경에 대해서 Undo 로그에 넣어두고 앞서 발생한 트랜잭션에 대해서는 실제 데이터가 아닌 Undo 로그에 있는 백업데이터를 읽게 한다.
- 이렇게 함으로써 트랜잭션 중 값의 변경에 대해서 일정한 값으로 처리할 수 있다.
- 이렇게하면 삭제와 수정에 대해서 트랜잭션내에서 불일치를 가져오던 Non-Reapeatable Read를 해소할 수 있다.
- Multiversion Concurrency Control
#### Serializable Read
- 트랜잭션 내에서 쿼리를 두 번 이상 수행할 때, 첫 번째 쿼리에 있던 레코드가 사라지거나 값이 바뀌지 않음은 물론 새로운 레코드가 나타나지도 않도록 하는 설정이다.
