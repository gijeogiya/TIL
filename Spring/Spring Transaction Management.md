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
|propagation|트랜잭션 개시할지 등 전파행위에 관한 속성.|
|isolation|트랜잭션 격리레벨에 관한 속성으로 기본값은 Default레벨이며 실제 사용하는 데이터베이스(JDBC) 등의 기본값을 따릅니다.|
|readOnly|트랜잭션을 읽기전용으로 지정하는 속성. 최적화 관점에서 지원되는 프로터티이므로 현재 트랜잭션 상태에따라 다르게 동작할 수 있습니다.|
|timeout|트랜잭션의 타임아웃(초단위)을 지정하는 속성으로 지정하지 않을 경우 사용하는 트랜잭션 시스템의 타임아웃을 따릅니다.|
|rollbackFor|Checked 예외 발생시에 롤백을 수행할 예외를 지정하는 속성.|
|rollbackForClassName|rollbackFor와 동일하지만 문자열로 클래스명을 지정하는 속성.|
|noRollbackFor|Spring의 트랜잭션은 기본적으로 Runtime예외만 롤백처리를 수행하지만 Runtime예외중 특정 예외는 롤백을 수행하지 않아야 할 경우 사용하는 속성.|
|noRollbackForClassName|noRollbackFor와 동일하지만 문자열로 클래스명을 지정하는 속성.|
