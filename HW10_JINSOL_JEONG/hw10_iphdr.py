# UDP 헤더 pack/unpack 해보기
# UDP 헤더는 2바이트 송신자 포트번호Source Port, 2바이트 수신자 포트번호Destination Port,
# 2바이트 UDP 패킷 길이Length, 2바이트 체크섬Checksum으로 구성됨 (총 8바이트)

import socket
import struct
import binascii

class Udphdr:
    # sport = 송신자 포트 / dport = 수신자 포트
    def __init__(self, sport, dport, len, checksum):
        self.sport = sport
        self.dport = dport
        self.len = len
        self.checksum = checksum
    
    def pack_Udphdr(self):
        packed = b''    # 바이트 객체로 초기화
        # '!' = 빅엔디언
        # B=1bytes / H=2bytes
        packed += struct.pack('!H', self.sport) # 2bytes
        packed += struct.pack('!H', self.dport) # 2bytes
        packed += struct.pack('!H', self.len) # 2bytes
        packed += struct.pack('!H', self.checksum) # 2bytes
        return packed
    
def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!HHHH', buffer[:8]) 
    return unpacked     # 튜플형태

def getSPort(unpacked): 
    return unpacked[0]

def getDPort(unpacked): 
    return unpacked[1]

def getLen(unpacked): 
    return unpacked[2]

def getChecksum(unpacked): 
    return unpacked[3]

# pack
ip = Udphdr(5555, 80, 1000, 0xFFFF) 
packed_udphdr = ip.pack_Udphdr() 
print(binascii.b2a_hex(packed_udphdr))

# unpack
unpacked_udphdr = unpack_Udphdr(packed_udphdr) 
print(unpacked_udphdr)

print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'\
    .format(getSPort(unpacked_udphdr), getDPort(unpacked_udphdr), getLen(unpacked_udphdr), getChecksum(unpacked_udphdr)))