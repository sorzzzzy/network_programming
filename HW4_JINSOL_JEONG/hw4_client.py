# 문자열(이름), 정수(학번) 전송하기
# 본인의 이름(예:'JINSOL JEONG')을 문자열로 전송하기
# 본인의 학번을 수신한 후 정수로 변환하여 출력

from socket import *

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

# 'Hello + 클라이언트 주소' 수신 후 출력
msg = sock.recv(1024)
print(msg.decode())

# 본인 이름을 문자열로 전송
sock.send(b'JINSOL JEONG')

# 학번 수신 후 출력
num_b = sock.recv(1024)
print(num_b.decode())

sock.close()