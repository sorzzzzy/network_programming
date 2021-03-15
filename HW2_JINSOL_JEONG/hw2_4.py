num = []
sum = []
def num_list(num):
    for i in range(1,1001):
        num.append(str(i))
    return num

def cal_sum(num, sum):
    for s in num:
        res = 0
        for w in s:
            res += int(w)
        sum.append(res)
    return sum

# print(num_list(num))
num_list(num)
print(cal_sum(num,sum))
