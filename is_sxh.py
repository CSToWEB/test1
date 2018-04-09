# -*- coding:utf-8 -*-

#判断一个数是否是水仙花数
def is_sxh(n):
	s=len(str(n))
	t=0
	if s<3:
		print('请输入一个三位数及以上的正整数！')
	else:
		for x in str(n):
			t+=int(x)**s
		if t==n:
			return True
		else:
			return False

# s1=[153,667,888]
# s2=list(map(is_sxh,s1))
# print(s2)
while True:      
    print('判断一个数是否是水仙花数')
    x=int(input('请输入待待判断的数：'))
    if is_sxh(x)==True:
        print('%d是水仙花数'%x,'\n')
    else:
        print('%d不是水仙花数'%x,'\n')
