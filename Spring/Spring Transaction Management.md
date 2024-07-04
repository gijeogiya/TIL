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
