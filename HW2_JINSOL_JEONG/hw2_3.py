# 문자 'a'가 들어가는 단어를 키보드에서 입력 받아 
# 첫 번째 줄에는 'a'까지의 문자열을 출력하고, 
# 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.

str = input('문자열을 입력하세요 : ')

result = str.find('a')

print(str[:result+1])
print(str[result+1:])

