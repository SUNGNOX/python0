# -*- coding: utf-8 -*-
#多进程加多线程
import multiprocessing
from multiprocessing import Pool, Process
import threading
import random, os, time
lock = threading.Lock()
x = 1
def Tst_Thread2(i,k):
    x=1
    print('*********(%d)child thread(%d)(%s)**********' % (i, k, threading.current_thread().name))
    time.sleep(4)
    # while x<10000000:
    #     x = x+1
    # print('Test_Thread2222222222')

def Tst_Thread1(i,k):
    x=1
    print('*********(%d)child thread(%d)(%s)**********' % (i, k, threading.current_thread().name))
    time.sleep(3)
    # while x<10000000:
    #     x = x+1
    # print('Test_Thread1111111111')

def Tst_Thread0(i,k):
    global x
    print('*********(%d)child thread(%d)(%s)**********' % (i, k, threading.current_thread().name))
    for i in range(10):
        try:
            lock.acquire()
            # print('i=%d' % i)
            x = x+1
            time.sleep(0.5)
            x = x-1
        finally:
            lock.release()
    print('%d:x=%d' % (k, x))

def Tst(i):
    print('(%d)进程%d' % (i, os.getpid()))
    print('*********(%d)main thread(%s)**********' % (i, threading.current_thread().name))

    T0 = threading.Thread(target=Tst_Thread0, args=(i,0))
    T1 = threading.Thread(target=Tst_Thread0, args=(i, 1))
    T2 = threading.Thread(target=Tst_Thread0, args=(i, 2))
    T0.start()
    T1.start()
    T2.start()
    T0.join()
    T1.join()
    T2.join()
    print(x)
    print('(%d)%d final!!' % (i, os.getpid()))

if __name__ == '__main__':
    start = time.time()
    try:
        P = Pool(1)#进程池
        for i in range(1):
            P.apply_async(Tst, args=(i,))
        print(multiprocessing.cpu_count())
        print('ready!!')
        P.close()
        P.join()
    finally:
        print('all finish!')
        end = time.time()
        print('apply_async all time %ds' % (end-start))
    #
    # start = time.time()
    # for i in range(5):
    #     Test(i)
    # end = time.time()
    # print('next all time %d' % (end-start))
