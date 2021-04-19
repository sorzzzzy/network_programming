# 클라이언트로부터 1~10까지의 숫자를 받으면 영어로 변환하여 전송

from socket import *

table = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five',\
        '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten'}

port = 3333
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)
print('waiting...')

while True:
    conn, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        try:
            res = table[data.decode()]
        except:
            conn.send(b'Try again.')
        else:
            conn.send(res.encode())
    
    conn.close()