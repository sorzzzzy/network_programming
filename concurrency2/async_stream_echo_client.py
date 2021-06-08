import asyncio 

port = 2500
BUFSIZE = 1024

async def main():
    # asyncio.open_connection()을 통해 서버에 연결
    reader, writer = await asyncio.open_connection('localhost', port)
    
    while True:
        data = input('Enter the message to send: ') 
        writer.write(data.encode())
        await writer.drain()
        
        data = await reader.read(BUFSIZE)
        print('Received:', data.decode())

asyncio.run(main())