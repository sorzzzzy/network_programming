# 간단한 웹 서버 프로그램

# 클라이언트로부터 HTTP 요청이 들어오면, 해당 요청에 따라 자원을 전송해주는 웹 서버 구현
# 웹 서버에서 처리 가능한 자원은 'index.html'
#   -> 웹 브라우저는 'index.html' 파일을 참조하여 'iot.png'를 추가 요청 
#   -> 웹 브라우저 자체적으로 'favicon.ico' 파일을 요청할 수 있음
# 'http://127.0.0.1/index.html'만 처리 가능하다고 가정

from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    # req[0] = GET /index.html HTTP/1.1
    # req[0].split() = ['GET', '/index.html', 'HTTP/1.1']
    # req[0].split()[1] = /index.html 
    # req[0].split()[1].replace('/', '') = index.html
    # '/'를 제거하고 최종 파일 이름을 얻음
    filename = req[0].split()[1].replace('/', '')

    if filename == 'index.html':
        # html 파일에 대한 mimeType 설정
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        # html 파일이 존재하는 경우, HTTP Response 메시지를 다음과 같이 생성하여 전송
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        data = f.read()
        c.send(data.encode('euc-kr', 'ignore'))
    elif filename == 'iot.png':
        # png 파일에 대한 mimeType 설정
        f = open(filename, 'rb')
        mimeType = 'image/png'
        # png 파일이 존재하는 경우, HTTP Response 메시지를 다음과 같이 생성하여 전송
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        data = f.read()
        c.send(data)
    elif filename == 'favicon.ico':
        # ico 파일에 대한 mimeType 설정
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        # ico 파일이 존재하는 경우, HTTP Response 메시지를 다음과 같이 생성하여 전송
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        data = f.read()
        c.send(data)
    else:
        # 해당 파일이 존재하지 않는 경우, HTTP Response 메시지를 다음과 같이 생성하여 전송
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close()
