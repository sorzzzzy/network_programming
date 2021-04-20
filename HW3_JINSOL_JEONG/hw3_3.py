# 다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여,
# 딕셔너리로 반환하는 함수를 포함하는 프로그램을 작성하라.

user_input = 'led=on&motor=off&switch=off'

res1 = user_input.split('&')
# res1 = ['led=on', 'motor=off', 'switch=off'] 이라는 리스트 형태로 출력됨

# 새로운 딕셔너리 생성
res2 = {}

for i in res1:
    key, val =(i.split('='))
    res2[key] = val
print(res2)