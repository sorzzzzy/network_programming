import re
import requests

url = 'http://goo.gl/U7mSQl'
rsp = requests.get(url)
# 응답 메시지의 데이터를 가져옴
html = rsp.text
# '+' = 1개 이상
results = re.findall(r'[A-Za-z0-9]+\*\*\*', html)

for id in results:
    print(id)