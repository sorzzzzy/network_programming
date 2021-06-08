import aiohttp
import asyncio

async def main():
    # async with를 써서 클라이언트 세션을 만들고,
    async with aiohttp.ClientSession() as session:
        # session.get을 통해 응답을 받아옴
        async with session.get('http://python.org') as rsp: 
            print(rsp.status)
            print(rsp.headers)
            print(await rsp.text())

loop = asyncio.get_event_loop() 
loop.run_until_complete(main())