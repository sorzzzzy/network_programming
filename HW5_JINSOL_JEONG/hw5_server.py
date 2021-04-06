from socket import *

port = 3333
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)
conn, (remotehost, remoteport) = sock.accept()
print("connected by", remotehost, remoteport)

while True:
    try:
        data = conn.recv(BUFSIZE)   # client로부터 계산식을 받음
    except:
        break
    else:
        if not data:
            break
        res = data.decode()
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
        conn.send(str(cal_res).encode())
    except:
        conn.send(b'ERROR')
        break

conn.close()