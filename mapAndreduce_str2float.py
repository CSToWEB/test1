# -*- coding: utf-8 -*-
from functools import reduce

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def char2float(ch):
	return CHAR_TO_FLOAT[ch]

def str2float(s):
    nums = map(char2float, s)
    #可使用lambda函数简化代码（不用定C2F函数）
    #nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point			#nonlocal：在函数或其他作用域中使用外层(非全局)变量
        if n == -1:				#当n是小数点时，返回整数部分的值
            point = 1
            return f
        if point == 0:			#小数点之前正常取数
            return f * 10 + n
        else:
            point = point * 10	#小数部分采用分别除10、100、1000···的方法
            return f + n / point
    return reduce(to_float, nums, 0.0)



print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

'''
其他思路：
（1）利用’切片‘将字符串分成两部分来处理
	找小数点的方法：index或者find
（2）去掉小数点（remove），按整数处理，然后n/pow(10,m)
'''