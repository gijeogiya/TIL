# Spring 트랜잭션 관리(Spring Transaction Management)
## 프로그램에 의한(Programmatic) 트랜잭션 관리
프로그램 코드에 의한 트랜잭션 관리
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
위의 코드와 같이 트랜잭션 매니저를 통해서 직접 트랜잭션 개시, 커밋, 롤백등을 수행하는 방법으로 소스코드에 직접기술하기 때문에 가독성을 떨어트리고 실수할 가능성도 높아지므로 많이 사용하는 방식은 아니지만, 내부구현을 외부에 노출하고 싶지 않은 경우에 사용할 수 있다.
## 선언적(Declarative) 트랜잭션 관리
선언적 트랜잭션 관리는 트랜잭션에 관한 코드를 비지니스 코드로 부터 분리해서 비침투적인 방법으로 기술하여 관리하는 방법을 의미이다.
### 어노테이션(Annotation)으로 트랜잭션 선언
```java
@Transactional
public class SomeService() {
    @Transactional
    public void operateSome() {
    }
}
```
@Transactional 어노테이션을 사용할 경우에는 프래그램을 사용할 때와같이 트랜잭션 매니저를 직접 지정하지 못하기 때문에 transactionManager 라는 속성을 통해서 사용할 트랜잭션 매니저를 지정할 수 있다.
### AOP 설정으로 트랜잭션 선언
```xml
<aop:config>
    <aop:pointcut id="serviceOperation"
          expression="execution(* service..*Service.*(..))"/>
    <aop:advisor pointcut-ref="serviceOperation" advice-ref="txAdvice"/>
</aop:config>

<tx:advice id="txAdvice">
    <tx:attributes>
        <tx:method name="*"/>
    </tx:attributes>
</tx:advice>
```
```java
@Bean
public TransactionInterceptor transactionInterceptor(PlatformTransactionManager transactionManager) {
    return new TransactionInterceptor(transactionManager, transactionAttributeSource());
}

@Bean
public NameMatchTransactionAttributeSource transactionAttributeSource() {
    NameMatchTransactionAttributeSource tas = new NameMatchTransactionAttributeSource();

    Map<String, AttributeSource> matches = new HashMap<>();
    matches.put("get*", new RuleBasedTransactionAttribute());
    return tas;
}

@Bean
public AspectJExpressionPointcutAdvisor transactionAdvisor(TransactionInterceptor advice) {
    AspectJExpressionPointcutAdvisor advisor = new AspectJExpressionPointcutAdvisor();
    advisor.setAdvice(advice);
    advisor.setExpression("execution(* service..*Service.*(..))");
    return advisor;
}
```
스프링에서 제공하는 설정방식인 어노테이션이나 혹은 AOP설정 이용하여 트랜잭션 관리를 수행할 수 있다. @Transactional 어노테이션 이외의 방식은 거의 사용되지 않으므로 할 수 있다.
## Spring 트랜잭션 속성
|속성|설명|
|----|----|
|propagation|트랜잭션 개시할지 등 전파행위에 관한 속성|
|isolation|트랜잭션 격리레벨에 관한 속성으로 기본값은 Default레벨이며 실제 사용하는 데이터베이스(JDBC) 등의 기본값을 따름|
|readOnly|트랜잭션을 읽기전용으로 지정하는 속성. 최적화 관점에서 지원되는 프로터티이므로 현재 트랜잭션 상태에따라 다르게 동작할 수 있음|
|timeout|트랜잭션의 타임아웃(초단위)을 지정하는 속성으로 지정하지 않을 경우 사용하는 트랜잭션 시스템의 타임아웃을 따름|
|rollbackFor|Checked 예외 발생시에 롤백을 수행할 예외를 지정하는 속성|
|rollbackForClassName|rollbackFor와 동일하지만 문자열로 클래스명을 지정하는 속성|
|noRollbackFor|Spring의 트랜잭션은 기본적으로 Runtime예외만 롤백처리를 수행하지만 Runtime예외중 특정 예외는 롤백을 수행하지 않아야 할 경우 사용하는 속성|
|noRollbackForClassName|noRollbackFor와 동일하지만 문자열로 클래스명을 지정하는 속성|
### 설정에시
```java
@Transactional(propagation = Propagation.REQUIRED, rollbackFor = Exception.class)
public class SomeService {

    @Transactional(propagation = Propagation.REQUIRES_NEW, isolation = Isolation.DEFAULT, timeout = 10)
    public void operateSome() {
    }
    //...
}
```
- 클래스 단위 혹은 메소드 단위로 지정할 수 있다.
- 메소드에 기술한 설정이 우선 적용되며 지정하지 않은 경우 클래스에 기술한 설정이 적용된다.
## 전파행위(Propagation Behavior)
전파행위(거동)는 트랜잭션을 개시할지 혹은 기존 트랜잭션을 이용할지 등 트랜잭션 경계(Transaction Boundary)를 설정할 때 이용하는 속성으로 가장 중요한 속성이라고 할 수 있다.
### 설정 가능한 전파행위 목록
|속성|설명|
|----|----|
|MANDATORY|트랜잭션이 존재할 경우 해당 트랜잭션을 이용하며 존재하지 않을 경우 예외발생|
|NESTED|트랜잭션이 존재할 경우 중첩된 트랜잭션을 개시하고 존재하지 않을 경우는 REQUIRED와 동일하게 동작|
|NEVER|트랜잭션이 존재할 경우 예외발생|
|NOT_SUPPORTED|트랜잭션이 존재할 경우 중단(Suspend)해서 트랜잭션을 이용하지 않음.|
|REQUIRED|트랜잭션이 존재하는 경우 해당 트랜잭션을 그대로 하며 개시된 트랜잭션이 없는 경우 트랜잭션 개시|
|REQUIRES_NEW|항상 신규트랜잭션을 개시함. 트랜잭션이 존재하는 경우 해당 트랜잭션을 중단하고 새로운 트랜잭션 개시|
|SUPPORTS|트랜잭션이 존재할 경우 해당 트랜잭션을 이용하고 존재하지 않을 경우는 트랜잭션을 이용하지 않음|
#### MANDATORY
트랜잭션이 개시된 것을 강제해야할 경우 사용하는 속성으로 데이터베이스의 락을 취득한다던지 시퀀셜한 번호를 생성하거나 하는등 단독으로 사용할 이유가 없는 경우에 해당 상황을 배제하기 위해 사용한다.
#### NESTED
중첩트랜잭션은 이미 트랜잭션이 시작되어있는 상태에서 트랜잭션 내부에 새로운 트랜잭션 경계를 설정하고자 할 때 사용하는 속성으로 JDBC의 Savepoint 기능을 이용한다.
Savepoint 기능이 JDBC 3.0이후부터 지원되는 영향인지 전파행위의 다른 속성들은 동일한 이름으로 EJB에 존재하지만 중첩 트랜잭션은 존재하지 않다.
중첩트랜잭션을 사용할만한 상황을 예를 들어보면 주문 트랜잭션 내부에서 포인트 적립을 처리하는 부분만 별도로 경계를 설정하고 해당 경계 내부의 처리에 실패하더라도 주문자체는 정상 처리시키고자 할 때 사용할 있다.
하지만 최근에 많이 사용하는 JPA를 사용하는 경우, 변경감지를 통해서 업데이트문을 최대한 지연해서 발행하는 방식을 사용하기 때문에 중첩된 트랜잭션 경계를 설정할 수 없어 지원하지 않는다.
JPA(Hibernate 구현체)에서 중첩 트랜잭션을 사용할려고 하면 아래와 같은 예외를 만나게 됩니다.
`org.springframework.transaction.NestedTransactionNotSupportedException: JpaDialect does not support savepoints - check your JPA provider's capabilities`
#### NEVER
트랜잭션이 존재하는 경우에 예외를 발생시켜 트랜잭션을 사용하지 않는 것을 강제하는 속성이다.
#### NOT_SUPPORTED
트랜잭션이 존재할 경우 해당 트랜잭션을 중단하고 트랜잭션이 없는 상태로 처리를 수행한다.
#### REQUIRED
기본값으로 사용되는 속성으로 트랜잭션이 존재하지 않을 경우 개시하고 있으면 그대로 사용하는 속성이다.
어노테이션기반의 설정일 경우에는 어노테이션에 기본값으로 명시되어있으며 그 이외의 경우에는 별도로 지정하지 않은경우 org.springframework.transaction.support.DefaultTransactionDefinition의 기본값이 사용된다.
#### REQUIRES_NEW
트랜잭션이 존재할 경우 해당 트랜잭션을 중단하고 새로운 트랜잭션 경계를 설정하는 속성으로 트랜잭션이 존재하지 않는 경우에는 REQUIRED와 동일한 동작을 한다.
모든 트랜잭션 매니저가 실제 트랜잭션 중단을 지원하는 것은 아니기 때문에 일반적으로 기존 트랜잭션을 방치한 상태로 새로운 트랜잭션을 생성한다.
물리적으로 데이터베이스 커넥션을 새로 얻는다는 의미이다.
요청이 많은 특정 서비스에 사용할 경우 데이터베이스 커넥션을 얻기위해 대기하는 리소스 데드락(Resource Deadlock - 특정리소스를 점유한 스레드들이 동일한 리소스를 얻으려고 대기하는 상태) 을 유발할 가능성이 있으므로 주의해서 사용해야할 필요가 있다.
위에서 설명한 NOT_SUPPORTED의 경우도 트랜잭션이 중단된 상태에서 다시 REQUIRED를 만나게 되면 동일한 현상이 발생할 가능성이 있다.
#### SUPPORTS
트랜잭션이 존재하면 해당 트랜잭션을 사용하고 존재하지 않을 경우 트랜잭션 경계를 설정하지 않는 속성이다.
내부적으로 트랜잭션관련된 처리는 없지만 실패할 경우 트랜잭션 롤백을 해야할 경우에 사용할 수 있다.
## 격리레벨(Isolation Level)
JDBC에서 제공하는 격리레벨을 설정하는 속성이다.
|속성|설명|
|----|----|
|DEFAULT|사용하는 저장소의 기본 격리레벨을 이용하는 속성으로 데이터베이스마다 다를 수 있음|
|READ_UNCOMMITTED|다른 트랜잭션에의해 커밋되지 않은 변경사항을 읽을 수 있는 격리레벨로 Dirty read, Nonrepeatable read, Panthom read가 발생|
|READ_COMMITTED|다른 트랜잭션에 의해 커밋된 내용이 읽을때마다 반영되는 격리레벨. Nonrepeatable read, Panthom read가 발생합니다. Oracle(오라클), PostgreSQL등의 기본 격리레벨|
|REPEATABLE_READ|동일 트랜잭션 경계안에서 반복해서 읽을 경우 다른 트랜잭션에 의해 커밋된 내용이 반영되지 않고 동일한 내용이 읽히는 격리레벨. 다만 Panthom read는 발생|
|SERIALIZABLE|해당하는 테이블을 모두 잠그는 가장 높은 수준의 격리레벨로 다른 레벨에서 발생할 수 있는 모든 문제가 차단됨. 하지만 성능적인 측면에서 문제가 있어서 거의 사용되지 않음|
- Dirty read는 커밋되지 않는 변경사항이 읽히는 문제로 해당하는 내용이 롤백될 경우 읽은 내용이 유효하지 않을 가능성이 있는 문제이다.
- Nonrepeatable read는 트랜잭션 경계 내부에서 반복적으로 읽기를 수행할때 다른 데이터를 읽을 수 있는 가능성이 있는 문제이다.
- Panthom read는 다른 트랜잭션에 의해서 추가된 행(Row)이 읽히는 문제이다.
## 주의사항
Spring에서 제공하는 트랜잭션을 사용하면서 가장 중요하게 인식해야할 사항은 트랜잭션이 적용된 메소드를 경계로 트랜잭션의 상태가 관리된다는 점이다.
예외를 트랜잭션이 적용된 메소드 외부로 던지면 트랜잭션에 롤백해야한다고 표시되며 해당 트랜잭션을 커밋할려고 시도할 경우 아래와 같은 예외와 만나게 된다.
`org.springframework.transaction.UnexpectedRollbackException: Transaction silently rolled back because it has been marked as rollback-only`
`Could not commit JPA transaction; nested exception is javax.persistence.RollbackException: Transaction marked as rollbackOnly`
따라서 예외가 트랜잭션이 적용된 메소드 경계를 지나 던져졌을 경우 catch를 이용하여 잡더라도 특정 처리후에 다시 던지거나 다른 예외를 던저야 한다는 점에 주의해야한다.
또 한가지 주의할 점은 Load Time Weaving(LTW)나 Compile Time Weaving등을 별도로 사용하지 않는 경우 AOP가 Proxy기반으로 동작한다는 점이다.
이는 특정 Spring 빈 내부에서 this를 통해서 다른 메소드를 호출할 경우 트랜잭션에 관한 설정이 적용되지 않는다는 점이다.
따라서 빈 내부에서 트랜잭션이 선언된 내부의 메소드를 호출할 경우에도 ApplicationContext를 통해서 빈의 레퍼런스를 얻는 방법을 통해서 Proxy를 경유해서 호출해야 트랜잭션에 관한 선언이 적용된다.
