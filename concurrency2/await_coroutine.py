import asyncio, time

# 비동기 함수1
async def add(a, b): 
    print('In add() func') 
    await asyncio.sleep(1) 
    print(a + b)

# 비동기 함수2
async def mul(a, b):
    print('In mul() func')
    await asyncio.sleep(2)
    print(a * b)

async def main():
    print(f"started at {time.strftime('%X')}")
    # 비동기 함수1 호출
    await add(1,2)
    # 비동기 함수2 호출
    # 위의 add가 끝날 때 까지 기다렸다가 실행함
    await mul(3,4)
    print(f"finished at {time.strftime('%X')}" 
)

# 이벤트 루프 생성
loop = asyncio.get_event_loop()
# 메인 함수를 실행해라
loop.run_until_complete(main())
loop.close()