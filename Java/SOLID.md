# 객체지향 프로그래밍의 5가지 설계 원칙, SOLID
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
## 개방 폐쇄 원칙 (Open-Closed Principle, OCP)
개방 폐쇄 원칙(Open-Closed Principle, OCP)은 **확장에 대해 열려있고 수정에 대해서는 닫혀있어야 한다는 원칙**으로, 각각이 갖는 의미는 다음과 같다.       
- 확장에 대해 열려 있다: 요구사항이 변경될 때 새로운 동작을 추가하여 애플리케이션의 기능을 확장할 수 있다.
- 수정에 대해 닫혀 있다: 기존의 코드를 수정하지 않고 애플리케이션의 동작을 추가하거나 변경할 수 있다.
이번에는 비밀번호 암호화를 강화해야 한다는 요구사항이 새롭게 들어왔다고 가정하자. 비밀번호 암호화를 강화하기 위해 다음과 같이 SHA-256 알고리즘을 사용하는 새로운 PasswordEncoder를 생성하였다.        
(물론 SHA256 해시 알고리즘을 비밀번호 암호화에 사용하는 것은 적절하지 못하다. 그 이유는 SHA256으로 해시되는 값들을 미리 적어두어 해킹하는 레인보우 테이블 공격 기법을 사용할 수 있기 때문이다. 그러나 여기서는 개방 폐쇄의 원칙을 설명하기 위함이므로 예시로 사용하고자 한다.)
```java
@Component
public class SHA256PasswordEncoder {

    private final static String SHA_256 = "SHA-256";

    public String encryptPassword(final String pw)  {
        final MessageDigest digest;
        try {
            digest = MessageDigest.getInstance(SHA_256);
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalArgumentException();
        }

        final byte[] encodedHash = digest.digest(pw.getBytes(StandardCharsets.UTF_8));

        return bytesToHex(encodedHash);
    }

    private String bytesToHex(final byte[] encodedHash) {
        final StringBuilder hexString = new StringBuilder(2 * encodedHash.length);

        for (final byte hash : encodedHash) {
            final String hex = Integer.toHexString(0xff & hash);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }

        return hexString.toString();
    }
}
```
그리고 새로운 비밀번호 암호화 정책을 적용하려고 봤더니 새로운 암호화 정책과 무관한 UserService를 다음과 같이 수정해주어야 하는 문제가 발생하였다.    
```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final SHA256PasswordEncoder passwordEncoder;

    ...
    
}
```
이는 기존의 코드를 수정하지 않아야 하는 개방 폐쇄 원칙에 위배된다. 그리고 나중에 또 다시 비밀번호 암호화 정책을 변경해야 한다는 요구사항이 온다면 또 다시 UserService에 변경에 필요해진다.      
이러한 문제를 해결하고 개방 폐쇄 원칙을 지키기 위해서는 추상화에 의존해야 한다. 추상화란 핵심적인 부분만 남기고, 불필요한 부분은 제거함으로써 복잡한 것을 간단히 하는 것이고, 추상화를 통해 변하지 않는 부분만 남김으로써 기능을 구체화하고 확장할 수 있다. 변하지 않는 부분은 고정하고 변하는 부분을 생략하여 추상화함으로써 변경이 필요한 경우에 생략된 부분을 수정하여 개방-폐쇄의 원칙을 지킬 수 있다.       
위의 예제에서 변하지 않는 것은 사용자를 추가할 때 암호화가 필요하다는 것이고, 변하는 것은 사용되는 구체적인 암호화 정책이다. 그러므로 UserService는 어떠한 구체적인 암호화 정책이 사용되는지는 알 필요 없이 단지 passwordEncoder 객체를 통해 암호화가 된 비밀번호를 받기만 하면 된다.        
그러므로 UserService가 구체적인 암호화 클래스에 의존하지 않고 PasswordEncoder라는 인터페이스에 의존하도록 추상화하면 우리는 개방 폐쇄의 원칙이 충족되는 코드를 작성할 수 있다.       
```java
public interface PasswordEncoder {
    String encryptPassword(final String pw);
}

@Component
public class SHA256PasswordEncoder implements PasswordEncoder {

    @Override
    public String encryptPassword(final String pw)  {
        ...
    }
}

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public void addUser(final String email, final String pw) {
        final String encryptedPassword = passwordEncoder.encryptPassword(pw);

        final User user = User.builder()
            .email(email)
            .pw(encryptedPassword).build();

        userRepository.save(user);
    } 
}
```
OCP가 본질적으로 얘기하는 것은 추상화이며, 이는 결국 런타임 의존성과 컴파일타임 의존성에 대한 이야기이다. 여기서 런타임 의존성이란 애플리케이션 실행 시점에서의 객체들의 관계를 의미하고, 컴파일타임 의존성이란 코드에 표현된 클래스들의 관계를 의미한다.        
다형성을 지원하는 객체지향 프로그래밍에서 런타임 의존성과 컴파일타임 의존성은 동일하지 않다. 위의 예제에서 UserService는 컴파일 시점에 추상화된 PasswordEncoder에 의존하고 있지만 런타임 시점에는 구체 클래스(SHA256PasswordEncoder)에 의존한다.     
       
객체가 알아야 하는 지식이 많으면 결합도가 높아지고, 결합도가 높아질수록 개방-폐쇄의 원칙을 따르는 구조를 설계하기가 어려워진다. 추상화를 통해 변하는 것들은 숨기고 변하지 않는 것들에 의존하게 하면 우리는 기존의 코드 및 클래스들을 수정하지 않은 채로 애플리케이션을 확장할 수 있다. 그리고 이것이 개방 폐쇄의 원칙이 의미하는 것이다. 개방 폐쇄 원칙은 확장성이 코드 품질의 중요한 척도이기 때문에 가장 유용하다.        
그렇다고 하여 추후 확장될 가능성이 거의 없는 것들까지 미리 준비하는 것은 과도한 설계가 될 수 있다. 개방 폐쇄 원칙은 “공짜”가 아니다. 따라서 코드의 확장성과 가독성 사이에서 적절한 균형이 필요하다. 따라서 단기간 내에 진행할 수 있는 확장, 코드 구조 변경에 미치는 영향이 비교적 큰 확장, 구현 비용이 많이 들지 않는 확장에 대해 확장 포인트를 미리 준비하되, 향후 지원 여부가 확실하지 않은 요구사항이나 확장이 오히려 개발에 부하를 주는 경우에는 해당 작업이 실제로 필요할 때 리팩터링하는 것이 더 나을 수 있다.       
## 인터페이스 분리 원칙 (Interface segregation principle, ISP)
객체가 충분히 높은 응집도의 작은 단위로 설계됐더라도, 목적과 관심이 각기 다른 클라이언트가 있다면 인터페이스를 통해 적절하게 분리해줄 필요가 있는데, 이를 인터페이스 분리 원칙이라고 부른다. 즉, 인터페이스 분리 원칙이란 클라이언트의 목적과 용도에 적합한 인터페이스 만을 제공하는 것이다. 인터페이스 분리 원칙을 준수함으로써 모든 클라이언트가 자신의 관심에 맞는 퍼블릭 인터페이스(외부에서 접근 가능한 메세지)만을 접근하여 불필요한 간섭을 최소화할 수 있으며, 기존 클라이언트에 영향을 주지 않은 채로 유연하게 객체의 기능을 확장하거나 수정할 수 있다.       
인터페이스 분리 원칙을 지킨다는 것은 어떤 구현체에 부가 기능이 필요하다면 이 인터페이스를 구현하는 다른 인터페이스를 만들어서 해결할 수 있다. 예를 들어 파일 읽기/쓰기 기능을 갖는 구현 클래스가 있는데 어떤 클라이언트는 읽기 작업 만을 필요로 한다면 별도의 읽기 인터페이스를 만들어 제공해주는 것이다.
예를 들어 사용자가 비밀번호를 변경할 때 입력한 비밀번호가 기존의 비밀번호와 동일한지 검사해야 하는 로직을 다른 Authentication 로직에 추가해야 한다고 가정하자. 그러면 우리는 다음과 같은 isCorrectPassword라는 퍼블릭 인터페이스를 SHA256PasswordEncoder에 추가해줄 것이다.      
```java
@Component
public class SHA256PasswordEncoder implements PasswordEncoder {

    @Override
    public String encryptPassword(final String pw)  {
        ...
    }

    public String isCorrectPassword(final String rawPw, final String pw) {
        final String encryptedPw = encryptPassword(rawPw);
        return encryptedPw.equals(pw);
    }
}
```
하지만 UserService에서는 비밀번호 암호화를 위한 encryptPassword() 만을 필요로 하고, 불필요하게 isCorrectPassword를 알 필요가 없다. 현재 UserService는 PasswordEncoder를 주입받아 encrpytPassword에만 접근 가능하므로 인터페이스 분리가 잘 된 것 처럼 보인다. 하지만 새롭게 추가될 Authentication 로직에서는 isCorrectPassword에 접근하기 위해 구체 클래스인 SHA256PasswordEncoder를 주입받아야 하는데 그러면 불필요한 encryptPassword에도 접근 가능해지고, 인터페이스 분리 원칙을 위배하게 된다.       
물론 PasswordEncoder에 isCorrectPassword 퍼블릭 인터페이스를 추가해줄 수 있지만, 클라이언트의 목적과 용도에 적합한 인터페이스 만을 제공한다는 인터페이스 분리 원칙을 지키기 위해서라도 이미 만든 인터페이스는 건드리지 않는 것이 좋다.      
그러므로 위의 상황을 해결하기 위해서는 비밀번호를 검사를 의미하는 별도의 인터페이스(PasswordChecker)를 만들고, 해당 인터페이스로 주입받도록 하는 것이 적합하다.      
```java
public interface PasswordChecker {
    String isCorrectPassword(final String rawPw, final String pw);
}

@Component
public class SHA256PasswordEncoder implements PasswordEncoder, PasswordChecker {

    @Override
    public String encryptPassword(final String pw)  {
        ...
    }
  
    @Override
    public String isCorrectPassword(final String rawPw, final String pw) {
        final String encryptedPw = encryptPassword(rawPw);
        return encryptedPw.equals(pw);
    }
}
```
클라이언트에 따라 인터페이스를 분리하면 변경에 대한 영향을 더욱 세밀하게 제어할 수 있다. 그리고 이렇게 인터페이스를 클라이언트의 기대에 따라 분리하여 변경에 의해 의한 영향을 제어하는 것을 인터페이스 분리 원칙이라고 부른다.    
여기서 인터페이스는 꼭 하나의 인터페이스 파일에만 해당하지는 않는다. 인터페이스 분리 원칙에서 이야기하는 인터페이스는 넓게 보아 아래의 내용들 까지 확장될 수도 있다.    
- API나 기능의 집합
- 단일 API 또는 기능
- 객체지향 프로그래밍의 인터페이스
## 리스코프 치환 원칙 (Liskov Substitution Principle, LSP)
리스코프 치환 원칙은 1988년 바바라 리스코프가 올바른 상속 관계의 특징을 정의하기 위해 발표한 것으로, 하위 타입은 상위 타입을 대체할 수 있어야 한다는 것이다. 즉, 해당 객체를 사용하는 클라이언트는 상위 타입이 하위 타입으로 변경되어도, 차이점을 인식하지 못한 채 상위 타입의 퍼블릭 인터페이스를 통해 서브 클래스를 사용할 수 있어야 한다는 것이다. 즉, 이는 클라이언트와 객체 사이의 계약이 존재하고, 이를 준수해야 한다는 원칙이므로 계약에 따른 설계(design by contract) 라고 표현할 수도 있다. 하위 클래스는 상위 클래스의 동작 규칙(계약)을 따라야 하는 것이다.       
     
리스코프 치환 원칙에 대해 이해하기 위해 기존의 예시들과 다른 정사각형은 직사각형이다(Square is a Rectangle)는 예시를 살펴보도록 하자. 직사각형과 정사각형을 각각 구현하면 다음과 같다.       
```java
@Getter
@Setter
@AllArgsConstructor
public class Rectangle {

    private int width, height;

    public int getArea() {
        return width * height;
    }

}

public class Square extends Rectangle {

    public Square(int size) {
        super(size, size);
    }
	
    @Override
    public void setWidth(int width) {
        super.setWidth(width);
        super.setHeight(width);
    }

    @Override
    public void setHeight(int height) {
        super.setWidth(height);
        super.setHeight(height);
    }
}
```
Square는 1개의 변수만을 생성자로 받으며, width나 height 1개 만을 설정하는 경우 모두 설정되도록 메소드가 오버라이딩 되어 있다.
이를 이용하는 클라이언트는 당연히 직사각형의 너비와 높이가 다르다고 가정할 것이고, 직사각형을 resize()하기를 원하는 경우 다음과 같은 메소드를 만들어 너비와 높이를 수정할 것이다. (항상 클라이언트의 입장에서 생각해야 함에 유의해야 한다.)
