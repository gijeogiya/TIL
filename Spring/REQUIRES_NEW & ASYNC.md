# REQUIRES_NEW & ASYNC
**Requires_new is king of side effects**
“REQUIRES_NEW는 부작용 대장이다.”라는 말에는 그 이유가 있다.    
REQUIRES_NEW 전파 속성은 새로운 Transaction을 시작하는 기능을 가지며, 그로 인해 Dead Lock 발생의 위험성이 증가한다.    
이미 실행 중인 Transaction 내에서 이 전파 속성을 가진 메서드를 호출하면 새로운 Transaction이 시작된다.    
이 과정에서 Connection Pool의 Resource가 부족해지면 Dead Lock의 위험이 있다.    

## Dead Lock의 원리
REQUIRES_NEW는 이미 실행 중인 Transaction이 있을 때 새로운 Transaction을 시작하는 전파 속성이다.    
만약 동시에 많은 요청이 여러 Transaction을 시작하려 할 때, 사용 가능한 Connection Resource가 부족하게 되면 Dead Lock이 발생한다.    
