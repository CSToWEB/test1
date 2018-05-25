# -*- coding:utf-8 -*- 

import sqlite3

'''
1.如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，
有几个?占位符就必须对应几个参数，例如：
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

2.要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露.
[可使用错误处理来确保程序在出错的情况下仍能正确关闭Connection对象和Cursor对象]
'''
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values[0][1])
cursor.close()
conn.close()
