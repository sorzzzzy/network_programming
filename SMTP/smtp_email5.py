# 메일 보내기: 특정 폴더를 압축한 후 전송하기
# 폴더 내에 모든 하위폴더와 파일을 1개의 파일로 압축

import smtplib
from email.message import EmailMessage 
import zipfile
import os

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jinsol9830@gmail.com'
recipient = 'jinsol0330@naver.com'
password = 'poymdpnxppohzsze'

zf_name = 'email.zip' # 압축 파일 이름 (현재 디렉토리에 생성됨) 
folder = 'test' # 현재 디렉토리에 있는 압축할 폴더

# folder 하위의 모든 폴더와 파일을 zf_name으로 압축 
zf = zipfile.ZipFile(zf_name, 'w') 
print('Zipping current dir', folder)

# 하위 디렉토리와 파일들을 찾아가면서 압축해야함
# os.walk : 압축하고 싶은 디렉토리를 넣어주면, 
# 알아서 첫번째 디렉토리부터 하위까지 하나하나 방문해서 iterator로 돌려줌
# dirs -> 현재 디렉토리 / subdirs -> 하위 디렉토리 / files -> 그 안의 파일들
for dirs, subdirs, files in os.walk(folder):
    # 현재 디렉토리를 압축 (서브 디렉토리는 따로 안해줌, 그 이후에 할 것이기 때문)
    zf.write(dirs)
    # 디렉토리 밑에 있는 파일들을 하나하나 
    for file in files:
        # 경로는 디렉토리 밑의 파일
        zf.write(os.path.join(dirs, file)) 
zf.close()

# 메일전송
msg = EmailMessage()
msg['Subject'] = 'Source Code'
msg['From'] = sender
msg['To'] = recipient

# 압축파일 메일에 첨부(add_attachment)
with open(zf_name, 'rb') as f:
    msg.add_attachment(f.read(), maintype='application', subtype='zip', filename='e_mail.zip')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) 
s.ehlo()
s.starttls()
s.login(sender, password) 
s.send_message(msg)
s.quit()