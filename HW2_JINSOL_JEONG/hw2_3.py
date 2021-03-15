str = input('문자열을 입력하세요 : ')

result = str.find('a')

print(str[:result+1])
print(str[result+1:])

