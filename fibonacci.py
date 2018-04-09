# -*- coding:utf-8 -*-

#斐波那契数列
def fib(n):
	f=[]
	if n==0:
		print('请输入一个正整数！')
	elif n<3:
		for x in range(0,n):
			f.append(1)
	else:
		f=[1,1]
		for x in range(2,n):
			temp=f[x-2]+f[x-1]
			f.append(temp)
	return f	
			
n=int(input("请指定斐波那契数列的长度:"))
#list=fib(n)
#print(list)
print(fib(n))
