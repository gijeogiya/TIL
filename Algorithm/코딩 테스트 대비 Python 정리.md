# 코딩 테스트 대비 Python 정리

## 문자열

- Immutable: 문자열을 변경할 수 없음
- `+` : 문자열 합치기 가능
- `*`: 문자열 연속 합치기 가능

- Iterable: 문자열을 순회 가능함

- `[index:index:value]`: 슬라이싱 가능

- `in`: 리스트안에 특정한 문자가 없는지 확인

- 리스트 >> 문자열 변환: map과 join을 활용

  ```python
  numbers_list = [1, 2, 3]
  number_str = '(접착제)'.join(map(str, numbers_list))
  
  # number_str은 '123'
  ```

- 문자열 >> 리스트 변환: split 또는 list 사용

  - 공백 또는 어떤 문자로 나누려면

    ```python
    my_str = "I am gijeong"
    my_list = my_str.split() #디폴트(괄호안에 아무것도 없으면)는 띄워쓰기
    
    # my_list는 ['I', 'am', 'gijeong']
    ```

    

  - 알파벳, 공백 등 한 글자씩 나누고 싶다면

    ```python
    my_str = "I am gijeong"
    my_list = list(my_str)
    
    # my_list는 ['I', ' ', 'a', 'm', ' ', 'g', 'i' ...]
    ```



## 리스트

### method

`extend`

`append`

`insert`: (index, item)

`remove`: (item)

`clear`

`pop`

`count` : (item)

`sort`

`reverse`



## 모듈

### Copy

`import copy`

`deepcopy`



### 순열, 조합

`from itertools import permutations`

`from itertools import combinations`

`list(permutations(items, 2))`

`list(combinations(items, 2))`



## deque

`from collections import deque`

- `deque.append(item)`: item을 데크의 오른쪽 끝에 삽입한다.
- `deque.appendleft(item)`: item을 데크의 왼쪽 끝에 삽입한다.
- `deque.pop()`: 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- `deque.popleft()`: 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
- `deque.extend(array)`: 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
- `deque.extendleft(array)`: 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
- `deque.remove(item)`: item을 데크에서 찾아 삭제한다.
- `deque.rotate(num)`: 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).