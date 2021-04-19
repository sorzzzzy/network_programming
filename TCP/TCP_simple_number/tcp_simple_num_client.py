# 1~10까지의 숫자를 서버로 전송하고, 응답을 받으면 출력
# 'q'를 입력하면, 클라이언트 종료

from socket import *

port = 3333
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', port))

while True:
    msg = input('Number to send : ')
    if msg == 'q':
        break
    s.send(msg.encode())
    
    data = s.recv(1024)
    if not data:
        break

    print('Received message : ', data.decode())

s.close()