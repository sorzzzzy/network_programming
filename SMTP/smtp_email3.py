# 메일 보내기: HTML 메일 전송하기

import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'jinsol9830@gmail.com' 
recipient = 'jinsol0330@naver.com' 
password = 'poymdpnxppohzsze'

msg = EmailMessage()
msg['Subject'] = "HTML 메시지 전송"
msg['From'] = sender
# 보내는 사람을 튜플로 지정
msg['To'] = ('jinsol0330@sch.ac.kr', 'jinsol0330@naver.com') 

# HTML 메시지 작성하기
# 
content_id = 'my_image1'
# add_alternative : 이 함수는 html로 보내고 싶은 내용을 추가할 수 있음
msg.add_alternative('''\
<html>
<head></head> 
    <body>
    <p>안녕하세요.</p>
    <p>순천향대학교 김대희입니다.</p> 
    <p>아래 사이트 확인 부탁 드립니다.</p> 
    <p>
        <a href=https://labs.sch.ac.kr/department/iot/m/> 순천향대학교 사물인터넷학과</a> 
    </p>
    <p>감사합니다.</p>
    <img src="cid:{cid}" />
    </body>
</html>
'''.format(cid=content_id), subtype='html')

# HTML 메시지의 해당 부분에 이미지 추가하기 
with open("profile.jpg", 'rb') as img:
    # get_payload : 기존에 작성된 메시지가 나옴
    # 우리는 하나밖에 작성하지 않았기 때문에 바로 위의 메시지가 나옴
    # add_related : 읽어들인 이미지 파일의 내용을 읽어서 cid에 해당되는 곳에 집어넣음
    msg.get_payload()[0].add_related(img.read(), maintype='image', subtype='jpg', cid=content_id)

# 보내는 메시지 저장하기
with open('outgoing.msg', 'wb') as f:
    f.write(bytes(msg))

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) 
s.ehlo()
s.starttls()
s.login(sender, password) 
s.send_message(msg)
s.quit()