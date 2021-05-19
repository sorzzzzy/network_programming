# 멀티스레드 에코 서버 : threading.Thread 클래스
#   -> 특정 클라이언트로부터 메시지를 받고, 응답하는 부분을 별도 스레드로 구현
#   -> 메인 스레드는 클라이언트로부터 연결요청을 받은 후, 새로운 스레드를 생성하는 역할을 수행

from socket import *
import threading

port = 2500
BUFSIZE = 1024

# 하나의 별도의 함수로 만듬
# 클라이언트와 통신할 스레드를 만들기 때문에 소켓을 인자로 받음

def echoTask(sock): 
    while True:
        data = sock.recv(BUFSIZE)
        if not data:
            break
        print('Received message:', data.decode()) 
        # echo 이기 때문에 받은 것을 다시 돌려줌 다시 돌려줌
        sock.send(data)
    
    sock.close()

sock = socket(AF_INET, SOCK_STREAM) 
sock.bind(('', port)) 
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept() 
    print('connected by', remotehost, remoteport)
    
    # 인자로 소켓을 넘겨줌
    th = threading.Thread(target=echoTask, args=(conn,)) 
    th.start()