#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading
start = (time.time())
# 新线程执行的代码:
cout = 0
def count(n):
    global cout
    cout = cout + n
    cout = cout - n
def prical(n):
    for i in range(100000):
        count(n)

t = 1
def loop():
    global t
    print('调用loop次数', t)
    t=t+1
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(5)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t0 = threading.Thread(target=loop)
t1 = threading.Thread(target=loop)
t2 = threading.Thread(target=loop)
t0.start()
t1.start()
t2.start()
t0.join(4)
t1.join(2)
t2.join(2)
print('thread %s ended.' % threading.current_thread().name)
#loop()
#loop()
#loop()
#prical(0)
print(cout)
end = (time.time())
print(end-start)
#多线程的速度并不会提升
