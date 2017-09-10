#import aiohttp
#import asyncio
import time
def f0():
    m = ' '
    while(True):
        r = yield m
        print('我是消费者(%d)!!' % r)
        time.sleep(0.2)


def f1(coro):
    yield from coro
#相当于
#def f1(coro):
#    for g in coro:
#        yield g

def produce(c):
    c.send(None)
    n=1
    while True:
        print('生产者生产!')
        time.sleep(1)
        print('生产者生产完毕!')
        c.send(n)
        n=n+1
        time.sleep(1)
    c.close()

f = f0()
produce(f1(f))