# requests.get()

import requests

rsp = requests.get('https://naver.com') 
print(rsp.status_code) # 응답 상태 코드 
print(rsp.encoding) # 응답 데이터의 인코딩 방식

url = 'https://search.naver.com/search.naver' 
payload = {'query': 'iot'}
rsp = requests.get(url, params=payload)

print(rsp.url) 
print(rsp.headers) 
print(rsp.text)
# 요청 URL
# 응답 헤더
# 응답 데이터