# TCP 계산기 클라이언트
#   -> 사용자로부터 “20 + 17” 형태의 계산식을 입력 받음
#   -> 지원 연산: 더하기, 빼기, 곱하기, 나누기(소수점 1자리까지 표시)
#   -> 입력 받은 계산식을 서버로 전송
#   -> 서버로부터 전송 받은 결과를 화면에 출력
#   -> 사용자가 “q”를 입력하면 종료

from socket import *

address = ("localhost", 3333)
BUFSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Input : ")

    # 'q'를 입력하면 종료
    if msg == 'q':  
        break

    # 그게 아니라면,
    else:
        # 계산식을 서버로 전송
        try:
            bytesSent = s.send(msg.encode()) 
        # 예외처리  
        except:
            print('connection closed')
            break

        # 계산 결과를 수신
        try:
            data = s.recv(BUFSIZE)
        except:
            print('connection closed')
            break
        else:
            # 데이터를 수신할 때 꼭 필요한 예외처리
            if not data:
                break
            res = data.decode()
            # 소수점 첫째자리 까지만 표기
            # {:.2f} = 둘째자리, {:.0} = 정수만
            res = '{:.1f}'.format(float(res))
            print('Result is : ', res)

s.close()