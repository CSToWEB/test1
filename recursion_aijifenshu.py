# -*- coding:utf-8 -*-

#将真分数分解为埃及分数式（分子为1的分数）之和
#递归思想
def func(a,b):
	k=b//a
	if b%a==0:
		res='1/%s'%k
	else:
		k+=1
		res='1/%s+%s'%(k,func(a*k-b,b*k))
	return res

print('分解真分数为埃及分数式：')
x1=int(input('请输入分子：'))
x2=int(input('请输入分母：'))
s=func(x1,x2)
print('%s/%s=%s'%(x1,x2,s))
