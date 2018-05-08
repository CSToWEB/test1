# -8- coding:utf-8 -*-
from io import StringIO;

f = StringIO()
f.write('Hello World!')
print(f.tell())
f.seek(6)
print(f.tell())
s = f.readline()
print(s)
print(f.tell())

print('__________________')

d = StringIO("1\n2\n3")
print(d.tell())
d.write("4\n 5\n 6")
print(d.tell())
#d.seek(0)
print(d.readline())