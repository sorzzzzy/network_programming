# 딕셔너리 생성
d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, 
    {'name':'Princess', 'phone':'555-3141', 'email':''}, 
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

# 전화번호가 8로 끝나는 사용자의 이름 출력
list1 = []
for key in range(len(d)):
    if d[key]['phone']:
        user = d[key]['phone']
        # 끝자리가 8이면
        if user[-1] == '8':
            list1.append(d[key]['name'])
print('전화번호가 8로 끝나는 사용자 : ', list1)

# 이메일이 없는 사용자 이름 출력
list2 = []
for key in range(len(d)):
    # 이메일이 없으면
    if len(d[key]['email']) == 0:
        list2.append(d[key]['name'])
print('이메일이 없는 사용자 : ', list2)

# 사용자 이름을 입력받아 출력
user = input('사용자 이름을 입력하세요 : ')
flag = True
for key in range(len(d)):
    if d[key]['name'] == user:
        print(user, '의 전화번호 :', d[key]['phone'], ', 이메일 :', d[key]['email'])
        flag=False
if flag:
    print('이름이 없습니다.')