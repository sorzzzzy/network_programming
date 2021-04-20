# 서버-클라이언트 통합 UDP 프로그램
# 실행 인수에 따라 서버와 클라이언트 기능을 모두 수행할 수 있는 프로그램
# 프로그램을 실행할 때 ‘c’ 또는 ‘s’ 인수를 지정하면 각각 Client 또는 Server 함수가 실행됨
#   -> 예) 클라이언트 실행: py udp_total.py c, 서버: py udp_total.py s

import argparse, socket, random 
from datetime import datetime

BUFF_SIZE = 1024

# 서버 함수
# 서버는 클라이언트로부터 받은 메시지의 바이트 수를 계산하여 응답 
# 서버는 일정 비율(prob)에 따라 메시지에 대한 응답을 보내지 않을 수 있음
def Server(ipaddr, port): # 서버 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.bind((ipaddr, port))
    print('Waiting in {}...'.format(sock.getsockname())) 
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() < prob:  # 확률에 따라 보낼건지, 아닌지 결정
            print('Message from {} is lost.'.format(addr))
            continue
        print('{} client message {!r}'.format(addr, data.decode()))
        text = 'The length is {} bytes.'.format(len(data))
        sock.sendto(text.encode(), addr)

# 클라이언트 함수
# 클라이언트는 현재 시각을 count 개수만큼 서버로 전송 
# 서버의 응답이 없을 경우 재전송
#   -> 재전송 타임아웃 시간(time)은 0.1로 시작하여 손실 발생 시 2배로 증가(최대 2.0)
def Client(hostname, port): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    index=1 #보낸 메시지 번호 
    time = 0.1 # seconds
    while True:
        data = str(datetime.now())  # 현재 시간을 문자열로 변환
        sock.sendto(data.encode(), (hostname, port)) 
        print('({}) Waiting for {} sec'.format(index, time)) 
        sock.settimeout(time)   # 타임아웃 설정
        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except socket.timeout:
            time *= 2
            if time > 2.0:
                print('{}th packet is lost'.format(index)) 
                if index >= sending_counts:
                    break
                index += 1
                time = 0.1 
            else:
                print('Server reply: {!r}'.format(data.decode())) 
                if index >= sending_counts:
                    break
                index += 1
                time = 0.1

if __name__ == '__main__':
    mode = {'c': Client, 's': Server}   # 딕셔너리 생성
    parser = argparse.ArgumentParser(description='Send and receive UDP packets with setting drop probability')
    
    # 필수
    parser.add_argument('role', choices=mode, help='which role to take between server and client') 
    
    # 옵션
    parser.add_argument('-s', default='localhost', help='server that client sends to') 
    parser.add_argument('-p', type=int, default=2500, help='UDP port (default:2500)') 
    parser.add_argument('-prob', type=float, default=0, help='dropping probability (0~1)') 
    parser.add_argument('-count', type=int, default=10, help='number of sending packets')
    
    args = parser.parse_args()
    prob = args.prob
    sending_counts = args.count
    
    if args.role == 'c':
        mode[args.role](args.s, args.p) 
    else:
        mode[args.role]('', args.p)
