# 숫자를 문자열로 변화하는 방법은 str(num)을 이용한다. 
#   --> str(12)→'12'가 된다. 
# 반대로 문자열을 숫자로 변환하려면 int(string)을 이용한다. 
#   --> int('12') → 12가 된다. 
# 이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라. 
#   --> 예를 들어 234→2+3+4=9가 된다.

# 빈 리스트 생성
num = []
sum = []

def num_list(num):
    # 1~1000 까지 리스트 생성(문자열로)
    for i in range(1,1001):
        num.append(str(i))
    return num

def cal_sum(num, sum):
    # num 리스트 안에 있는 1~1000 사이의 문자를 하나하나 가져옴
    for s in num:
        res = 0
        # 숫자의 각 자리수를 정수형으로 변환해 다 더함
        for w in s:
            res += int(w)
        # sum 리스트에 추가함
        sum.append(res)
    return sum

# print(num_list(num))
num_list(num)
print(cal_sum(num,sum))
