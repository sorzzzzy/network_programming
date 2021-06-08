# 메일 보내기: 여러 사람에게 메일 전송 + 이미지 파일 첨부하기

import smtplib
from email.message import EmailMessage
import imghdr   # 이미지 유형을 판단해주는 모듈

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jinsol9830@gmail.com'
password = 'poymdpnxppohzsze'
family = ['jinsol0330@naver.com', 'jinsol0330@sch.ac.kr']

msg = EmailMessage()
msg['Subject'] = '내 사진'
msg['From'] = sender
msg['To'] = ', '.join(family)
text = '내 사진입니다'
msg.set_content(text)
msg.preamble = 'Fail'

# 첨부할 파일 열기
with open('profile.jpg', 'rb') as f:
    img_data = f.read()

# add_attachment 함수를 이용해 파일 첨부. 
# 파일 첨부시 첨부된 파일의 mime-type 지정
msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data), filename='profile.jpg')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()