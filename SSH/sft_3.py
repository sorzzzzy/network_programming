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
 
# SFTP 3: 원격 서버의 특정 폴더를 압축한 후 가져오기

import paramiko
import getpass

# 압축파일 이름
filename = 'test.zip'
# 압축할 폴더
dirname = '/home/net_pro/test'
# 리눅스 압축 명령어
CMD = 'zip -r ' + filename + ' ' + dirname

# ssh 연결
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

user = input('Username: ')
pwd = getpass.getpass('Password: ')
ssh.connect('114.71.220.79', 22, user, pwd)

# 명령어 실행 결과가 stdout에 저장됨
stdin, stdout, stderr = ssh.exec_command(CMD)

# open_sftp() : SFTP 클라이언트 객체 생성 
sftp = ssh.open_sftp()

# 압축 파일을 로컬로 가져오기
# 서버에 test.zip이라는 이름으로 만들어져 있으므로
# 내 컴퓨터 현재 디렉토리에도 똑같은 이름으로 가져옴
sftp.get(filename, filename)

sftp.close()
ssh.close()