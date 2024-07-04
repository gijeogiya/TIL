# Spring 트랜잭션 관리(Spring Transaction Managing)
Spring(스프링)에서 트랜잭션(Transaction)을 관리하는 방법은 크게 서로 대비되는 2가지 방법으로 나눌 수 있다.
## 프로그램에 의한(Programmatic) 트랜잭션 관리
- 프로그램 코드에 의한 트랜잭션 관리
```java
@Autowired
private PlatformTransactionManager transactionManager;

public void operateSome() {
    TransactionStatus status = transactionManager.getTransaction(new DefaultTransactionDefinition());
    try {
    } catch (RuntimeException e) {
        transactionManager.rollback(status);
        throw e;
    } finally {
        if (status.isRollbackOnly()) {
            transactionManager.rollback(status);
        } else {
            transactionManager.commit(status);
        }
    }
}
```
