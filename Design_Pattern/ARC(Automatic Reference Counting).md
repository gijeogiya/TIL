# 자동 참조  카운트 ARC (Automatic Reference Counting)

## 참조 횟수 계산 방식(reference counting)

### 참조 횟수 계산 방식(reference counting)

참조 횟수 계산 방식(reference counting)은 메모리를 제어하는 방법 중 하나로, 쓰레기 수집의 한 방식이다. 구성 방식은 단순하다. 어떤 한 동적 단위(객체, Object)가 참조값을 가지고 이 단위 객체가 참조(참조 복사)되면 참조값을 늘리고 참조한 다음 더이상 사용하지 않게 되면 참조값을 줄이면 된다. 보통 참조값이 0이 되면 더이상 유효한 단위 객체로 보지 않아 메모리에서 제거한다.

### 문제점

약점으로는 매번 참조할 때마다 참조값을 검사해야 하므로 많은 수의 단위 객체를 사용하게 되면 그 검사에 대한 부하가 커진다. 또한 참조하는 단위 객체 사이에 서로 참조하게 되면 순환 참조 오류로 인해 잘못된 참조 파괴가 생기거나 또는 단위 객체가 고아(orphaned)가 될 수 있다.

### 방식

참조 횟수 계산 방식에는 강한 참조(strong reference)와 약한 참조(weak reference)가 있는데 보통 참조 횟수 계산 방식을 이야기 할때는 강한 참조를 말하며, 약점으로 지적된 순환 참조 오류를 해소하기 위해 약한 참조를 사용하기도 한다.



## 자동 참조  카운트 (Automatic Reference Counting)

### 자동 참조  카운트 (Automatic Reference Counting)

Swift에서는 앱의 메모리 사용을 관리하기 위해 ARC(Automatic Reference Counting)을 사용한다. 자동으로 참조 횟수를 관리하기 때문에 대부분의 경우에 개발자는 메모리 관리에 신경쓸 필요가 없고 ARC가 알아서 더이상 사용하지 않는 인스턴스를 메모리에서 해지한다. **하지만 몇몇의 경우 ARC에서 메모리 관리를 위해 코드의 특정 부분에 대한 관계에 대한 정보를 필요로 한다.** 참조 횟수는 클래스 타입의 인스턴스에만 적용되고 값 타입인 구조체 열거형 등에는 적용되지 않는다.



### 동작

ARC가 실제 어떻게 동작하는지 예제 코드를 통해 확인해 보자. 아래 코드는 하나의 클래스를 선언하고 클래스의 인스턴스가 생성될 때와 해지될때 print로 로그를 찍게 구현한 클래스이다.

```swift
class Person {
    let name: String
    init(name: String) {
        self.name = name
        print("\(name) is being initialized")
    }
    deinit {
        print("\(name) is being deinitialized")
    }
}
```

위에서 선언한 `Person`클래스 타입을 갖는 reference 변수 3개를 선언합니다. 이 변수는 모두 옵셔널 변수이다. 그래서 초기값으로 모두 `nil`을 갖고 있다.

```swift
var reference1: Person?
var reference2: Person?
var reference3: Person?
```

하나의 변수에 Person 인스턴스를 생성에 참조하도록 한다.

```swift
reference1 = Person(name: "gi jeong")
// Prints "John Appleseed is being initialized"
```

나머지 두 변수를 첫 번째 변수를 참조하도록 한다.

```swift
reference2 = reference1
reference3 = reference1
```

이 경우 `reference2`, `reference3`모두 처음에 `reference1`이 참조하고 있는 같은 `Person`인스턴스를 참조하게 된다. 이 시점에 `Person`인스턴스에 대한 참조 횟수는 3이 된다. 그리고 나서 `reference1`, `reference2`두 변수의 참조를 해지한다. 그렇게 되면 `Person` 인스턴스에 대한 참조 횟수는 아직 1이어서 `Person`인스턴스는 해지되지는 않는다.

```swift
reference1 = nil
reference2 = nil
```

`Person`인스턴스를 참조하고있는 나머지 변수 `reference3`의 참조를 해지하면 더이상 `Person`인스턴스를 참조하고있는 것이 없으므로 ARC가 `Person`인스턴스를 메모리에서 해지하게 된다.

```swift
reference3 = nil
// Prints "gi jeong is being deinitialized"
```

위에 해지 로그가 찍히는 것으로 `Person`인스턴스가 메모리에서 내려 갔음을 확인할 수 있다.



### 클래스 인스턴스간 강한 참조 순환 문제 해결

![referenceCycle03_2x](ARC(Automatic Reference Counting).assets/referenceCycle03_2x.png)

변수 john과 unit4A는 각 인스턴스에 대한 참조를 하고 있지 않지만 Person인스턴스와 Apartment인스턴스의 변수가 각각 상호 참조를 하고 있어 참조 횟수가 1이기 때문에 이 두 인스턴스는 해지되지 않고 메모리 누수가 발생합니다.



### 약한 참조 (Weak References)

약한 참조로 선언하면 참조하고 있는 것이 먼저 메모리에서 해제되기 때문에 ARC는 약한 참조로 선언된 참조 대상이 해지 되면 런타임에 자동으로 참조하고 있는 변수에 nil을 할당한다. 

![cbxczfdfd](ARC(Automatic Reference Counting).assets/cbxczfdfd.png)

john의 참조 대상을 nil로 할당하면 더 이상 Person 인스턴스를 참조하는 것이 없게 된다. 그 결과 ARC에서 아래 그림과 같이 Person 인스턴스를 메모리에서 해지한다. 

![zbdbdrs](ARC(Automatic Reference Counting).assets/zbdbdrs.png)

이 시점에서 변수 unit4A에 nil을 할당하면 Apartment 인스턴스를 참조하는 개체도 사라지게 되서 Apartment 인스턴스도 메모리에서 해지된다.



## 쓰레기 수집(garbage collection 가비지 컬렉션 GC)과의 비교

### 쓰레기 수집(garbage collection 가비지 컬렉션 GC)

 메모리 관리 기법 중의 하나로, 프로그램이 동적으로 할당했던 메모리 영역 중에서 필요없게 된 영역을 해제하는 기능이다. 영어를 그대로 읽어 가비지 컬렉션이라 부르기도 한다.



### 차이점

- 쓰레기 수집(garbage collection 가비지 컬렉션 GC)은 런타임 동안 쓰레기 영역을 찾아 해당 영역을 해제하기 때문에 런타임 동안 작동하므로서 성능 저하를 야기한다.
- 하지만 자동 참조  카운트 (Automatic Reference Counting)의 경우 컴파일 이전에 쓰레기 영역을 제거 하므로서 런타임동안의 성능저하를 야기하지 않는다.
- 대표적으로 애플의 경우 기존에 쓰레기 수집(garbage collection 가비지 컬렉션 GC)를 채택하여 사용했지만, 이후 Swift를 개발하여 자동 참조  카운트 (Automatic Reference Counting)를 채택, 성능을 개선했다.
