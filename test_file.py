# -*- coding:utf-8 -*-

import re, time
from datetime import datetime

# # split string
# s1 = 'a b c  d'
# print(s1.split(' '))

# # match string
# n1 = '010-12345'
# n2 = '010，12345'
# tele = re.compile(r'^\d{3}\-\d{3,8}$')
# R1 = re.match(r'^\d{3}\-\d{3,8}$', n1)
# R2 = tele.match(n1)
# print(R1)
# print(R2)

t1 = time.time()
dt1 = datetime.now()
print(datetime.fromtimestamp(t1))
print(dt1.timestamp())
#print(dt1.strftime('%Y/%m/%d %H:%M:%S'))
print(dt1.strftime('%c | %x'))