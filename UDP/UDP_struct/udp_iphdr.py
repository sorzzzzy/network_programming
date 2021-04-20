# IPv4 헤더 : 옵션 제외 시 20바이트

import socket

# struct 모듈
#   -> 이진 데이터를 bytes로 만들거나(pack)
#   -> bytes를 이진 데이터로 해석(unpack)하기 위한 모듈
import struct
import binascii

class Iphdr:
    # saddr = 보낸 IP / daar = 받는 IP
    def __init__(self, tot_len, protocol, saddr, daddr):
        self.ver_len = 0x45
        self.tos = 0
        self.tot_len = tot_len
        self.id = 0
        self.frag_off = 0
        self.ttl = 127
        self.protocol = protocol    # TCP(6)/UDP(17)
        self.check = 0
        # inet_aton = 문자열을 bytes 객체로 변환해줌
        self.saddr = socket.inet_aton(saddr) 
        self.daddr = socket.inet_aton(daddr)
    
    def pack_Iphdr(self):
        packed = b''    # 바이트 객체로 초기화
        # '!' = 빅엔디언
        # B=1bytes / H=2bytes
        packed += struct.pack('!BBH', self.ver_len, self.tos, self.tot_len) # 4byte
        packed += struct.pack('!HH', self.id, self.frag_off)    # 4byte
        packed += struct.pack('!BBH', self.ttl, self.protocol, self.check) # 4byte 
        # 이미 위에서 byte 객체로 변환을 했으므로 그냥 s로 보냄 
        packed += struct.pack('!4s', self.saddr)    
        packed += struct.pack('!4s', self.daddr)
        return packed

def unpack_Iphdr(buffer):
    unpacked = struct.unpack('!BBHHHBBH4s4s', buffer[:20]) 
    return unpacked     # 튜플형태

def getPacketSize(unpacked_ipheader): 
    return unpacked_ipheader[2]

def getProtocolId(unpacked_ipheader): 
    return unpacked_ipheader[6]

def getIP(unpacked_ipheader):
    # inet_ntoa = byte 객체를 문자열로 변환
    src_ip = socket.inet_ntoa(unpacked_ipheader[8]) 
    dst_ip = socket.inet_ntoa(unpacked_ipheader[9]) 
    return (src_ip, dst_ip)

# pack
ip = Iphdr(1000, 6, '10.0.0.1', '11.0.0.1') 
packed_iphdr = ip.pack_Iphdr() 
print(binascii.b2a_hex(packed_iphdr))
# pack_result = b'450003e8000000007f0600000a0000010b000001'

# unpack
unpacked_iphdr = unpack_Iphdr(packed_iphdr) 
print(unpacked_iphdr)
# unpack_result = (69, 0, 1000, 0, 0, 127, 6, 0, b'\n\x00\x00\x01', b'\x0b\x00\x00\x01')
# unpacked[0] = 69
# unpacked[1] = 0 과 같이 튜플 형태로 반환됨

print('Packet size:{} Protocol:{} IP:{}'\
    .format(getPacketSize(unpacked_iphdr), getProtocolId(unpacked_iphdr), getIP(unpacked_iphdr)))