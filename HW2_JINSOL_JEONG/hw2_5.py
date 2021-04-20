# for 루프를 이용해 다음과 같은 리스트 생성
#   -> 0~49 까지의 수로 구성되는 리스트
#   -> 0~49 까지 수의 제곱으로 구성되는 리스트

list1 = []
list2 = []

for i in range(50):
    list1.append(i)
    list2.append(i ** 2)

print(list1)
print(list2)