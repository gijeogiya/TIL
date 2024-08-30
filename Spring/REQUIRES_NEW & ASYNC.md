# REQUIRES_NEW & ASYNC
**Requires_new is king of side effects**
“REQUIRES_NEW는 부작용 대장이다.”라는 말에는 그 이유가 있다.    
REQUIRES_NEW 전파 속성은 새로운 Transaction을 시작하는 기능을 가지며, 그로 인해 Dead Lock 발생의 위험성이 증가한다.    
이미 실행 중인 Transaction 내에서 이 전파 속성을 가진 메서드를 호출하면 새로운 Transaction이 시작된다.    
이 과정에서 Connection Pool의 Resource가 부족해지면 Dead Lock의 위험이 있다.    

## Dead Lock의 원리
REQUIRES_NEW는 이미 실행 중인 Transaction이 있을 때 새로운 Transaction을 시작하는 전파 속성이다.    
만약 동시에 많은 요청이 여러 Transaction을 시작하려 할 때, 사용 가능한 Connection Resource가 부족하게 되면 Dead Lock이 발생한다.    
![image](https://github.com/user-attachments/assets/39fbae9e-bc41-4b24-9da1-b50ddf1552e7)

## 예시 상황
사용자가 ‘좋아요’를 누르면 알림을 전송하는 서비스가 있다고 가정하자.    
![image](https://github.com/user-attachments/assets/e71a87df-3744-425b-8472-4e760b5cb207)
`LikeService`는 좋아요 정보를 DB에 저장하고, `NotificationService`에 알림 전송을 요청한다.    
`NotificationService`는 알림을 전송하고, 알림 정보를 DB에 저장한다.    
알림 전송에 실패해도 좋아요 정보는 롤백되어서는 안 된다.    
`NotificationService`의 `sendNotification()`의 전파 속성을 `REQUIRES_NEW`로 설정함으로써 두 작업을 독립적인 트랜잭션으로 분리 가능하다.    

```java
@Service
@RequiredArgsConstructor
@Slf4j
public class LikeService {

	private final PostRepository postRepository;
	private final LikeRepository likeRepository;
	private final NotificationService notificationService;

	@Transactional
	public void like(Long postId) {
		Post post = postRepository.findById(postId).orElseThrow();
		Like like = likeRepository.save(new Like(post));
		try {
			notificationService.sendNotification(like);
		} catch (Exception e) {
			log.error("알림 전송 실패", e);
		}
	}
}

@Service
@RequiredArgsConstructor
public class NotificationService {

	private final NotificationRepository notificationRepository;
	private final NotificationClient notificationClient;

	@Transactional(propagation = Propagation.REQUIRES_NEW)
	public void sendNotification(Like like) {
		Notification notification = new Notification(like);
		notificationClient.send(notification);
		notificationRepository.save(notification);
	}
}
```
## 문제점
문제는 하나의 요청이 2개의 데이터베이스 커넥션을 점유한다는 것이다.     
(외부 트랜잭션과 내부 트랜잭션에서 각각 1개의 커넥션을 필요로 한다.)    
많은 요청이 동시에 들어오면, 커넥션 풀이 고갈되어 모든 커넥션들이 새로운 커넥션을 대기하는 데드락이 발생한다.     

## 해결 방안
이러한 데드락 위험성 때문에, 동시 요청이 많은 상황에서는 `REQUIRES_NEW`를 최대한 지양하는 것이 좋다.    
그러면 두 요청을 독립적인 트랜잭션으로 분리하고 싶을 땐 어떻게 할 수 있을까?    
### @Async 활용
`@Async` 어노테이션을 사용해 메서드를 비동기로 처리를 하면, 트랜잭션을 분리할 수 있다.     
비동기 메서드는 새로운 스레드에서 작업을 수행하는데, 트랜잭션은 스레드 로컬이기 때문에 두 요청에서 서로 다른 트랜잭션을 사용하게 된다.      
커넥션 풀이 가득 찬 상황이라도, 내부 트랜잭션은 외부 트랜잭션이 끝날 때까지 대기하다가 해당 커넥션을 가져간다.     
![image](https://github.com/user-attachments/assets/6896e0f5-829e-4841-bca1-7bdc193c64cb)
```java
@Async
@Transactional
public void sendNotification(Like like) {
	/***/
}
```
비동기로 호출 시, 외부 메서드가 내부 비동기 메서드의 결과를 기다리지 않고 반환한다.       
즉, 내부 메서드의 결과를 외부 메서드에서 활용해야 하는 경우에는 적합하지 않다.     
### FacadeService 활용
두 서비스 메서드 앞단에 FacadeService를 사용하면 데드락 문제를 해결할 수 있다.     
이 서비스는 트랜잭션을 적용하지 않고, 각 트랜잭션 메서드를 순차적으로 호출한다.     
이렇게 하면 각 메서드가 종료될 때마다 사용했던 커넥션을 반환하므로 데드락의 위험이 크게 줄어든다.     
![image](https://github.com/user-attachments/assets/2a418fd8-e146-4e18-8509-d33a49a6315c)
```java
@Service
@RequiredArgsConstructor
public class LikeFacadeService {

	private final LikeService likeService;
	private final NotificationService notificationService;

	public void like(Long postId) {
		Like like = likeService.like(postId);
		notificationService.sendNotification(like);
	}
}

@Service
@RequiredArgsConstructor
public class LikeService {
	/***/
	@Transactional
	public Like like(Long postId) {
		Post post = postRepository.findById(postId).orElseThrow();
		return likeRepository.save(new Like(post));
	}
}
```
이 경우 동기적으로 호출하기 때문에 Time Out 등의 문제가 발생 할 수 있다.     
이러한 것이 문제가 되는 경우 앞서 살펴본 `@Async` 어노테이션이 더 적합 할 수 있다.
