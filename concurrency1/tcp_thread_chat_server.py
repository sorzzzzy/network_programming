# 멀티스레드 TCP 채팅 프로그램 만들기 : 채팅 서버
# 기존 채팅 프로그램의 문제점 : 한 번씩 번갈아 가면서 채팅을 해야함
#   -> 사용자 입력을 받아 전송하는 부분과, 메시지를 수신하는 부분을 별도 쓰레드로 구현

from socket import *
import threading

port = 3333
BUFFSIZE = 1024

# 메시지를 입력하는 부분을 별도 스레드로 만듬
def sendTask(sock):
    while True:
        resp = input()
        # 입력받은 메시지를 화면에 출력
        print('->', resp)
        # 입력받은 메시지를 클라이언트로 보냄
        sock.send(resp.encode())

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(1)
# 메인 스레드를 위한 소켓 생성
conn, addr = s.accept()

# 메시지 전송 스레드 생성 : 메시지를 입력받아서 보내는 역할
th = threading.Thread(target=sendTask, args=(conn,)) 
th.start()

# 메인 스레드는 받아서 화면에 출력하는 역할만 수행함
while True:
    data = conn.recv(BUFFSIZE) 
    print('<-', data.decode())