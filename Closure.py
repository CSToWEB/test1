# -*- coding: utf-8 -*-

'''
(1)一个函数可以返回一个计算结果，也可以返回一个函数。
(2)返回一个函数时，牢记该函数并未执行，返回函数不要引用任何循环变量，
或者后续会发生变化的变量.
(3)在函数中又定义了函数,并且内部函数可以引用外部函数的参数和局部变量，当外部函数
返回内部函数时，相关参数和变量都保存在返回的函数中，这种程序结构称为“闭包'Closure'
'''

def createCounter():
	lis=[0]
	def counter():
		lis[0]=lis[0]+1
		return lis[0]
	return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
