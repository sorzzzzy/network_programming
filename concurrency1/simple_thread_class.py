import threading
import datetime

class myThread(threading.Thread):
    def __init__(self, name, counter):
        super().__init__()
        # 오버라이딩
        self.name = name
        self.counter = counter

    # 이 스레드가 실제로 할 일
    def run(self):
        print('\nStarting {}[{}]'.format(self.name, self.counter)) 
        print_date(self.name, self.counter)
        print('\nExiting {}[{}]'.format(self.name, self.counter))

def print_date(threadName, counter):
    today = datetime.date.today()
    print('\n{}[{}]: {}'.format(threadName, counter, today))

thread1 = myThread('Th', 1)
thread2 = myThread('Th', 2)

thread1.start() 
thread2.start()

thread1.join()
thread2.join()

print('\nExiting the program')
 