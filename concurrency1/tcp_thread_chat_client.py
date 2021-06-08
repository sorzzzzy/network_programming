# 멀티스레드 TCP 채팅 프로그램 만들기: 채팅 클라이언트
# 기존 채팅 프로그램의 문제점 : 한 번씩 번갈아 가면서 채팅을 해야함
#   -> 사용자 입력을 받아 전송하는 부분과, 메시지를 수신하는 부분을 별도 쓰레드로 구현

from socket import * 
import threading

port = 3333
BUFFSIZE = 1024

# 메시지를 수신해서 화면에 출력하는 부분을 스레드로 만듦
# 보내는 부분을 스레드로 만들어도 상관은 없음
def recvTask(sock):
    while True:
        # 받아서 메시지를 계속 출력
        data = sock.recv(BUFFSIZE)
        print('<-', data.decode())

# 소켓 만들고 연결
sock = socket(AF_INET, SOCK_STREAM) 
sock.connect(('localhost', port))

# 수신하는 역할만 하는 스레드를 생성
th = threading.Thread(target=recvTask, args=(sock,)) 
th.start()

# 메인 스레드 : 메시지를 입력받아서 출력하고, 서버로 보내는 부분
while True:
    msg = input()
    print('->', msg)
    sock.send(msg.encode())