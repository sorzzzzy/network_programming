'''
● SFTP 클라이언트 객체 생성
    1. paramiko.Transport() 객체로부터 생성하기 (SFTP 예제 1) 
    2. paramiko.SSHClient() 객체로부터 생성하기 (SFTP 예제 2, 3)
● 파일 전송 및 수신
    -> 파일 전송: sftp.put(로컬 파일, 원격 파일)
        : 내 컴퓨터의 ‘로컬 파일’을 원격 시스템의 ‘원격 파일’로 전송 
    -> 파일 수신: sftp.get(원격 파일, 로컬 파일)
        : 원격 시스템의 ‘원격 파일’을 내 컴퓨터의 ‘로컬 파일’로 가져옴
''' 

# SFTP 1: 파일 송수신 (Transport 이용)

import paramiko
import getpass

# 인증과 보안을 제공해주는 보안채널(transport)생성 - ssh 기반으로 함
# 접속할 서버의 주소와, 포트번호 (ssh주소, ssh포트번호)
transport = paramiko.Transport(('114.71.220.79', 22))

user = input('Username: ')
pwd = getpass.getpass('Password: ')
# 트랜스포트 객체에 연결
transport.connect(username=user, password=pwd)

# SFTP 클라이언트 객제 생성
sftp = paramiko.SFTPClient.from_transport(transport)


src_file_path = 'test/iot.txt'  
# [0]:test  [1]:iot.txt
# 현재 디렉토리에 iot.txt 라는 파일의 이름으로 가져오겠다
dst_file_path = src_file_path.split('/')[1]
# get : 원격 서버에 있는 파일을 내 로컬 파일로
sftp.get(src_file_path, dst_file_path)


src_file_path = 'index.html'
dst_file_path = src_file_path
# put : 로컬에 있는 파일을 서버로 보내기
sftp.put(src_file_path, dst_file_path)

sftp.close()
transport.close() 