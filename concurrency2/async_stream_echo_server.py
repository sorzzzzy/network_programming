import asyncio

port = 2500
BUFSIZE = 1024

# 함수가 시작되면서 자동으로 reader, writer을 넘겨받는데 우리가 신경 쓸 필요는 없음
async def handle_echo(reader, writer):  
    while True:
        # 데이터 읽기(코루틴 함수이므로 await 사용)
        data = await reader.read(BUFSIZE)
        addr = writer.get_extra_info('peername') 
        print(f'Received {data.decode()!r} from {addr!r}')

        # 데이터 쓰기
        # writer 쓸 때는 반드시 writer.drain()을 써야함
        writer.write(data)
        await writer.drain() 
        print(f'Send: {data.decode()!r}')

async def main():
    # 연결을 기다림
    # 소켓은 이 안에서 만들어짐(고수준)
    server = await asyncio.start_server(handle_echo, '', port)
    
    # 소켓의 정보를 알기 위함
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
   
    # serve_forever() 를 호출하면 연결 수락을 시작함
    await server.serve_forever()

asyncio.run(main())