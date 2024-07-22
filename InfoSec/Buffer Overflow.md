# Buffer Overflow(버퍼 오버플로우)
> 버퍼 오버플로는 버퍼에 데이터를 쓰는 프로그램이 해당 버퍼의 용량을 초과할 때 발생한다.
> 이는 8온스 잔에 12온스의 우유를 붓는 것과 같다.
## Buffer Overflow(버퍼 오버플로우)
- 버퍼 오버플로는 버퍼에 데이터를 쓰는 소프트웨어가 버퍼의 용량을 초과하여 인접한 메모리 위치를 덮어쓸 때 발생하는 비정상적인 현상이다.
- 달리 말하자면, 공간이 충분하지 않은 컨테이너에 너무 많은 정보가 전달되어 결국 해당 정보가 인접한 컨테이너의 데이터를 대체하게 되는 것이다.
- 버퍼 오버플로는 프로그램 실행을 방해하거나 제어하기 위해 컴퓨터의 메모리를 수정하려는 공격자가 악용할 수 있다.
![image](https://github.com/user-attachments/assets/8d9aeeaa-2796-4fd8-b3ae-a1e06e19527d)
## Buffer(버퍼)
- 버퍼 또는 데이터 버퍼는 데이터를 한 장소에서 다른 장소로 이동하는 동안 임시로 저장하는 데 사용되는 물리적 메모리 저장 영역이다.
- 이러한 버퍼는 일반적으로 RAM 메모리에 저장된다.
- 컴퓨터는 성능 향상을 위해 버퍼를 자주 사용하고, 대부분의 최신 하드 드라이브는 데이터에 효율적으로 액세스하기 위해 버퍼링을 활용하며, 많은 온라인 서비스에서도 버퍼를 사용한다.
- 예를 들어 버퍼는 온라인 동영상 스트리밍에서 끊김을 방지하기 위해 자주 사용된다.
- 동영상이 스트리밍되면 동영상 플레이어는 한 번에 약 20%의 동영상을 다운로드하여 버퍼에 저장한 다음 해당 버퍼에서 스트리밍한다.
- 이렇게 하면 연결 속도가 약간 떨어지거나 빠른 서비스 중단이 발생해도 동영상 스트리밍 성능에는 영향이 미치지 않는다.
- 버퍼는 특정 양의 데이터를 담도록 설계되어있다.
- 버퍼에 너무 많은 데이터가 전송되면 데이터를 삭제하는 명령이 버퍼를 사용하는 프로그램에 내장되어 있지 않은 한, 프로그램은 버퍼에 인접한 메모리에 있는 데이터를 덮어쓴다.
- 공격자는 버퍼 오버플로를 악용하여 소프트웨어를 손상시킬 수 있다.
- 버퍼 오버플로 공격은 잘 알려져 있음에도 불구하고 여전히 사이버 보안 팀을 괴롭히는 주요 보안 문제이다.
- 2014년에는 'Heartbleed'로 알려진 위협 때문에 수억 명의 사용자가 SSL 소프트웨어의 버퍼 오버플로 취약점으로 인해 공격에 노출되었다.
## 공격자는 버퍼 오버플로를 어떻게 악용할까?
- 공격자는 신중하게 조작된 입력을 프로그램에 의도적으로 삽입하여 프로그램이 해당 입력을 충분히 크지 않은 버퍼에 저장하도록 하여 버퍼 공간에 연결된 메모리 일부를 덮어쓰게 할 수 있다.
- 프로그램의 메모리 레이아웃이 잘 정의되어 있다면 공격자는 실행 코드가 포함된 것으로 알려진 영역을 의도적으로 덮어쓸 수 있다. 그런 다음 공격자는 이 코드를 자신의 실행 코드로 대체하여 프로그램의 작동 방식을 크게 변경할 수 있다.
- 예를 들어 메모리의 덮어쓴 부분에 포인터(메모리의 다른 위치를 가리키는 객체)가 포함되어 있는 경우 공격자의 코드는 해당 코드를 익스플로잇 페이로드를 가리키는 다른 포인터로 대체할 수 있다. 이렇게 하면 전체 프로그램의 제어권이 공격자의 코드로 넘어갈 수 있다.
## 버퍼 오버플로 공격으로부터 보호하는 방법
- 다행히 최신 운영 체제에는 버퍼 오버플로 공격을 완화하는 데 도움이 되는 런타임 보호 기능이 있다.
- 익스플로잇 위험을 완화하는 데 도움이 되는 두 가지 일반적인 보호 기능은 아래와 같다.
  - 주소 공간 무작위화: 프로세스의 주요 데이터 영역의 주소 공간 위치를 무작위로 재배치합니다.버퍼 오버플로 공격은 일반적으로 중요한 실행 코드의 정확한 위치를 알고 있어야 하는데, 주소 공간이 무작위화되면 이것이 거의 불가능해진다.
  - 데이터 실행 방지: 특정 메모리 영역을 실행 가능 또는 비실행 가능으로 표시하여 익스플로잇이 비실행 영역에서 발견된 코드를 실행하지 못하도록 만든다.
- 소프트웨어 개발자는 보호 기능이 내장된 언어로 작성하거나 코드에 특별한 보안 절차를 사용하여 버퍼 오버플로 취약점에 대한 예방 조치를 취할 수도 있다.
- 예방 조치에도 불구하고 개발자들이 새로운 버퍼 오버플로 취약점을 계속 찾아내고 있으며, 때로는 익스플로잇의 성공에 뒤이어 찾아내기도 한다. 새로운 취약점이 발견되면 엔지니어는 영향을 받는 소프트웨어에 패치를 적용하고 해당 소프트웨어 사용자가 패치에 액세스할 수 있도록 해야한다.
## 버퍼 오버플로 공격의 유형
- 스택 오버플로 공격: 가장 일반적인 유형의 버퍼 오버플로 공격으로, 호출 스택*의 버퍼를 오버플로시키는 공격이다.
- 힙 오버플로 공격: 이 유형의 공격은 힙*으로 알려진 개방형 메모리 풀의 데이터를 대상으로 한다.
- 정수 오버플로 공격: 정수 오버플로의 경우에는 산술 연산으로 인해 저장하려는 정수 유형에 비해 너무 큰 정수가 생성되며, 이로 인해 버퍼 오버플로가 발생할 수 있다.
- 유니코드 오버플로: 유니코드 오버플로는 ASCII 문자를 예상하는 입력에 유니코드 문자를 삽입하여 버퍼 오버플로를 생성합니다.(ASCII와 유니코드는 컴퓨터가 텍스트를 표현할 수 있도록 하는 인코딩 표준이다. 예를 들어 문자 'a'는 ASCII에서 숫자 97로 표시됩니다.ASCII 코드는 서양 언어의 문자만 지원하지만, 유니코드는 지구상의 거의 모든 문자 언어의 문자를 생성할 수 있다. 유니코드로 사용할 수 있는 문자가 훨씬 더 많으므로 유니코드 문자가 가장 큰 ASCII 문자보다 큰 경우가 많다)
> 컴퓨터는 스택과 힙이라는 두 가지 메모리 할당 모델을 사용하며, 이 두 모델은 모두 컴퓨터의 RAM에 저장된다. 스택은 깔끔하게 정리되어 있으며 데이터를 후입선출(Last-In, First-Out) 모델로 보관한다. 탄창에 마지막으로 삽입된 총알이 가장 먼저 발사되는 것처럼 가장 최근에 스택에 배치된 데이터 조각이 가장 먼저 나온다. 힙은 정리되지 않은 여분의 메모리 풀이며, 데이터가 특정 순서로 힙에 들어오고 나가지 않는다. 스택에서 메모리에 액세스하는 것이 힙에서 액세스하는 것보다 훨씬 빠르므로 일반적으로 힙은 대용량 데이터나 프로그래머가 명시적으로 관리하고자 하는 데이터에 주로 사용된다.