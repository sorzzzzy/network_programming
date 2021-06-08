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

# SFTP 2: 파일 송수신 (SSHClient 이용)

import paramiko
import getpass

# SSHClient 이용
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input('Username: ')
pwd = getpass.getpass('Password: ')
# ssh 접속
ssh.connect('114.71.220.79', port=22, username=user, password=pwd)

# open_sftp() : SFTP 클라이언트 객체 생성 
sftp = ssh.open_sftp()

src_file_path = 'index_get.html'
# test 밑에 index_get.html을 생성
dst_file_path = 'test/' + src_file_path
# put : 로컬에 있는 파일을 서버로 보내기
sftp.put(src_file_path, dst_file_path)

# 원격 서버에 있는 test/index_get.html 파일을 가져옴
src_file_path = dst_file_path
# index_get1.html이라는 이름으로 가져옴
dst_file_path = 'index_get1.html'
# get : 원격 서버에 있는 파일을 내 로컬 파일로
sftp.get(src_file_path, dst_file_path)

sftp.close()
ssh.close()