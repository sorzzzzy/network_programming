def cal_gcd(num1,num2):
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1

num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))

result = cal_gcd(num1,num2)

print(result)
