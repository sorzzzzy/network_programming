import socket

port = int(input("Port No: "))
address = ("localhost", port)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect(address)

while True:
    msg = input("Message to send: ")
    try:
        # 인코딩해서 전송
        bytesSent = s.send(msg.encode())
    except:
        print('connection closed')
        break 
    else:
        # 전송 내용 출력
        print("{} bytes send".format(bytesSent))

    try:
        # 데이터 받기
        data = s.recv(BUFSIZE)
    except:
        print('connection closed') 
        break
    else:
        if not data:
            break
        print("Received message: %s" %data.decode()) 
s.close()