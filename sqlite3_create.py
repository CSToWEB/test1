# -*- coding:utf-8 -*- 

import sqlite3

'''
(1)Connection和Cursor对象，打开后一定记得关闭

(2)Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数

(3)Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list,
每个元素都是一个tuple，对应一行记录。

(4)如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，
有几个?占位符就必须对应几个参数，例如：
cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))

'''

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'1\', \'Mike\')')
cursor.execute('insert into user (id, name) values (\'2\', \'Jane\')')
cursor.execute('insert into user (id, name) values (\'5\', \'Mary\')')
cursor.execute('insert into user (id, name) values (\'10\', \'k-James\')')
cursor.execute('insert into user (id, name) values (\'100\', \'k-T\')')
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()
