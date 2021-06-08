# UDP를 이용한 단체 채팅 프로그램 만들기(단체 채팅 프로그램) : 클라이언트
#   -> 최초 실행 시, ‘ID’를 입력받아 서버로 전송
#   -> 서브 스레드는 채팅 서버로부터 메시지를 수신하여 화면에 출력 
#   -> 메인 스레드는 사용자의 입력을 받아 서버로 전송

import socket
import threading

# 메시지 수신 부분을 별도의 스레드로 만듦
# 수신받아 화면에 출력
def handler(sock): 
    while True:
        msg, addr = sock.recvfrom(1024)
        print(msg.decode())

svr_addr = ('localhost', 2500)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ID 입력받기
my_id = input('ID를 입력하세요: ') 
sock.sendto(('['+my_id+']').encode(), svr_addr)

# 메인 스레드 만들기
th = threading.Thread(target=handler, args=(sock,)) 
# 메인 스레드 종료 시, 서브 스레드도 함께 종료시키기 위함
th.daemon = True
th.start()

# 메시지를 입력받아 보내는 부분
while True:
    msg = '[' + my_id + '] ' + input()
    sock.sendto(msg.encode(), svr_addr)
