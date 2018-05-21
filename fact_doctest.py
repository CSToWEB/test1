# -*- coding: utf-8 -*-


'''
文档测试：在函数说明文档部分：
（1）可解释函数的作用;
（2）编写测试用例（遵循交互式输入方式）
（3）若测试通过，则正常运行，否则报错。
'''

def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
