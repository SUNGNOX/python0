import threading
import asyncio
import time


n = 1
def f0():
    global n
    n = n+1
    print(n)
    yield


#@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    y = yield from asyncio.sleep(10)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
#loop.run_until_complete(hello())
loop.close()