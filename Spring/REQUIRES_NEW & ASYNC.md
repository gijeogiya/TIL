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
java```
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
