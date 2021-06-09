from socket import *
import time
import selectors

BUF_SIZE = 1024
LENGTH = 20

def device1(conn, mask):
    msg = conn.recv(BUF_SIZE)
    temp, humid, illum = msg.decode().split('/')
    now = time.strftime('%c', time.localtime(time.time()))
    string = now + f': Device1: Temp={temp}, Humid={humid}, Illum={illum}\n'
    print(string)
    f = open('data.txt', 'a')
    f.write(string)
    f.close()

def device2(conn, mask):
    msg = conn.recv(BUF_SIZE)
    heartbeat, steps, cal = msg.decode().split('/')
    now = time.strftime('%c', time.localtime(time.time()))
    string = now + f': Device2: Heartbeat={heartbeat}, Steps={steps}, Cal={cal}\n'
    print(string)
    f = open('data.txt', 'a')
    f.write(string)
    f.close()

# device1 소켓 생성
socket1 = socket(AF_INET, SOCK_STREAM)
socket1.connect(('localhost', 7777))

# device2 소켓 생성
socket2 = socket(AF_INET, SOCK_STREAM)
socket2.connect(('localhost', 9999))

socket1.send(b'Register')
socket2.send(b'Register')

sel = selectors.DefaultSelector()
sel.register(socket1, selectors.EVENT_READ, device1)
sel.register(socket2, selectors.EVENT_READ, device2)

while True:
    # 등록된 객체에 대한 이벤트 감시 시작
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
