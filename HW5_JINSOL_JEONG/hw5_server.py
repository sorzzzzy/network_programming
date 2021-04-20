# TCP 계산기 서버
#   -> 클라이언트로부터 계산식을 수신한 후, 결과를 반환

from socket import *

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

conn, addr = sock.accept()
print("connected by", addr)

while True:
    try:
        data = conn.recv(BUFSIZE)   # client로부터 계산식을 받음
    except:
        break
    else:
        # 데이터를 수신할 때 꼭 필요한 예외처리
        if not data:
            break
        res = data.decode()

        # 공백을 기준으로 분리
        res_list = res.split()

        num1 = int(res_list[0])
        num2 = int(res_list[2])

        if res_list[1] == '+':
            cal_res = num1 + num2
        elif res_list[1] == '-':
            cal_res = num1 - num2
        elif res_list[1] == '*':
            cal_res = num1 * num2
        elif res_list[1] == '/':
            cal_res = num1 / num2

    try:
        # 문자열로 변환 후 전송
        conn.send(str(cal_res).encode())
    except:
        conn.send(b'ERROR')
        break

conn.close()