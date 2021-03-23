days = {'January':31, 'February':28, 'March':31, 
        'April':30, 'May':31, 'June':30, 
        'July':31, 'August':31, 'September':30, 
        'October':31, 'November':30, 'December':31}

# 사용자의 입력에 따라 월의 일수 출력
month = input('월을 입력해주세요 : ')
print('입력한 월의 일수는 : ', days[month])

# 알파벳 순서로 모든 월 출력
print('알파벳 순서로 월 출력하기 : ', sorted(days))

# 일수가 31인 월 출력
list1=[]
print('일수가 31인 월은')
for key, val in days.items():
    if val == 31:
        list1.append(key)
print(list1)

# 월의 일수를 기준으로 오름차순으로 쌍 출력
print('월의 일수를 기준으로 오름차순으로 쌍 출력 ')
for key, val in sorted(days.items(), key=lambda x:x[1]):
    print(key,val)

# 사용자가 월을 3자리만 입력하면 월의 일수 출력
month2 = input('월을 3자리만 입력해주세요 : ')
for key, val in days.items():
    if key[0:3] == month2:
        print(val)