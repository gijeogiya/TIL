# BuilderPattern
## 빌더 패턴
- 동일한 프로세스를 거처 다양한 구성의 인스턴스를 만드는 방법
- (복잡한) 객체를 만드는 프로세스를 독립적으로 분리할 수 있다.
- 빌더 패턴은 인스턴스를 생성자를 통해 직접 생성하지 않고, 빌더라는 내부 클래스를 통해 간접적으로 생성하게 하는 패턴이다.
![image](https://github.com/gijeogiya/TIL/assets/97646078/352de8cc-720a-45d9-8853-6b0287ec3835)

## 빌터 패턴 구현 방법
![image](https://github.com/gijeogiya/TIL/assets/97646078/770ec669-5187-46a9-9d2a-4903bcc5046f)
### 예시
```python
class Something:
    def __init__(self, number, name, size):
        self.number = number
        self.name = name
        self.size = size
    
    class Builder:
        def __init__(self):
            pass
        
        def setNumber(self, number):
            self.number = number
            return self
        
        def setName(self, name):
            self.name = name
            return self
        
        def setSize(self, size):
            self.size = size
            return self
        
        def build(self):
            return Something(self.number, self.name, self.size)
        
        
something = Something.Builder().setNumber(3).setName('st').setSize(7).build()

print(something.number, something.name, something.size)  # 3 st 7
```
### 사용 상황

>    클래스와 사용 대상의 결합도를 낮추기 위해

-   클래스의 사양 변경으로, 생성자에 인수로 전달하는 부분의 규격이 변경되었다면, 일반적인 경우 해당 클래스를 생성하는 모든 부분을 수정해야 한다.
-   **Builder를 사용하면 설정되지 않은 인수에 대해 적절한 값으로 초기화하고, 사용자의 요청에 따라 상세한 값을 설정하는 것도 가능하므로** 이러한 문제를 해결할 수 있다.
-   e.g., 위 `Something` 클래스에서 `weight`라는 인수를 추가로 할당하려고 하면, **일반 패턴에서는 생성자를 호출하는 모든 코드마다** `weight`라는 인자를 추가해야 하지만, **Builder 패턴에서는** 대상 클래스의 private 생성자에 `weight`를 추가하고, `setter`를 정의한 뒤 기본값을 `-1`로 설정하면 그냥 기능 추가가 된다.



>   복잡한 객체를 만들 때 인자에 의미를 부여

-   위 클래스에서 빌더 패턴이 없다면, `something = Something(3, 'st', 7)`이라고 작성한다.
-   생성자에 전달하는 인수의 개수가 많아진다면, 이러한 방식은 인수의 종류와 순서를 모두 외우고 있어야 하므로 매우 비효율적이다.

-   **따라서, 복잡한 객체를 만드는 데 좋은 패턴이다.**

    -   e.g., text (font, color, padding etc.,)
![image](https://github.com/gijeogiya/TIL/assets/97646078/bb2b4ce4-bc8d-4c1d-9a91-fe8a4da0a20e)
### 장단점
#### 장점
- 만들기 복잡한 객체를 순차적으로 만들 수 있다
- 복잡한 객체를 만드는 구체적인 과정을 숨길 수 있다.
- 동일한 프로세스를 통해 각기 다르게 구성된 객체를 만들 수도 있다
- 불완전한 객체를 사용하지 못하도록 방지할 수 있다
#### 단점
  - 원하는 객체를 만들려면 빌더부터 만들어야 한다
  - 구조가 복잡해 진다 (트레이드 오프)
## 실무에서 어떻게 쓰이나?
- 자바 8 Stream.Buidler API
- StringBuilder는 빌더 패턴일까?
- 롬복의 @Builder
  -https://projectlombok.org/features/Builder
- 스프링
  - UriComponentsBuilder
  - MockMvcWebClientBuilder
  - …Builder
