# AdapterPattern

## Adapter

하나의 인터페이스를 다른 인터페이스로 전환 하는 것

![image-20220519193637320](C:\Users\msg01\AppData\Roaming\Typora\typora-user-images\image-20220519193637320.png)

## AdapterPattern

인터페이스의 형태를 Adapter의 도움으로 바꾸어주어 사용 할 수 있게 해주는 디자인 패턴

- Adapter의 구조가 class를 감싸서 새로운(별표)형태의 인터페이스만 내어 놓는 것으로 보여 Wrapper라고 불리기도 한다.

![image-20220519194031812](C:\Users\msg01\AppData\Roaming\Typora\typora-user-images\image-20220519194031812.png)



### 예시 Code

![image-20220519200234075](C:\Users\msg01\AppData\Roaming\Typora\typora-user-images\image-20220519200234075.png)

```python
class Animal:     #interface class
  def walk(self):
    pass

class Cat(Animal):
  def walk(self):
    print("cat walking")

class Dog(Animal):
  def walk(self):
    print("dog walking")

def makeWalk(animal : Animal):
  animal.walk()

kitty = Cat()
bingo = Dog()

makeWalk(kitty)
makeWalk(bingo)
```

//cat walking

//dog walking



```python
class Fish:    #fish doesn't have a run method
  def swim(self):
    print("fish swimming")

nemo = Fish()

makeWalk(nemo)  #nemo cannot walk
```

//AttributeError: 'Fish' object has no attribute 'walk'



```python
class FishAdapter(Animal):
  def __init__(self, fish:Fish):
    self.fish = fish
  
  def walk(self):
    self.fish.swim()

adapted_nemo = FishAdapter(nemo)
makeWalk(adapted_nemo)
```

//fish swimming