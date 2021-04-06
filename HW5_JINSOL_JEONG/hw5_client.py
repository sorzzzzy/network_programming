import socket

address = ("localhost", 3333)
BUFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Input : ")
    if msg == 'q':  
        break
    else:
        try:
            bytesSent = s.send(msg.encode())   
        except:
            print('connection closed')
            break

        try:
            data = s.recv(BUFSIZE)
        except:
            print('connection closed')
            break
        else:
            if not data:
                break
            res = data.decode()
            res = '{:.1f}'.format(float(res))
            print('Result is : ', res)

s.close()