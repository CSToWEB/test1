# -*- coding: utf-8 -*-

from functools import reduce

def str2num(s):
	try:
		return int(s)
	except Exception as e:
		return float(s)
	else:
		print('no error')
	finally:
		pass	

def calc(exp):
    return eval(exp)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()