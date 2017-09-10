# -*- coding:utf-8 -*-
#多线程并不能提高计算密集型任务的速度
#但可以提高IO密集型任务的速度
from threading import Thread
import threading
import time
threading.currentThread()
#计算密集型任务
#采用多线程运行的时间不比单线程小
def CN():
    print(threading.currentThread())
    i = 1
    for k in range(20000000):
        # time.sleep(0.001)
        i += 1
    print('i:',i)
    print('N')


def CP():
    print(threading.currentThread())
    i = 1
    for k in range(50000000):
        # time.sleep(0.001)
        i += 1
    print('i:',i)
    print('P')


#IO密集型任务
#就算是IO密集型任务，加锁之后也不能提高速度
# lock = threading.Lock()
def SN():
    i = 1
    # lock.acquire()
    for k in range(2):
        time.sleep(1)
        i += 1
    # lock.release()
    print('i:',i)
    print('N')

def SP():
    i = 1
    # lock.acquire()
    for k in range(5):
        time.sleep(1)
        i += 1
    # lock.release()
    print('i:',i)
    print('P')


if __name__ == '__main__':

    # t1 = Thread(target=CN)
    # t2 = Thread(target=CP)
    star = time.time()
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    CN()
    CP()
    en = time.time()
    print(-star+en)
