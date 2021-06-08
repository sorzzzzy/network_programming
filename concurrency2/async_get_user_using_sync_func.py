'''
코루틴 내 블로킹 함수 사용하기
loop.run_in_executor(None, func, *args)
    - None : 기본 executor 선택
    - fucn : 실행할 함수
    - args : 함수 인자 리스트
'''
import asyncio, time

async def get_user(name):
    print('사용자 {!r} 정보 조회중...'.format(name)) 
    await loop.run_in_executor(None, time.sleep, 1) 
    print('사용자 {!r} 정보 조회 완료!'.format(name))

async def main():
    start = time.time()
    await asyncio.gather(get_user('Jeon'),
        get_user('Yun'),
        get_user('Kim'),
        get_user('Song'))
    end = time.time()
    print(f'총 소요시간: {end - start}')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()