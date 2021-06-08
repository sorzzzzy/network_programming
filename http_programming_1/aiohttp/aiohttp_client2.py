import aiohttp
import asyncio

async def main():
    # 세션을 만들지 않아도 됨
    async with aiohttp.request('GET', 'http://python.org/') as rsp:
        print(rsp.status)
        print(rsp.headers)
        print(await rsp.text())

loop = asyncio.get_event_loop() 
loop.run_until_complete(main())