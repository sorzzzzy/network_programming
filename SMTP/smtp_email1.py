# 이메일 보내기

import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jinsol9830@gmail.com'
recipient = 'jinsol0330@naver.com'
password = 'poymdpnxppohzsze'

msg = EmailMessage()
msg['Subject'] = '이메일 테스트'
msg['From'] = sender
msg['To'] = recipient
text = '네트워크 프로그래밍 e-mail 테스트 중'
# 문자열이 본문으로 들어간 메시지가 만들어짐
msg.set_content(text)

# SMTP 객체 생성 후 메시지 전송
s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()