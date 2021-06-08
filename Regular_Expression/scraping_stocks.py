import requests
import re

url = 'https://finance.naver.com/item/main.nhn?code=005930'
rsp = requests.get(url)
# 응답 메시지의 데이터를 가져옴
html = rsp.text

stock_results = re.findall(r'(<dl class="blind">)([\s\S]+?)(</dl>)', html)
# HTML 내에 2개의 <dl class>~</dl> 부분이 존재. 첫 번째 것을 선택
samsung_stock =stock_results[0]
# <dl class>~</dl> 사이의 정보만 추출
samsung_index = samsung_stock[1]

# 주식 정보(<dd>~</dd>)를 추출
index_list = re.findall(r'(<dd>)([\s\S]+?)(</dd>)', samsung_index)

for index in index_list:
    print(index[1])