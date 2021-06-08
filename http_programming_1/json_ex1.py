# json.loads() 함수: JSON 포맷(문자열)을 딕셔너리로 변환하는 함수

import json

with open('ex.json', 'r') as f:
    data = f.read()

json_data = json.loads(data) 
print(type(json_data))
print(json_data) 
print(json_data['children']) 
print(json_data['children'][1]['firstName'],
       json_data['children'][1]['age'])