# 2개의 스레드를 가지고 전역변수 'x' 증가시키기
# Lock 클래스 사용

import threading

x = 0 # global variable shared by threads

def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(300000):
    
    # 임계구역
    lock.acquire() # Acquire lock before accessing the shared data 
    increment()
    lock.release() # Release lock after finishing the access

def main_task():
    global x
    x=0     # initialize x as 0

    lock = threading.Lock() # create a lock object

    t1 = threading.Thread(target=thread_task, args=(lock,)) 
    t2 = threading.Thread(target=thread_task, args=(lock,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main_task()
    print('Iteration {0}: x = {1}'.format(i, x))