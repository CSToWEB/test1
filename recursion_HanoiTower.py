#-*- coding:utf-8 -*-
'''
1.该函数实现n>2个盘子如何实现汉诺塔
2.汉诺塔规则：
（1）三个柱子A B C 起始位置A上有N个盘子
（2）一次只能移动一个盘子，盘子由小到大依次从上到下排列
（3）移动盘子时仍然遵守上小下大的规则
3.打印如何实现将所有盘子从A移动到C上的整个过程
'''
def yidong(n, a, b, c): 
     if n == 1: 
          print('move', a, '-->', c) 
     else:
          yidong(n-1, a, c, b) 
          yidong(1, a, b, c) 
          yidong(n-1, b, a, c) 
 
 
rec=input('请输入A柱上的盘子数： ')
n=int(rec)
yidong(n, 'A', 'B', 'C')

input()
