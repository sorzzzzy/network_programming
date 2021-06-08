# UDP를 이용한 단체 채팅 프로그램 만들기(단체 채팅 프로그램) : 서버
#   -> 채팅 서버는 수신한 메시지를 발신자를 제외한 다른 클라이언트에게 전송
#   -> 새로운 클라이언트가 들어오면, 클라이언트 목록에 저장
#   -> 채팅 클라이언트가 ‘quit’를 전송하면 해당 클라이언트를 목록에서 삭제

import socket
import time

clients = [] # 클라이언트 목록 리스트 생성

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 2500))

print('Server Started')

while True:
    # 메시지를 기다림
    # UDP는 receive 하면 데이터와 보낸이의 주소가 들어옴
    data, addr = s.recvfrom(1024) 

    # 받은 메시지 안에 'quit'이 들어있다면
    if 'quit' in data.decode():
            # 'quit'을 보낸 주소(=addr)가 클라이언트 목록에 있다면
            if addr in clients:
                print(addr, 'exited')
                # 해당 클라이언트를 리스트 목록에서 삭제
                clients.remove(addr)
                # 계속해서 진행
                continue

    # 새로운 클라이언트이면 목록에 추가
    if addr not in clients:
            print('new client', addr)
            clients.append(addr)
    
    print(time.asctime() + str(addr) + ':' + data.decode())

    # 클라이언트들에게 메시지 전송
    for client in clients:
        # 메시지를 보낸 client를 제외한 나머지에게 전송
        if client != addr:
            # UDP는 메시지를 보낼 때 주소만 있으면 되는데, 
            # 그 주소를 이미 clients 리스트에 저장해놨음
            s.sendto(data, client)
 