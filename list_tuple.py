#list与tuple
# -*- coding: utf-8 -*-

#创建一个包含列表的列表（列表L的三个元素分别是三个列表）
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


#“改变”tuple的值
#tuple的每个元素，指向永远不变,指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = ('a', 'b', ['A', 'B'])
print('元组原来的值：'+str(t))
t[2][0]='X'
t[2][1]='Y'
print('元组元素\"改变\"后的值：'+str(t))

input()

