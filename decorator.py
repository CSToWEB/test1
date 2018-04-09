# -*- coding: utf-8 -*-

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def printtime(*args,**kw):
        t0=time.time()
        fn(*args,**kw)
        t1=time.time()
        t=(t1-t0)*1000
        print('%s executed in %f ms' % (fn.__name__,t))
        return fn(*args,**kw)
    return printtime

# 测试
@metric         #相当于是 fast=metric(fast)
def fast(x, y):
    #time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    #time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
print(f)
s = slow(11, 22, 33)
print(s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
	print('测试成功!')
