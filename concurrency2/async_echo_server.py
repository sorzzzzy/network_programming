# 에코 서버를 비동기적 방식으로 만들기

import asyncio
from socket import *

port = 2500
BUFSIZE = 1024

async def handler(conn, addr):
    while True:
        # 메시지 수신
        # conn.recv 함수의 비동기적 방법을 몰라도 
        # loop.run_in_executor을 통해 비동기적으로 사용 가능
        data = await loop.run_in_executor(None, conn.recv, BUFSIZE) 
        if not data:
            break
        print(f'{addr} Received message: ', data.decode()) 
        # 받은 메시지 다시 전송
        conn.send(data)

async def main():
    # 연결을 기다리는 서버소켓 생성
    sock = socket()
    sock.bind(('', port)) 
    sock.listen(5)
    while True:
        # sock.accept를 loop.run_in_executor를 사용하여 비동기 함수로 만듬 
        client, addr = await loop.run_in_executor(None, sock.accept) 
        # accept가 되면 핸들러로 만들어, 태스크로 만든다
        print(addr, 'accepted')
        loop.create_task(handler(client, addr))

loop = asyncio.get_event_loop() 
loop.run_until_complete(main()) 
loop.close()