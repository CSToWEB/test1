# -*-coding:utf-8-*-

#__getattr__ 定制类

# class Chain(object):

#     def __init__(self, path=''):
#         self._path = path

#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))

#     def __str__(self):
#         return self._path

#     __repr__ = __str__

# #test
# print(Chain().status.user.timeline.list)

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, att):		#可利用该方法动态处理任何属性
        if att=='score':
            return 99
        else:
        	return '\'Student\' object has no attribute \'%s\'' % att
        #raise AttributeError('\'Student\' object has no attribute \'%s\'' % att)

s=Student()
print(s.name)
print(s.gender)

