# 
# -*- coding: utf-8 -*-
#author:QT
# date:2018/3/29

#输出杨辉三角
'''
该方法的巧妙之处在于：
（1）L.append(0)的运用——在输出L后在末尾加0，改变L的长度，从而便于产生首尾的1；
（2）【L（-1）=列表最后一个元素】的应用
（3）测试通过的代码-->[yield_triangle.py]
注：该方法可打印出杨辉三角，但是会测试失败，思考：解决方法？
'''

#产生杨辉三角的生成器
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    #print(results)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')