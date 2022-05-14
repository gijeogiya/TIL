# Vue를 활용한 SPA 구성

## 느낀점

axios & API호출로 모든 영화 목록을 state로 관리하고, 나는 WatchListView를 맡아 사용자가 나중에 보고 싶은 영화를 추가하고, 보관하는 기능을 구현했다.

Driver, Navigater가 아닌 처음으로 branch를 사용하여 협업 했다. 서로의 진행상황을 commit으로 확인 할 수 있었다. 때문에 commit message의 중요성을 깨달았다.

새로운 언어에 미숙하다보니 알고리즘적인 요소를 구현하는 것이 어려웠습니다. 단순히 랜덤한 무언가를 선택하는 것도 필요한 함수, state, component 들을 가져와야 한다는 것에 낯섬을 느꼈다.

명세서를 팀원과 함께 살펴보고 업무를 분담하며, 유기적으로 얽힌 부분들을 나누는 것은 쉽지 않았다. 그렇기 때문에 기획단계에서의 설계가 매우 중요하다는 것을 알게되었다.

서로 기능을 분담해서 작업하기로 했고, 예상보다 기능이 빨리 구현됐거나 혹은 문제가 발생하면 서로 부담없이 소통을 진행했기 때문에 동시다발적인 작업이 진행돼도 함께 하는 기분이 들 수 있어서 좋았다. 그리고 함께 진행한 만큼 작업도 빨리 끝낼 수 있어서 효율적이었다.



## 1. HomeView

### 어려웠던 점

- MovieCard.vue 와 연결시키는 것이 어려웠다.
- axios, API를 이용하여 데이터를 가져오는 것이 어려웠다.



### 해결방안

- axios, api를 활용하여 영화 데이터들을 가져왔다.

```js
loadMovieCards: function ({ commit }) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
        }
      })
        .then((res) => {
          commit('LOAD_MOVIE_CARDS', res.data.results)
        })
    }
```



## 2. RamdomView

### 어려웠던 점

- lodash를 바로 적용이 안되어 어려움이 있었다.
- RandomView를 구현하기 위해 작성 중 이었다. store.mutations에서 lodash로 하나의 영화를 무작위로 뽑는 알고리즘을 작성했음에도 출력이 안돼서 단계별로 문제가 발생하는 구간을 찾아 헤맸는데, 컴포넌트에서 store 작성된 action을 호출하는 코드를 작성하지 않아서 문제가 있었다. (mapActions 이슈)



### 해결방안

- view.py 파일에서 while문, if문, random함수를 활용하여 적합한 recommended_movies를 만들었다.
- 빼먹은 method 부분을 추가해주었다.

```js
LOAD_RANDOM_MOVIE(state, movieCards) {
      state.pickedMovie = _.sample(movieCards)
    }
```

```js
  methods: {
    ...mapActions(['loadRandomMovie'])
```



## 3. Git Merge

### 어려웠던 점

- 네비게이터와 드라이버 역할을 구분하지 않고, 각자 맡은 기능을 동시다발적으로 수행하기위해 깃브랜치로 프로젝트를 진행했다. 나와 파트너 둘 다 깃브랜치로 프로젝트를 진행한 경험이 없어서 문제 해결을 위해 어느 정도 삽질이 필요했다.



### 해결방안

- conflict가 나는 상황을 익숙하게 받아들이게 됐고, 상대가 브랜치 머지한 것을 풀 받을때 conflict가 나면 당황하지 않고, VSCode에서 수정하라는 곳만 수정하면 해결할 수 있었다.

