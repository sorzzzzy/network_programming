# 웹에서 JSON 데이터 수신하기
# 파일에서 JSON 읽기와 동일하게 json.loads() 함수를 사용하여, JSON 문자열을 딕셔너리로 변환

import json
from urllib import request

url = 'https://python.bakyeono.net/data/movies.json' 
text_data = request.urlopen(url).read().decode() 
print(text_data)
print(type(text_data))

movies = json.loads(text_data)
sorted_by_year = sorted(movies,
    key = lambda t: t['year'])

for movie in sorted_by_year: 
    print(movie['year'], movie['title'],
        movie['genre'], movie['starring'])