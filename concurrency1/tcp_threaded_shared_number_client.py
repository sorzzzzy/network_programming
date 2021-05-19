# 공유 자원을 사용하는 프로그램 : 클라이언트
#   -> 서버에 접속 후, 공유자원의 값을 수신하여 출력하는 프로그램

from socket import *

port = 2500
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', port)) 

print(int(s.recv(BUFSIZE).decode())) 
s.close()