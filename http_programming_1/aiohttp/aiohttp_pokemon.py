# aiohttp 사용

import aiohttp
import asyncio
import time

async def get_pokemon(session, url):
    async with session.get(url) as rsp:
        pokemon = await rsp.json()
        return pokemon['name']

async def main():
    # 세션을 만듬
    async with aiohttp.ClientSession() as session:
        # 테스크 리스트를 만듬
        tasks = []
        for number in range(1, 11):
            url = f'https://pokeapi.co/api/v2/pokemon/{number}' 
            # 테스크에 추가
            tasks.append(asyncio.create_task(get_pokemon(session, url)))
        
        # 리스트를 넘겨받을 때 '*' 필요
        original_pokemon = await asyncio.gather(*tasks) 
        for pokemon in original_pokemon:
            print(pokemon)

start_time = time.time()
loop = asyncio.get_event_loop() 
loop.run_until_complete(main())
print("--- %s seconds ---" % (time.time() - start_time))