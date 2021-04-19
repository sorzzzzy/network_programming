# 에코 서버
# 클라이언트로부터 수신한 데이터를 출력하고, 상대방에게 다시 전송
# 연결 설정이 따로 없으므로, 다수의 사용자와 송수신 가능
#   -> 소켓 하나로 여러 클라이언트와 송수신 가능

from socket import *

port = 2500
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock = bind(('', port))

while True:
    # 메시지를 수신할 때 주소도 함께 받아야 함
    msg, addr = sock.recvfrom(BUF_SIZE)
    print("Received data : ", msg.decode())

    # 그대로 돌려주기
    # 연결설정을 따로 안하기 때문에 돌려받을 주소를 명시해주어야 함
    sock.sendto(msg, addr)