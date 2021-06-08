# select()를 이용한 에코 서버

import socket, select

socks=[]    # 소켓 리스트, 이 리스트를 가지고 select를 호출할 것임 
BUFFER = 1024
PORT = 2500

# 서버 소켓 만들기
s_sock = socket.socket()    # TCP 소켓
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)    # 소켓 리스트에 서버 소켓을 추가
print(str(PORT) + '에서 접속 대기 중')

while True:
    # 읽기 이벤트(연결요청 및 데이터 수신) 대기
    # 메시지 수신(읽기)만 체크할 것이기 때문에, 쓰기와 예외는 비워둠
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    # 소켓 요청이 하나만 있지 않을수도 있기 때문에(=여러개 일 수도 있으므로)
    # 리스트로 받아서 체크해야함
    for s in r_sock:    # 수신(읽기 가능한) 소켓 리스트 검사
        # 서버소켓이라면, (새로운 클라이언트의 연결 요청이 있다는 뜻)
        if s == s_sock:     
            c_sock, addr = s_sock.accept()
            # 연결된 클라이언트 소켓을 소켓 리스트에 추가한 뒤 출력
            socks.append(c_sock)    
            print('Client ({}) connected'.format(addr))
        # 기존 클라이언트의 데이터 수신 이벤트 발생
        else:   
            data = s.recv(BUFFER) 
            if not data:
                s.close()
                # 연결 종료된 클라이언트 소켓을 소켓 리스트에서 제거
                socks.remove(s)     
                continue
            print('Received:', data.decode())
            s.send(data)

