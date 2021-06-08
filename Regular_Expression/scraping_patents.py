from urllib import request
import re

url = 'https://bulkdata.uspto.gov/data/patent/officialgazette/2019/'
rsp = request.urlopen(url)
# 문자열로 바꾸기
html = rsp.read().decode()

# findall 을 통해 찾기
# 소괄호를 사용했기 때문에 튜플형태로 옴
file_list = re.findall(r'(e-)(.+)(zip")', html)
file_url = ''

for name in file_list:
    # 큰 따옴표 빼기
    file_url = (url + ''.join(name))[:-1]
    print(file_url)

request.urlretrieve(file_url, 'test.zip')   