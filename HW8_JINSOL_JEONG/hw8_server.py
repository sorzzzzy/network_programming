from socket import *

BUF_SIZE = 1024
port = 3333

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
res = {}

while True:
    data, addr = sock.recvfrom(BUF_SIZE)
    msg = data.decode()
    temp = msg.split()
    box_id, message = temp[1], temp[2:]

    # print(temp)

    if msg == 'quit':
            break

    if temp[0] == 'send':
        if box_id in res:
            res[box_id].append(message)
        else:
            res[box_id] = [message]

        sock.sendto(b'OK', addr)
        # print(res)
    elif temp[0] == 'receive':
        if box_id not in res:
            sock.sendto(b'No messages', addr)
        else:
            msg2 = " ".join(res[box_id][0])
            sock.sendto(msg2.encode(), addr)
            if len(res[box_id]) == 1:
                del res[box_id]
            elif len(res[box_id]) > 1:
                del res[box_id][0]
            else:
                sock.sendto(b'No messages', addr)
            # print(res)

sock.close()    
    
    

