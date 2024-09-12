# # 객체지향 프로그래밍의 5가지 설계 원칙, SOLID
> SOLID란 객체 지향 프로그래밍을 하면서 지켜야하는 5대 원칙으로 각각 SRP(단일 책임 원칙), OCP(개방-폐쇄 원칙), LSP(리스코프 치환 원칙), DIP(의존 역전 원칙), ISP(인터페이스 분리 원칙)의 앞글자를 따서 만들어졌다. SOLID 원칙을 철저히 지키면 시간이 지나도 변경이 용이하고, 유지보수와 확장이 쉬운 소프트웨어를 개발하는데 도움이 되는 것으로 알려져있다.
## 단일 책임의 원칙(SRP, Single Responsibility Principle)
로버트 마틴은 SOLID 원칙 중에서 가장 의미가 전달되지 못한 것으로 단일 책임의 원칙(SRP, Single Responsibility Principle)을 뽑았는데, SRP는 하나의 모듈이 하나의 책임을 가져야 한다는 모호한 원칙으로 해석하면 안된다. 대신 모듈이 변경되는 이유가 한가지여야 함으로 받아들여야 한다. 여기서 변경의 이유가 한가지라는 것은 해당 모듈이 여러 대상 또는 액터들에 대해 책임을 가져서는 안되고, 오직 하나의 액터에 대해서만 책임을 져야 한다는 것을 의미한다.     
만약 어떤 모듈이 여러 액터에 대해 책임을 가지고 있다면 여러 액터들로부터 변경에 대한 요구가 올 수 있으므로, 해당 모듈을 수정해야 하는 이유 역시 여러 개가 될 수 있다. 반면에 어떤 모듈이 단 하나의 책임 만을 갖고 있다면, 특정 액터로부터 변경을 특정할 수 있으므로 해당 모듈을 변경해야 하는 이유와 시점이 명확해진다. 참고로 여기서 모듈이라 함은 클래스 혹은 클래스의 모음 등으로 해석할 수 있다.     
예를 들어 사용자의 입력 정보를 받고, 비밀번호를 암호화하여 데이터베이스에 저장하는 로직이 있다고 하자.      
```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public void addUser(final String email, final String pw) {
        final StringBuilder sb = new StringBuilder();

        for(byte b : pw.getBytes(StandardCharsets.UTF_8)) {
            sb.append(Integer.toString((b & 0xff) + 0x100, 16).substring(1));
        }

        final String encryptedPassword = sb.toString();
        final User user = User.builder()
            .email(email)
            .pw(encryptedPassword).build();

        userRepository.save(user);
    }
}
```
위의 UserService의 사용자 추가 로직에는 다음과 같은 다양한 액터로부터 변경이 발생할 수 있다.      
- 기획팀: 사용자를 추가할 때 역할(Role)에 대한 정의가 필요하다.
- 보안팀: 사용자의 비밀번호 암호화 방식에 개신이 필요하다.
- 기타 등등
 
이러한 문제가 발생하는 이유는 UserService가 여러 액터로부터 단 하나의 책임을 갖고있지 못하기 때문이며, 이를 위해서는 비밀번호 암호화에 대한 책임을 분리해야 한다.       
다음과 같이 비밀번호 암호화를 책임지는 별도의 클래스를 만들어 UserService로부터 이를 추상화하고, 해당 클래스를 합성하여 접근 및 사용하면 우리는 UserService로부터 비밀번호 암호화 방식을 개선해달라는 변경을 분리할 수 있다.
```java
@Component
public class SimplePasswordEncoder {

    public String encryptPassword(final String pw) {
        final StringBuilder sb = new StringBuilder();

        for(byte b : pw.getBytes(StandardCharsets.UTF_8)) {
            sb.append(Integer.toString((b & 0xff) + 0x100, 16).substring(1));
        }

        return sb.toString();
    }
}

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final SimplePasswordEncoder passwordEncoder;

    public void addUser(final String email, final String pw) {
        final String encryptedPassword = passwordEncoder.encryptPassword(pw);

        final User user = User.builder()
            .email(email)
            .pw(encryptedPassword).build();

        userRepository.save(user);
    }
}
```
단일 책임 원칙을 제대로 지키면 **변경이 필요할 때 수정할 대상이 명확**해진다. 그리고 이러한 단일 책임 원칙의 장점은 시스템이 커질수록 극대화되는데, 시스템이 커지면서 서로 많은 의존성을 갖게되는 상황에서 변경 요청이 오면 딱 1가지만 수정하면 되기 때문이다.       
단일 책임 원칙을 적용하여 적절하게 책임과 관심이 다른 코드를 분리하고, 서로 영향을 주지 않도록 추상화함으로써 애플리케이션의 변화에 손쉽게 대응할 수 있다.      
하지만 SRP를 위반하는지 판단하는 것은 상당히 어려운데, 그 이유는 동일한 대상이라 할지라도 유스케이스나 요구 사항의 단계에 따라 책임이 단일한지 여부가 달라질 수 있기 때문이다. 유스케이스를 변경하거나 요구 사항이 달라질 경우에는 기존에 충족했던 단일 책임 원칙이 충족되지 못할 수 있다. 또한 해당 클래스를 어떻게 바라보는가에 따라서도 다를 수 있다.        
예를 들어 다음의 Serializable 클래스는 직렬화 메서드와 역직렬화 메서드를 모두 갖고 있다. 해당 클래스는 SRP를 위반하는가?      
```java
@Getter
@RequiredArgsConstructor
public class Serializable<T> {

    private final Gson gson;

    public String serialize(T t) {
        return ...
    }
    
    public T deserialize(String input) {
        return ...
    } 
}
```
해당 클래스의 책임을 직렬화 자체만으로 보는지 또는 직렬화와 역직렬화는 사실상 세트니까 직렬화 전반에 대한 책임으로 보는지에 따라 다르다. 만약 해당 서비스가 임의의 데이터를 직렬화해서 적재만 하고, 해당 데이터를 역직렬화해서 후처리하는 것은 다른 서비스에서 맡고 있다면 SRP를 위반한다고도 판단할 수 있다. 하지만 캐시와 같은 저장소에 직접 직렬화해서 저장하고, 역직렬화해서 조회한다면 SRP를 위반하기 어렵다고 볼 수도 있을 것이다. 따라서 SRP를 판단하기 위해서는 유스케이스와 요구 사항 등을 고려해야 한다.
