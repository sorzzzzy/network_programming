# 타임 서버
# 클라이언트가 접속하면 현재 시간을 전송하는 프로그램

from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s = bind(('', 9999))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('connection from ', addr)

    # time.time() = 1970년 1월 1일 0시 0분 0초부터의 경과시간을 나타냄
    # time.ctime() = 초 단위의 시간을 문자열로 변환하는 함수
    #   -> ex) 'Thu Mar 4 09:43:07 2021
    conn.send(time.ctime(time.time()).encode())
    conn.close()