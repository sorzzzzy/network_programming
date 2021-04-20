# 2개의 IoT 디바이스로부터 데이터 수집하기

# 디바이스 1: 온도, 습도, 조도를 측정 제공
# 사용자로부터 ‘Request’ 메시지를 수신하면 온도, 습도, 조도를 전송
# 사용자로부터 ‘quit’ 메시지를 수신하면 종료

from socket import *
import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue

    # 사용자로부터 ‘quit’ 메시지를 수신하면 종료
    elif msg == b'quit':
        print('client: ', addr, msg.decode())
        conn.close()
        continue

    # 사용자로부터 ‘Request’ 메시지를 수신하면 온도, 습도, 조도를 전송
    elif msg == b'Request':
        print('client: ', addr, msg.decode())

        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)

        conn.send(f'{temp}/{humid}/{illum}'.encode())
