import socket
import struct
import sys

class DnsClient:
    def __init__(self, domainName):
        self.domainName = domainName
        # DNS Query Header, 쿼리 만들기
        self.TransactionId = 1  # 아무 숫자든 괜찮음
        self.Flag = 0x0100  
        self.Questions = 1  # 질문 1개 
        self.AnswerRRs = 0 
        self.AuthorityRRs = 0 
        self.AdditionalRRs = 0
    
    def response(self, packet):     # processing dns response
        dnsHeader = packet[:12]     # 헤더
        dnsData = packet[12:].split(b'\x00', 1)   # '\x00' = 질문이 끝나는 부분
                                                  # 그 이후부터 가져온다

        ansRR = packet[12+len(dnsData[0])+5:12+len(dnsData[0])+21] 
        rr_unpack = struct.unpack('!2sHHIH4s', ansRR)
        ip_addr = socket.inet_ntoa(rr_unpack[5]) 
        print(self.domainName, ip_addr)

    def query(self):        # create dns query
        # DNS header packing
        query = struct.pack('!HH', self.TransactionId, self.Flag)
        query += struct.pack('!HH', self.Questions, self.AnswerRRs)
        query += struct.pack('!HH', self.AuthorityRRs, self.AdditionalRRs)

        part = self.domainName.split('.')

        for i in range(len(part)):
            query = query + struct.pack('!B', len(part[i]))
            query = query + part[i].encode()

        query = query + b'\x00'     # 임의로 'x\00' 추가

        query_type = 1 # Type: A
        query_class = 1 # Class: IN
        query = query + struct.pack('!HH', query_type, query_class)

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        addr = ('220.69.193.130', 53)
        sock.sendto(query, addr)
        packet, address = sock.recvfrom(65535) 
        self.response(packet)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        client = DnsClient(sys.argv[1])
        client.query()