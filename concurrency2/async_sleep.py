# 비동기방식
# 1초후에 hello, 2초후에 world를 출력

import asyncio, time

async def say_after(delay, what): 
    await asyncio.sleep(delay) 
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    
    task1 = asyncio.create_task( 
        say_after(1, 'hello'))
    task2 = asyncio.create_task(
        say_after(2, 'world'))

    await task1
    await task2
    
    print(f"finished at {time.strftime('%X')}") 

asyncio.run(main())