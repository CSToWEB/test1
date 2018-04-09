# ！/user/bin/python
# -*- coding:utf-8 -*-

#倒序汉诺塔
'''
1.该函数实现n>2个盘子如何实现汉诺塔
2.倒序汉诺塔规则：
（1）三个柱子A B C 起始位置A上有N个盘子
（2）一次只能移动一个盘子，盘子由大到小依次从上到下排列；
（3）移动盘子时仍然遵守上大下小的规则
3.打印如何实现将所有盘子从A移动到C上的整个过程
'''
def move(n,a,b,c):
	if n==1:
		print('move',a,'-->',c)
	else:
		move(1,a,c,b)
		move(n-1,a,b,c)
		move(1,b,a,c)

value=input("请输入汉诺塔（倒序）的层数： ")
n=int(value)
move(n,'A','B',"C")
