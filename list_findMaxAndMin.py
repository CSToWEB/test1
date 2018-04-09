# ！/user/bin/python
# -*- coding:utf-8 -*-

#find the max/min value in a list and return a tuple.
def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    else:
        return (min(L), max(L))

print('找出列表中的最大值和最小值')
lis=[2,5,4,6,9,7]
print(lis)
print('结果：',findMinAndMax(lis))

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
	
