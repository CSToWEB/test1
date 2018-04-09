#coding:utf-8

import math
#构造求解一元二次方程的函数
def quadratic(a,b,c):
    for v in (a, b, c):
        if not isinstance(v, (int, float)):
            raise TypeError('bad operand type')
        else:
            delta=b*b-4*a*c
            if delta<0:
                print('此方程无实数解！')
            elif delta==0:
                x=-b/(2*a)
                return x
            else:
                x1=(-b+math.sqrt(delta))/(2*a)
                x2=(-b-math.sqrt(delta))/(2*a)
                return x1,x2

#输入系数，输出结果
while True:
    print('求解一元二次方程：ax^2+bx+c=0','\n请依次输入方程的系数')
    a=float(input('请输入a:'))
    b=float(input('请输入b:'))
    c=float(input('请输入c:'))
    print(quadratic(a,b,c),'\n')

