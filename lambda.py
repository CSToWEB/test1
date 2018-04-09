# -*- coding: utf-8 -*-

'''
#匿名函数——Lambda
（1）关键字lambda表示匿名函数，冒号前面的x表示函数参数
（2）匿名函数只能有一个表达式，不用写return，返回值就是该表达式的结果
（3）匿名函数没有名字，不必担心函数名冲突
（4）匿名函数也是一个函数对象（可被赋值给变量，或者作为函数的返回值）
'''
def is_odd(n):
    return n % 2 == 1
#改写前
L = list(filter(is_odd, range(1, 20)))
#改写后
L = list(filter(lambda n: n%2==1,  range(1, 20)))
print(L)
