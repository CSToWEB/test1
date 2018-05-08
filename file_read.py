# -*- coding:utf-8 -*-

fpath = r'D:\TempStorage\myReposity\studentInfo.py'
#r的作用相当于C#里面的@——一字不变的指定字符串

with open(fpath, 'r') as f:
    s = f.read()
    print(s)