# -*- coding:utf-8 -*-

import os

'''
create dir_path and create new dir
'''
# new_file=os.path.join('D:/TempStorage', 'abc')	#创建一个新的目录路径

# data_path=os.path.join(os.getcwd(),'data')	#创建一个新的目录路径

# os.mkdir(new_file)	#创建一个新目录

# print(data_path)

##########################################################################
new_file=os.path.join('D:/TempStorage', 'abc')
file1=os.path.join('D:/TempStorage/abc')
file2=os.path.join('D:/TempStorage/abc\\nothello.txt')
file3=os.path.join('D:/TempStorage/abc文件夹')
for x in os.listdir(new_file):
	y=os.path.join(new_file,x)
	if os.path.isdir(y):
		print(x)