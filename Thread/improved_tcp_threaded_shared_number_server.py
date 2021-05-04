from socket import *
import threading

port = 2500
BUFSIZE = 1024

sharedData = 0

def thread_handler(sock):
    global sharedData, lock 

    # 임계영역 보호
    lock.acquire() 
    for _ in range(10000000):
            sharedData += 1
    lock.release()

    print(sharedData)
    sock.send(str(sharedData).encode())
    sock.close()

s = socket(AF_INET, SOCK_STREAM) 
s.bind(('', port))
s.listen(5)

# Lock 클래스를 사용해 객체 생성
lock = threading.Lock()

while True:
    client, addr = s.accept()
    print('connected by', addr)
    th = threading.Thread(target=thread_handler, args=(client,)) 
    th.start()

s.close()