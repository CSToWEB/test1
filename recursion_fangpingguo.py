# -*- coding:utf-8 -*-

'''
ACM 题库题解大全> poj 1664 放苹果:
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，
问共有多少种不同的分法？
（注：5，1，1和1，5，1 以及1，1，5是同一种分法）
'''

def divide_apple(m,n):
	if m==0 or n==1:
		return 1
	elif m<n:
		return divide_apple(m,m)	
	else:
		return divide_apple(m,n-1)+divide_apple(m-n,n)

#测试
while True:
	m=int(input('请输入苹果个数：'))
	n=int(input('请输入盘子数目：'))
	result=divide_apple(m,n)
	print("%s个苹果，%s个盘子一共有“%s”种不同的分法"%(m,n,result))
