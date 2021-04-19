# 에코 클라이언트
# 서버로 메시지를 전송하고, 수신 메시지를 출력
# UDP 프로토콜은 connect()와 같은 연결이 없음

from socket import *

port = 2500
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input("Enter a message : ")
    if msg == 'q'
        break
    
    # 보낼 때 또한 주소 명시
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUF_SIZE)
    print("Server says : ", data.decode())

sock.close() 