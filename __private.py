# -*- coding:utf-8 -*-

#Understand 'Private name mangling'——私有变量轧压（或者叫‘名称改编’）
class A(object):					# 类A定义了一个私有成员函数（变量）
	def __init__(self):				# 在代码生成之前先执行私有变量轧压
		self.__private()			# self._A__private()
		self.public()
	def __private(self):			# def _A__private(self):
		print('A.__private()')
	def public(self):
		rint('A.public()')
		
class B(A):							# 类B定义的时候没有覆盖__init__方法，
	def __private(self):			# 所以调用的仍然是A.__init__
		print('B.__private()')
	def public(self):
		print('B.public()')

mystr='''
class A(object):
	def __init__(self):
		self.__private()
		self.public()
	def __private(self):
		print('A.__private()')
	def public(self):
		rint('A.public()')
		
class B(A):
	def __private(self):
		print('B.__private()')
	def public(self):
		print('B.public()')
		
b=B()的运行结果：
'''
print(mystr)
b = B()
