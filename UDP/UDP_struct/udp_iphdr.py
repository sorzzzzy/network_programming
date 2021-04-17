import socket
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

# unpack
unpacked_iphdr = unpack_Iphdr(packed_iphdr) 
print(unpacked_iphdr)
print('Packet size:{} Protocol:{} IP:{}'\
    .format(getPacketSize(unpacked_iphdr), getProtocolId(unpacked_iphdr), getIP(unpacked_iphdr)))