import asyncio

# 코루틴1
async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1)      # 1초 대기. asyncio.sleep도 네이티브 코루틴 
    return a+b                  # 두 수를 더한 결과 반환

# 코루틴2
async def print_add(a, b):
    # 코루틴2 호출, 그냥 호출하면 안되고 await 사용
    result = await add(a, b)    # await로 다른 네이티브 코루틴 실행하고 반환값을 변수에 저장 
    print('print_add: {0} + {1} = {2}'.format(a, b, result))

loop = asyncio.get_event_loop()     # 이벤트 루프를 얻음 
loop.run_until_complete(print_add(1, 2))    # print_add가 끝날 때까지 이벤트 루프를 실행 
loop.close()