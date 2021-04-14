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
    elif msg == b'quit':
        print('client: ', addr, msg.decode())
        conn.close()
        continue
    elif msg == b'Request':
        print('client: ', addr, msg.decode())

        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)

        conn.send(f'{temp}/{humid}/{illum}'.encode())
