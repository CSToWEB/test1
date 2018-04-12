#-*- coding:utf-8 -*-

#给类、实例绑定属性/方法
class Student(object):
	"""docstring for Student"""
	# def __init__(self, arg):
	# 	super(Student, self).__init__()
	# 	self.arg = arg

#给实例绑定属性
s=Student()
s.name='Mike'
print(s.name)

#给实例绑定方法
def set_grade(self,grade):
	self.grade=grade

Student.set_grade=set_grade

s1=Student()
s1.set_grade(98)
print(s1.grade)

#限制实例的属性
class Animal(object):
	__slots__=('name','age')

dog=Animal()
dog.age=5
# dog.gender='male'	#'Animal' object has no attribute 'gender';运行会报错
print(dog.age)

class cat(Animal):
	"""docstring for cat"""
	__slots__=('gender','shape')

miao=cat()
miao.shape='cycle'
miao.age=999
# miao.color='black'
# print(miao.color)
print(miao.age,miao.shape)