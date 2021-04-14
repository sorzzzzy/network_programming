from socket import *
import random

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
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

        heartbeat = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)

        conn.send(f'{heartbeat}/{steps}/{cal}'.encode())