# SSH: 원격 시스템의 CPU 및 메모리 정보 조회하기

import getpass
import paramiko

PORT = 22

# 기본 설정
cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

# 아이디와 비밀번호 입력
user = input('Username: ')
# 비밀번호는 보이면 안되기 때문에 getpass.getpass() 사용
pwd = getpass.getpass('Password: ')

# 서버에 연결
cli.connect('114.71.220.79', port=22, username=user, password=pwd)

# 내가 접속한 서버에서 cpu 정보를 보고싶을 때, 
# cpu 정보가 출력되고 결과가 stdout에 리턴이 됨
stdin, stdout, stderr = cli.exec_command('cat /proc/cpuinfo')
# 한 줄 한 줄 읽고
lines = stdout.readlines()
# join으로 합쳐짐
print(''.join(lines))

# 메모리 정보를 읽음
stdin, stdout, stderr = cli.exec_command('cat /proc/meminfo')
lines = stdout.readlines()
print(''.join(lines))

cli.close()