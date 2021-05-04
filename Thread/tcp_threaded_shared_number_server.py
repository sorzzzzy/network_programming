# 공유 자원을 사용하는 프로그램 : 서버
#   -> 클라이언트 접속 시, 별도 스레드를 생성하여 처리함
#   -> 스레드 내에서 공유자원(sharedData)을 1씩 10,000,000번 증가시킴

from socket import *
import threading

port = 2500 
BUFSIZE = 1024

# 공유 데이터 초기화
sharedData = 0

# 공유 데이터를 증가시키는 함수
def thread_handler(sock):
    global sharedData
    for _ in range(10000000):
        sharedData += 1 
    print(sharedData) 
    sock.send(str(sharedData).encode()) 
    sock.close()

# 소켓 생성
s = socket(AF_INET, SOCK_STREAM) 
s.bind(('', port))
s.listen(5)

# 스레드 생성
while True:
    client, addr = s.accept()
    print('connected by', addr)
    th = threading.Thread(target=thread_handler, args=(client,)) 
    th.start()

s.close()