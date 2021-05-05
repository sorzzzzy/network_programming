# TCP를 이용한 단체 채팅 프로그램 만들기(단체 채팅 프로그램) : 서버
#   -> 채팅 서버는 수신한 메시지를 발신자를 제외한 다른 클라이언트에게 전송
#   -> 새로운 클라이언트가 들어오면, 클라이언트 목록에 저장
#   -> 채팅 클라이언트가 ‘quit’를 전송하면 해당 클라이언트를 목록에서 삭제

from socket import *
import time
import threading

clients = [] # 클라이언트 목록 리스트 생성
port = 2500

def sendTask(conn, addr):
    while True:
        data = conn.recv(1024)

        # 받은 메시지 안에 'quit'이 들어있다면
        if 'quit' in data.decode():
            # 'quit'을 보낸 주소가 클라이언트 목록에 있다면
            if conn in clients:
                print(addr, 'exited')
                # 해당 클라이언트를 목록에서 삭제
                clients.remove(conn)
                continue
        else:
            print(time.asctime() + str(addr) + ':' + data.decode())
            # 클라이언트들에게 메시지 전송
            for client in clients:
                # 메시지를 보낸 client를 제외한 나머지에게 전송
                if client != conn:
                    client.send(data)

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)

print('Server Started')

while True:
    conn, addr = s.accept()

    # 새로운 클라이언트이면 목록에 추가
    if conn not in clients:
            print('new client', addr)
            clients.append(conn)

    th = threading.Thread(target=sendTask, args=(conn, addr, ))
    th.start()
    

s.close()
    

    
 