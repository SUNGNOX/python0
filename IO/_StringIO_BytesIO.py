# -*- coding: utf-8 -*-
#2017.9.3
#getvalue可以读取二进制和文本格式
from io import StringIO, BytesIO
f = StringIO('hello\nworld\n!\n')
# 1、
print(f.getvalue())
#2、
s = f.readline()
print(s.strip())
s = f.readline()
print(s.strip())
s = f.readline()
print(s.strip())

print(f.getvalue())

print(f.readlines())

f.close()

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
f.close()

import os
print(os.name)
# print(os.uname())#uname()函数在Windows上不提供
print(os.environ['PATH'])

