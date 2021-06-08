# 동기방식
# 1초후에 hello, 2초후에 world를 출력

import time

def say_after(delay, what): 
    time.sleep(delay) 
    print(what)

def main():
    # 시간, 분, 초 단위로 출력
    print(f"started at {time.strftime('%X')}")

    say_after(1, 'hello') 
    say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}") 

main()