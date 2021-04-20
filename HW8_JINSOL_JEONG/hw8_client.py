# UDP message 송수신 프로그램

from socket import *

port = 3333
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    user_input = input("Enter the message(\"send mboxid message\" or \"receive mboxid\"): ") 
    sock.sendto(user_input.encode(), ('localhost', port))

    if user_input == 'quit':
        break

    data, addr = sock.recvfrom(BUF_SIZE)
    print("Message from server : ", data.decode())

sock.close()