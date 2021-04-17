import socket
import cv2
import numpy as np

BUF_SIZE = 8192
LENGTH = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5000))

while True:
    sock.send(b'start')

    rx_size = 0
    data = b''
    while rx_size < LENGTH:
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf:
            break
        data = data + rx_buf
        rx_size += len(rx_buf)
    
    # 한번 더 체크 (위의 while문에서 break로 중간에 나올 수 있기 때문)
    if rx_size < LENGTH
        break

    frame_len = int(data)

    # 실제 이미지를 보내달라고 요청
    sock.send(b'image')

    rx_size = 0
    byteData = b''

    # 실제 이미지 수신
    # 한번에 바로 받아도 되지만, 그렇게 하면 못받는 경우가 생길 수도 있음
    while rx_size < frame_len:     
        rx_buf = sock.recv(BUF_SIZE)
        if not rx_buf
            break
        byteData= byteData + rx_buf
        rx_size += len(rx_buf)
    
    # 한번 더 체크
    if rx_size < frame_len:     
        break

    data = np.frombuffer(byteData, dtype = 'uint8')
    imgDecode = cv2.imdecode(data,1)
    cv2.imshow('image', imgDecode)

    # q를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()