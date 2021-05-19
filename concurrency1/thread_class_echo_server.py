# 멀티스레드 에코 서버 : Thread의 파생 클래스 이용
#   -> 특정 클라이언트로부터 메시지를 받고, 응답하는 부분을 별도 스레드로 구현
#   -> 메인 스레드는 클라이언트로부터 연결요청을 받은 후, 새로운 스레드를 생성하는 역할을 수행

from socket import *
import threading

port = 2500
BUFSIZE = 1024

# threading.Thread 클래스 상속받기
class ClientThread(threading.Thread): 
    def __init__(self, sock):
        threading.Thread.__init__(self)
        # 소켓 초기화
        self.sock = sock
    
    def run(self):
        while True:
            data = self.sock.recv(BUFSIZE) 
            if not data:
                break
            print('Received message:', data.decode()) 
            self.sock.send(data)
        
        self.sock.close()

sock = socket(AF_INET, SOCK_STREAM) 
sock.bind(('', port)) 
sock.listen(5)

while True:
    conn, (remotehost, remoteport) = sock.accept() 
    print('connected by', remotehost, remoteport) 
    th = ClientThread(conn)
    th.start()