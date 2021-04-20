# 문자열(이름), 정수(학번) 전송하기
# 학생의 이름을 수신한 후 출력
# 학생의 학번(정수형 변수)을 전송하기

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()

    # 클라이언트에게 연결 확인 메시지 보내기
    print('Connection from', addr)
    client.send(b'Hello ' + addr[0].encode())

    # 클라이언트로부터 이름 수신 후 출력
    name = client.recv(1024)
    print(name.decode())

    # 클라이언트에게 학번 보내기
    client.send(b'20171534')

    client.close()