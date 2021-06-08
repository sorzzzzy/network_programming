import asyncio, time

async def add(a, b): 
    print('In add() func') 
    await asyncio.sleep(1) 
    print(a + b)

async def mul(a, b):
    print('In mul() func')
    await asyncio.sleep(2)
    print(a * b)

async def main():
    print(f"started at {time.strftime('%X')}")
    # 코루틴 내에서 코루틴으로 태스크를 생성 후 태스크를 실행
    # create_task 라는 함수가 있음
    task1 = asyncio.create_task(add(1,2))
    task2 = asyncio.create_task(mul(3,4))
    # 코루틴 함수가 아니라, 위에서 만든 태스크를 await함
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}" 
)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()