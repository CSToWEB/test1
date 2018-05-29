#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

def addFunc(a,b):  
    return a+b  

if __name__ == '__main__':  
    print('test1计算结果:',addFunc(1,1))
elif __name__=='test1':
    print('该消息来自被调用的模块%s'%__name__)

#代码if name == 'main'实现的功能就是
#Make a script both importable and executable
#注：name两边各有2个下划线, __name__有2个取值：
#当模块是被调用执行的，取值为模块的名字；当模块直接执行，则该变量取值为：__main__

