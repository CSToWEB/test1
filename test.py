# -*- coding:utf-8 -*- 

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(3)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()