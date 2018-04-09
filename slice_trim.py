# -*- coding: utf-8 -*-

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格
# 注意不要调用str的strip()方法

#定义一个去空格函数
def trim(s):
	while s[:1] == ' ':    #为什么不用s[0]而采用切片——因为当字符串为空（''）或者
		s = s[1:]      #全部为空格时，使用s[0]会出错（string out of index）
	while s[-1:] == ' ':   #而采用切片，当字符串为空时会自动返回空值
		s = s[:-1] 
	return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


'''
#递归解法
def trim(s):
    if len(s)==0:
        return s
    if s[0]==' ':
        return trim(s[1:])
    if s[-1]==' ':
        return trim(s[:-1])
    return s

#其他解法

'''
