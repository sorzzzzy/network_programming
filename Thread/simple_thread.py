import threading 

def prtSquare(num):
    print("Square: {}".format(num**2))

def prtCube(num):
    print("Cube: {}".format(num**3))

# 인자가 1개여도 튜플형태로 넘겨주어야 함
t1 = threading.Thread(target=prtSquare, args=(10,))
t2 = threading.Thread(target=prtCube, args=(10,))

t1.start()  # start thread 1
t2.start()  # start thread 2

t1.join()   # wait until thread 1 is completed
t2.join()   # wait until thread 2 is completed

print('Done!')