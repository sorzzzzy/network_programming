# 두 수의 최대공약수는 두 수를 나누어 떨어지는 가장 큰 수이다. 
# 예를 들어 (16, 24)의 최대 공약수는 8이다. 
# 두 수를 입력 받아 다음 알고리즘에 의해 최대 공약수를 구하는 프로그램을 작성하라.

num = input("두 수를 입력해주세요. ex)16 24 : ")
num = num.split()

num1 = int(max(num))
num2 = int(min(num))

# 작은 수가 0이 될 때 까지 반복
while num2 != 0:
    # 큰 수를 작은 수로 나눈 나머지(=res)를 구함
    res = num1 % num2

    # 큰 수를 작은 수로 대체
    num1 = num2

    # 작은 수를 나머지(=res)로 대체
    num2 = res

# 과정을 반복한 뒤 마지막 큰 수가 최대 공약수
print("Result : ", num1)