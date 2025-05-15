# Locality of Reference (참조 지역성)

참조 지역성의 원리(Locality of Reference)란 CPU가 메모리에 접근할 때 일정한 경향성을 보인다는 사실을 바탕으로 한 개념이다. 이 원리는 주로 캐시 메모리의 적중률을 높여 CPU의 메모리 접근 횟수를 줄이는 데 활용된다.

## 참조 지역성의 종류

참조 지역성은 크게 두 가지로 나뉜다.

### 1. 시간 지역성(Temporal Locality)

- 시간 지역성이란, **최근에 접근한 데이터를 다시 접근할 가능성이 높다**는 경향을 의미한다.
- 예시: 반복문 안에서 같은 변수나 배열 요소를 여러 번 사용하는 경우가 이에 해당한다.

### 2. 공간 지역성(Spatial Locality)

- 공간 지역성이란, **한 번 접근한 메모리 주소 근처의 데이터도 곧 접근할 가능성이 높다**는 경향을 의미한다.
- 예시: 배열을 순차적으로 탐색할 때 인접한 요소들을 연달아 접근하는 경우가 이에 해당한다.

## 백엔드 개발과의 연관성

참조 지역성의 원리는 대규모 데이터 처리, 캐시 설계, 데이터베이스 쿼리 최적화 등 백엔드 시스템의 성능 최적화에 직접적으로 영향을 준다.  
특히, 인메모리 캐시(Redis, Memcached)나 대용량 데이터 처리 파이프라인에서 데이터 접근 패턴을 잘 설계하면 시스템 전체의 처리 속도를 크게 높일 수 있다.

## 코드 개선 사례

아래 코드는 2차원 배열을 열 우선으로 순회하며 값을 증가시키는 예시이다.

```java
public class LocalityTest {

     @Test
     void test() {
        int size = 10240;
        int[][] array = new int[size][size];

        long beforeTime = System.currentTimeMillis();

        for (int j = 0; j < size; j++) {
            for (int i = 0; i < size; i++) {
                array[i][j]++;
            }
        }

        long afterTime = System.currentTimeMillis();
        long diffTime = afterTime - beforeTime;
       
        System.out.println("수행시간(m) : " + diffTime); // 577ms
    }
}
```

자바에서 2차원 배열은 내부적으로 1차원 배열(int[])에 대한 참조 배열로 구현되어 있다.  
즉, `array[i]`는 각각 독립적인 int[] 객체이며, 이들이 메모리상에서 연속적으로 배치된다는 보장은 없다.

CPU 캐시는 공간 지역성 원리에 따라 인접한 데이터를 미리 캐싱한다.  
하지만 위 코드처럼 열을 먼저 순회하면 물리적으로 멀리 떨어진 데이터를 반복적으로 읽게 되어 캐시 히트율이 떨어진다.

### 개선 방법

가장 쉬운 개선 방법은 **행을 먼저 순회**하는 것이다.

```java
public class LocalityTest {

     @Test
     void test() {
        int size = 10240;
        int[][] array = new int[size][size];

        long beforeTime = System.currentTimeMillis();

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                array[i][j]++;
            }
        }

        long afterTime = System.currentTimeMillis();
        long diffTime = afterTime - beforeTime;
       
        System.out.println("수행시간(m) : " + diffTime); // 28ms
    }
}
```

이렇게 하면 메모리 접근이 연속적으로 이루어져 캐시 히트율이 높아지고, 실제로 수행 시간이 크게 줄어드는 것을 확인할 수 있다.

## 추가적인 개선 방안

- **병렬 처리**: 멀티코어 환경에서는 `IntStream.range(0, size).parallel()`을 사용해 병렬로 행을 처리할 수 있다.
- **로컬 변수 캐싱**: 배열의 행을 지역 변수에 할당하여 접근 속도를 높일 수 있다.

참조 지역성의 원리를 잘 이해하고 코드에 적용하면, 대규모 데이터 처리 시스템에서 성능을 극대화할 수 있다.
