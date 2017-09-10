import pickle
import json
b = {'json': 'Job', 'age': 25, 'sex': 'boy'}
po = open('json.txt', 'w')
df = json.dump(b, po)
po.close()
pi = open('json.txt', 'r')
mp = json.load(pi)
print(mp)
pi.close()
# coding:utf-8
try:
    with open('err.py', 'rb') as g:
        for line in g:
            c = g.readline()
            print(line.strip())
finally:
    if g:
        g.close()
k = open('pickle.txt', 'rb')
b = {'name': 'Job', 'age': 25, 'sex': 'boy'}
with open('pickle.txt', 'wb') as f:
    pickle.dump(b,f)
with open('pickle.txt', 'rb') as f:
    p = pickle.load(f)
    print(p)
k.close()