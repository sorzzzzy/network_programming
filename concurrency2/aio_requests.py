# 2개의 사이트를 번갈아 가면서 총 160번 웹 페이지 요청/응답 수신
# 비동기I/O 사용 -> 스레드 하나임 -> OS가 관리하는 것이 아니라, 각각이 함수로 관리됨

import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.create_task(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__": 
    sites = [
        "https://homepage.sch.ac.kr",
        "https://www.google.co.kr",
    ] * 80

    start_time = time.time() 
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites)) 
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")