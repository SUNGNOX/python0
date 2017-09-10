# -*- coding: utf-8 -*-
#2017.9.3
#把变量变为可存储及传输的过程称作序列化
import json, pickle, os
from io import BytesIO

A = {'a':1,'b':2}
print(pickle.dumps(A))
#pickle,以二进制的方式打开
with open('test', 'wb') as f:
    pickle.dump(A, f)

with open('test', 'rb') as f:
    print(f.read())
os.remove('test')
#####
# f = BytesIO()
# P0 = pickle.dump(A, f)
#
# P2 = pickle.load(f)
# print(P0)

#json，以普通文本格式打开
# S = json.dumps(A)
# print(S)
with open('test', 'w') as f:
    json.dump(A, f)#序列化

with open('test', 'r') as f:
    print(json.load(f))#反序列化

