# -*- coding: utf-8 -*-
# 
# 

L1 = [('Bob', 75), ('adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0].upper()

def by_score(t):
	return -t[1]

print('#列表按名字排序')		
L2 = sorted(L1, key=by_name)
print('排序前:',L1)
print('排序后:',L2,'\n')

#print('')

print('#列表按成绩排序（从高到低）')		
L3 = sorted(L1, key=by_score)
print('排序前:',L1)
print('排序后:',L3)
