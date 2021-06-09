import threading
from socket import *
from time import sleep
import random

BUF_SIZE = 1024

# 서버 소켓 생성
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)

conn, addr = sock.accept()
msg = conn.recv(BUF_SIZE)
if not msg:
    conn.close()
# 수신한 메시지가 register라면
elif msg == b'Register':
    print('Message : ', addr, msg.decode())
    while True:
        tem = random.randint(0, 40)
        hum = random.randint(0, 100)
        ill = random.randint(70, 150)

        conn.send(f'{tem}/{hum}/{ill}'.encode())
        sleep(3)