# -*- coding: utf-8 -*-
# 

#将用户输入的名字修改为标准格式
#1
def normalize(name):
	name=name.lower()
	name=name.title()		
	return name

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


'''
#方法二
def pro(name):
    n=1
    mystr=''
    for s in name:
        if n==1:
            mystr=mystr+s.upper()
        else:
            mystr=mystr+s.lower()
        n=n+1
    return mystr
L=['lily','ABC','MiKe']
L2=map(pro,L)
print(list(L2))
'''