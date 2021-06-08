# SSH: 원격 시스템에서 연속적으로 명령어 실행하기

import getpass
import paramiko
import time

BUF_SIZE = 65535

# 기본 설정
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

user = input('Username: ')
pwd = getpass.getpass('Password: ')

# 접속하기
cli.connect('114.71.220.79', username=user, password=pwd)

# invoke_shell : 새로운 셸 세션이 생성됨
# 이를 가지고 계속해서 명령을 내릴 수 있음
channel = cli.invoke_shell()
'''
채널을 통해 명령어 전송
엔터를 의미하는 \n 꼭 넣어주기
텀을 두기를 권장 (1초나 0.5초)
'''
# CPU 정보 출력
channel.send('cat /proc/cpuinfo\n')
time.sleep(0.5)
# 메모리 정보 출력
channel.send('cat /proc/meminfo\n')
time.sleep(0.5)
# test라는 폴더가 생성됨
channel.send('mkdir test\n')
time.sleep(0.5)
# 해당 폴더로 들어감
channel.send('cd test\n')
time.sleep(0.5)
# iot.txt 라는 텍스트 파일을 만듬
channel.send('echo iot > iot.txt\n')
time.sleep(0.5)
# 내용을 보여줌
channel.send('cat iot.txt\n')
time.sleep(0.5)

# 명령어 실행결과를 수신
output = channel.recv(BUF_SIZE).decode()
print(output)

cli.close()