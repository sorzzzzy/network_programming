# json.dump() 함수: 파이썬 딕셔너리를 JSON 포맷으로 변환하는 함수

import json

dict_data = {'Name': 'Kim', 'Department': 'IoT', 'University': 'Soonchunhyang'}
with open('data.json', 'w') as f: 
    json.dump(dict_data, f)