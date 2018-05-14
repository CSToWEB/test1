# -*- coding: utf-8 -*-

import json,pickle,os,io

storage_path='D:/TempStorage'
file1_path=os.path.join(storage_path,'dictinfo.txt')
file2_path=os.path.join(storage_path,'appendcontent.txt')

d = dict(name='Bob', age=20, score=88)
# with open(file1_path,'wb') as f1:
# 	f1.write(pickle.dumps(d))

# with open(file2_path,'ab') as f2:
# 	f2.write(pickle.dumps(d))

#观察ensure_ascii参数对中文进行序列化时的影响
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)	#设置为TRUE时以ASCII码表示中文
print(s)