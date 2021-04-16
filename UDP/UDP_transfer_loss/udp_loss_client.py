# 손실 복구 기능을 가진 UDP 클라이언트 프로그램
# 타임아웃이 발생하면, 재전송하고 타임아웃 시간을 2배 씩 증가
#   -> 타임아웃 시간이 2.0보다 커지면 재전송 중단
# socket의 settimeout() 함수 이용
#   -> 블로킹 소켓 연산에 시간제한을 설정

from socket import *

port = 5555
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
    time = 0.1
    data = 'Hello IoT'
    while True:
        sock.sendto(data.encode(), ('localhost', port))
        print('Packet({}): Waiting up to {} secs for ack'.format(i, time)) 
        sock.settimeout(time)

        try:
            # ack을 기다림
            data = sock.recvfrom(BUFSIZE)
        except timeout:     # 30% 확률로 ack이 오지 않을 때
            time *= 2
            if time > 2.0:
                break
        else:
            print('Response', data.decode())
            # break를 만나면 for문으로 돌아가 time을 초기화
            break