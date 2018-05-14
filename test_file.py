# -*- coding:utf-8 -*-

# import logging
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n

# def main():
#     foo('0')

# main()

# logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)


import re

# split string
s1 = 'a b c  d'
print(s1.split(' '))
print()

# match string
n1 = '010-12345'
n2 = '010 12345'
R1 = re.match(r'^\d{3}\-\d{3,8}$', n1)
R2 = re.match(r'^\d{3}\-\d{3,8}$', n2)
print(R1)
print(R2)