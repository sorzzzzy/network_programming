# 2개의 IoT 디바이스로부터 데이터 수집하기

# 2개의 IoT 디바이스와 TCP 연결
# 수집한 데이터는 시간정보를 추가하여 파일에 저장 (파일이름: data.txt)


from socket import *
import time

BUF_SIZE = 1024
LENGTH = 20

while True:
    user_input = input()

    # 디바이스 1 소켓
    device1_socket = socket(AF_INET, SOCK_STREAM)
    device1_socket.connect(('localhost', 7777))

    # 디바이스 2 소켓
    device2_socket = socket(AF_INET, SOCK_STREAM)
    device2_socket.connect(('localhost', 9999))
    
    # 사용자가 ‘1’을 입력하면 ‘디바이스 1’로 ‘Request’ 메시지를 전송하여 데이터 수집
    if user_input == '1':

        device1_socket.send(b'Request')
        msg = device1_socket.recv(BUF_SIZE)

        temp, humid, illum = msg.decode().split('/')
        now = time.strftime('%c', time.localtime(time.time()))
        string = now + f': Device1: Temp={temp}, Humid={humid}, Illum={illum}\n'
        print(string)

        # 파일 쓰기
        f = open('data.txt', 'a')
        f.write(string)
        f.close()

    # 사용자가 ‘2’를 입력하면 ‘디바이스 2’로 ‘Request’ 메시지를 전송하여 데이터 수집
    elif user_input == '2':
        device2_socket.send(b'Request')
        msg = device2_socket.recv(BUF_SIZE)

        heartbeat, steps, cal = msg.decode().split('/')
        now = time.strftime('%c', time.localtime(time.time()))
        string = now + f': Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n'
        print(string)

        # 파일 쓰기
        f = open('data.txt', 'a')
        f.write(string)
        f.close()

    # 사용자가 ‘quit’을 입력하면 ‘디바이스 1’, ‘디바이스 2’로 ‘quit’ 메시지를 전송 후 종료
    elif user_input == 'quit':
        device1_socket.send(b'quit')
        device2_socket.send(b'quit')
        break
