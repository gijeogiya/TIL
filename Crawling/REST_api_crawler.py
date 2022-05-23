import json
import requests
from tqdm import tqdm  # 진행 상태를 알려주는 모듈


def tmdb_movie_crawling():
    result = []
    pk_cnt = 1  # pk 값
    for page_cnt in tqdm(range(1, 61)):
        # 유명 영화 페이지당 20개 씩 요청
        url = f'https://api.themoviedb.org/3/movie/popular?api_key=<<api_key>>&language=ko-KR&page={page_cnt}'
        response = requests.get(url)
        datas = response.json()
        for data in datas['results']:
            # 불완전한 데이터 필터링
            if ('overview' in data) and ('genre_ids' in data) and ('poster_path' in data) and ('adult' in data) and ('release_date' in data) and ('original_title' in data) and ('original_language' in data) and ('title' in data) and ('popularity' in data) and ('vote_count' in data) and ('vote_average' in data):
                if len(data['overview']) != 0 and len(data['genre_ids']) != 0 and len(data['poster_path']) != 0 and len(data['release_date']) == 10 and len(data['original_title']) != 0 and len(data['original_language']) != 0 and len(data['title']) != 0 and data['popularity'] != 0 and data['vote_count'] != 0 and data['vote_average'] != 0:
                    result.append({'model': 'movies.movie',
                                   'pk': pk_cnt,
                                   'fields': {'genre_ids': data['genre_ids'],
                                              'poster_path': data['poster_path'],
                                              'adult': data['adult'],
                                              'overview': data['overview'],
                                              'release_date': data['release_date'],
                                              'original_title': data['original_title'],
                                              'original_language': data['original_language'],
                                              'title': data['title'],
                                              'popularity': data['popularity'],
                                              'vote_count': data['vote_count'],
                                              'vote_average': data['vote_average'],
                                              },
                                   })
                    pk_cnt += 1  # 데이터가 정상적으로 저장 되면 pk 값 1 올림

    with open('./popular_movie_data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    return result


tmdb_movie_crawling()
