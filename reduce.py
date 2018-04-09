# -*- coding: utf-8 -*-
from functools import reduce

#定义一个两数相加函数
def add(a,b):
	return a*b
#利用reduce定义一个多个数相乘的函数
def prod(self):
	total=reduce(add,self)
	return total

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
	
