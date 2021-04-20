# UDP message 송수신 프로그램

# 서버
# 클라이언트로부터 “send [mboxID] message” 메시지 수신 시, 
# 해당 [mboxID]에 message를 저장하고, “OK”를 클라이언트로 전송
# 클라이언트로부터 “receive [mboxID]” 메시지 수신 시, 
# 해당 [mboxID]의 제일 앞에 있는 메시지를 클라이언트로 전송한 후 삭제
# 클라이언트로부터 “quit” 메시지 수신 시, 프로그램 종료

from socket import *

BUF_SIZE = 1024
port = 3333

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
res = {}

while True:
    # UDP 프로토콜은 데이터 수신 시 연결을 따로 하지 않기 때문에,
    # 다시 돌려줄 클라이언트의 addr이 꼭 필요함
    data, addr = sock.recvfrom(BUF_SIZE)
    msg = data.decode()
    temp = msg.split()
    box_id, message = temp[1], temp[2:]
    print(temp)     # 확인용

    # 클라이언트로부터 “quit” 메시지 수신 시, 프로그램 종료
    if msg == 'quit':
            break

    if temp[0] == 'send':
        # box_id 가 이미 존재하면, 그 박스에 메시지 추가
        if box_id in res:
            res[box_id].append(message)
        else:
            res[box_id] = [message]

        # 메시지 수신 후 OK 전송
        sock.sendto(b'OK', addr)
        # print(res)
    elif temp[0] == 'receive':
        # box_id 가 존재하지 않을 때
        if box_id not in res:
            sock.sendto(b'No messages', addr)
        else:
            # 리스트 요소들을 하나의 문자열로 표현하기 위함
            # 제일 앞의 요소를 처리
            msg2 = " ".join(res[box_id][0])
            sock.sendto(msg2.encode(), addr)

            # 메시지 전송 후 삭제
            if len(res[box_id]) == 1:
                del res[box_id]
            elif len(res[box_id]) > 1:
                del res[box_id][0]
            else:
                sock.sendto(b'No messages', addr)
            # print(res)

sock.close()    
    
    

