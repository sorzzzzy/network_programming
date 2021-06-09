import threading
from socket import *
import random
from time import sleep

BUF_SIZE = 1024

# 서버 소켓 생성
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(10)

conn, addr = sock.accept()
msg = conn.recv(BUF_SIZE)
if not msg:
    conn.close()
    
# 수신한 메시지가 register라면
elif msg == b'Register':
    print('Message : ', addr, msg.decode())
    while True:
        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)

        conn.send(f'{heartbeat}/{steps}/{cal}'.encode())
        sleep(5)