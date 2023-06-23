# FlyweightPattern
## 플라이웨이트 패턴이란?
- 인스턴스를 가능한 한 공유해서 사용함으로써 메모리를 절약하는 패턴
- 자주 변하는 속성(또는 외적인 속성, extrinsit)과 변하지 않는 속성(또는 내적인 속성, intrinsit)을 분리하고 재사용하여 메모리 사용을 줄일 수 있다.
![image](https://github.com/gijeogiya/TIL/assets/97646078/73ef2515-ba0b-48dc-b7a8-683306abb149)
![image](https://github.com/gijeogiya/TIL/assets/97646078/07a27382-4ef9-4d13-af1d-12094e695fe7)

## 예시
### 문제 상황
- 마인크래프트 게임에 나무를 설치하고 싶음
- 나무는 색(color)을 정할 수 있고, 특정 위치(x, y)에 세울 수 있음
- 만약 내가 마크에 미쳐서 나무 10000개를 맵에 심는다고 할 때, 나무 한 그루에 들어가는 데이터는 color : 4Byte , x: 4byte, y:4byte
- 즉, 모든 나무를 심을 때마다 객체를 생성한다면, 나무 10,000개에는 120,000byte 가 듬

### 어떻게 해결할까?
​- 모든 나무의 x, y는 다르지만 나무 색은 항상 바뀔 필요는 없다. 거의 같고 가끔 색 바꾸게 됩니다.
​- 그러면 나무를 계속 새로 만들지 말고, 저장해놨다가 가져다 쓰는 식으로 한다면?
-​ 그러면 새로운 색상의 나무가 추가될 때만 새 객체를 생성한다면, 나무가 10000개 여도 12 * (새로운 색상을 추가한 횟수) byte
-​ 내가 만약 색을 2개만 쓴다면 24byte 이니까 이전보다 119976byte 가량 절약
​- 나무 수가 많을 수록 더 절약할 수 있겠다. 이렇게 인스턴스를 가능한대로 공유시켜서 쓸데없는 new를 통한 메모리 낭비를 줄이는것이 Flyweight 패턴

### 어떻게 구현할까?
-​ 플라이웨이트 패턴을 구현하기 위해 아래 3가지가 필요
  1. 실제 공유될 객체 (나무)
  2. 객체의 인스턴스를 생성하고 공유해주는 팩토리(Factory) -> 같은 색의 나무가 없다면 새로 생성하고, 있다면 그 색의 나무를 반환
  3. 패턴을 사용할 고객, 클라이언트 -> 우리는 그냥 2번에게 OO색 나무를 요청하고, 받아서 X,Y를 설정하고 설치하면 된다.

### 예시 코드
1. 공유할 Tree 객체
```java
public class Tree {

    // 나무는 아래와 같이 3개 정보를 가지고 있음
    private String color;
    private int x;
    private int y;

    //색상으로만 생성자를 만들어줌
    public Tree(String color) {
        this.color = color;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    //나무를 심을 때
    public void install(){
        System.out.println("x:"+x+" y:"+y+" 위치에 "+color+"색 나무를 설치했습니다!");
    }
}
```

3. Tree를 제공해줄 TreeFactory
```java
public class TreeFactory {
    //HashMap 자료구조를 활용해서 만들어진 나무들을 관리
    public static final HashMap<String, Tree> treeMap = new HashMap<>();
    
   
    public static Tree getTree(String treeColor){
        //Map에 입력받은 색상의 나무가 있는지 찾음. 있으면 그 객체를 제공
        Tree tree = (Tree)treeMap.get(treeColor); 

       //만약 아직 같은 색상의 나무가 Map에 없다면 새로 객체를 생성해 제공
        if(tree == null){
            tree = new Tree(treeColor);
            treeMap.put(treeColor, tree);
            System.out.println("새 객체 생성");
        }

        return tree;
    }
}
```
5. 사용할 고객
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("원하는 색을 입력해주세요 :)");
        for(int i=0;i<10;i++){
            //나무 색 입력받기
            String input = scanner.nextLine();
            //팩토리에서 나무 하나 공급받기
            Tree tree = (Tree)TreeFactory.getTree(input);
            //나무 x,y 설정하고
            tree.setX((int) (Math.random()*100));
            tree.setY((int) (Math.random()*100));
            //나무 설치하기
            tree.install();
        }

    }
}
```

### 결과
```java
원하는 색을 입력해주세요 :)
초록
새로운 객체 생성
x:47 y:55 위치에 초록색 나무를 설치했습니다!
연두
새로운 객체 생성
x:86 y:33 위치에 연두색 나무를 설치했습니다!
초록
x:62 y:30 위치에 초록색 나무를 설치했습니다!
초록
x:83 y:21 위치에 초록색 나무를 설치했습니다!
초록
x:47 y:46 위치에 초록색 나무를 설치했습니다!
연두
x:49 y:59 위치에 연두색 나무를 설치했습니다!
연두
x:10 y:38 위치에 연두색 나무를 설치했습니다!
카키
새로운 객체 생성
x:78 y:39 위치에 카키색 나무를 설치했습니다!
카키
x:21 y:41 위치에 카키색 나무를 설치했습니다!
카키
x:58 y:26 위치에 카키색 나무를 설치했습니다!
```

### 싱글톤 패턴과의 비교

싱글톤 역시 객체를 하나만 생성하고 활용하는 패턴

우리가 제작한 Flyweight 패턴에서, 나무는 색깔이 바뀔 때 새로운 객체를 생성
색상 별로 하나씩, 결과적으로는 여러개의 나무가 생김
또한 만들어진 객체의 색상은 바꿀 수 없음.
따라서 하나씩 여러종류를 가질 수 있습니다.

그러나 싱글톤 패턴의 경우, 나무 클래스에 단 한개의 나무만 만들수 있음
따라서 싱글톤 패턴을 사용한다면, 만들어진 단 하나의 객체(나무)의 색깔을 바꿔야함
싱글톤은 이렇듯 하나의 클래스에 단 하나의 인스턴스를 생성하고, 대신 변수를 필요시 변경해가며 쓸 수 있다는 차이가 있음
따라서 싱글톤 패턴은 종류 상관없이 단 하나만 가질 수 있습니다.

## 장단점
### 장점
  - 애플리케이션에서 사용하는 메모리를 줄일 수 있다.
### 단점
  - 코드의 복잡도가 증가한다.

## 실무에서의 예시
### Java
- Integer.valueOf(int)
- 캐시를 제공한다.
- https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html#valueOf-int

### Java String
- 플라이웨이트 패턴은 Java의 String Constant Pool에 적용됨
- Java의 String은 만들어질때 String Constant Pool에 저장되어 같은 문자열이 pool에 있다면 이를 불러오는 방식으로 되어있음
