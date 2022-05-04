# ObserverPattern

## ObserverPattern(감시자 패턴)

### Observer란 무엇인가?

Event가 일어 났을 때 바로 반응하는 녀석들

Subscriber, Listener 라고 불리기도 한다.



### Polling

주기적으로(1초, 1분, 1시간) 혹은 순번으로 Event가 있는지 없는지를 하는 것

문제점: 주기/순번 내에 Event가 발생했다가 사라지면 Event를 감지 할 수 없음



 