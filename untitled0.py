# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:05:40 2017

@author: sun
"""

import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.current_thread().name)
    r = yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()