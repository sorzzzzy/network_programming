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
    # create_task로 동시에 돌리고 싶은 태스크들을 생성함
    task1 = asyncio.create_task(add(1, 2)) 
    task2 = asyncio.create_task(mul(3, 4))

    # gather 사용 시 모아서 실행시킬 수 있음
    await asyncio.gather(task1, task2)
    print(f"finished at {time.strtime('%X')}")

# 이벤트 루프 얻기, 코루틴 실행, 이벤트 루프 종료 세 가지를 한 번에 처리 가능
'''
loop = asyncio.get_event_loop()     
loop.run_until_complete(main())    
loop.close()
'''
asyncio.run(main())
