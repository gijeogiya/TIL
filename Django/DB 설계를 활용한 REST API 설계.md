# DB 설계를 활용한 REST API 설계

2022.04.22

## 느낀점

django의 MCV패턴 속에 기능들이 더 해질 수록 코드가 헤비해 질 줄 알았다. 하지만 django가 지원하는 Django Rest Framework를 이용하니 코드 자체는 비교적 양이 적어졌다. 하지만 너무 덜어낸 나머지 그 기능을 눈으로 파악하기는 힘들었고 커스텀이 힘들었다. 이것이 프레임워크의 장점이자 단점인 것 같다. 1:N, N:M의 DB를 사용하니 세상의 많은 데이터 관계를 다시한번 생각하게 되었고 이것을 잘 정리하여 유용한 API를 만들어 배포한다면 수익 창출이 가능 하지 않을까 하는 생각을 했다.



## 1. Rest Framework를 활용한 API 서버 구성

### 어려웠던 점

- 모델링과 Data Load의 선후관계가 헷갈렸다.

- 설계 없이 바로 코드로 URL을 구성하려니 힘들었다.

- View에서 서브 class의 동작 원리가 헷갈렸다.

- 아래 부분의 read_only 부분의 기능과 역할이 헷갈렸다.  serializer에서 Movie를 찾을 수 없다는 에러가 발생한 부분의 코드는 아래와 같다.

  ```python
  class ReviewSerializer(serializers.ModelSerializer):
   
      class MovieListSerializer(serializers.ModelSerializer):
          
          class Meta:
              model = Movie
              fields = ('title', )
  
      movie = MovieListSerializer(many=True)
  
      class Meta:
          model = Review
          fields = ('id', 'movie', 'title', 'content', )
  ```
  
  

### 해결방안

- Data Load는 데이터 구성에 알맞게 모델링을 모두 끝내야 받아올 수 있었다.

- URL 코드를 짜기전에 Model과 View와 더불어 기능을 간단하게 다이어그램으로 그려봐도 좋을 것 같다.

- 다른  class field에서 필요한 것은 서블 class로 불러와서 작동시키면 된다.

- read, write 둘 다 하려는 부분은 아무것도 적지 않아도 되지만 읽기만 할 때는 read_only를 설정해 주어야 한다. 해결 후 코드는 아래와 같다.

  ```python
  class ReviewSerializer(serializers.ModelSerializer):
   
      class MovieListSerializer(serializers.ModelSerializer):
          
          class Meta:
              model = Movie
              fields = ('title', )
  	
  	# read_only를 추가해야 했다
      movies = MovieListSerializer(many=True, read_only=True)
  
      class Meta:
          model = Review
          fields = ('id', 'movies', 'title', 'content', )
          # 작동되게 추가
          read_only_fields = ('movies', )
  ```

  





## 2. Postman을 활용해 완성한 API 작동해보기

### 어려웠던 점

- movie_id를 받아오지 못해 처음 오류가 났다.

### 해결방안

- 아래와 같이 view의 create_view 함수를 구성해 주었다.

  ```python
  @api_view(['POST'])
  def create_review(request, movie_pk):
      movie = get_object_or_404(Movie, pk=movie_pk)
      serializer = ReviewSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(movie=movie)
          return Response(serializer.data)
  ```

  
