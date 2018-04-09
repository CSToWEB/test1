# -*- coding:utf-8 -*-

import random,time, functools
################################################################
#创建一个装饰器，用来打印函数的执行时间
def metric(fn):
	@functools.wraps(fn)
	def printTime(*agrs,**kw):
		t0=time.time()
		fn(*agrs,**kw)
		t1=time.time()
		t=(t1-t0)*1000
		print('%s executed in %s ms' % (fn.__name__, t))
		return fn(*agrs,**kw)
	return printTime
################################################################
#排序算法-冒泡排序
@metric
def bubblesort(list_num):
	list_length=len(list_num)
	for i in range(list_length):
		n=0
		for j in range(list_length-1-i):
			if list_num[j]>list_num[j+1]:	#把每一轮最大的数交换到最后面
				list_num[j],list_num[j+1]=list_num[j+1],list_num[j]
				n+=1
		if n==0:
			break
	return list_num

#排序算法-选择排序
@metric
def selectsort(list_num):
	list_length=len(list_num)
	for i in range(list_length):
		min=i
		for j in range(i+1,list_length):
			if list_num[min]>list_num[j]:
				min=j
		if i !=min:		#每一轮将最小值放到‘最前面’
			list_num[i],list_num[min]=list_num[min],ist_num[i]
		return list_num

#测试
list_num=[random.randint(0,100) for i in range(1000)]
print('原始数列：',list_num)
print('冒泡排序：',bubblesort(list_num))
print('选择排序：',selectsort(list_num))

