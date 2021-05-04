# 2개의 스레드를 가지고 전역변수 'x' 증가시키기

import threading

x = 0 # global variable shared by threads

# 전역변수를 1 증가시키는 함수
def increment():
    global x
    x += 1

# 스레드가 수행할 함수
def thread_task():
    for _ in range(300000):
        increment()

def main_task():
    global x
    x=0     # initialize x as 0

    # 스레드 생성
    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task) 
    
    t1.start()
    t2.start()

    t1.join() 
    t2.join()

# 메인 스레드
for i in range(10):
    main_task()
    print('Iteration {0}: x = {1}'.format(i, x))