# requests 사용

import requests
import time

# 시작시간
start_time = time.time()

for number in range(1, 11):    # 1~10까지
    url = f'https://pokeapi.co/api/v2/pokemon/{number}' 
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))