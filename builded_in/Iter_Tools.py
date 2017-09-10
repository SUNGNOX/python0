import itertools
print('从2开始计数')
co = itertools.count(2)
for i in co:
    if i == 5:
        break
    print(i)

print('重复序列！')
cy = itertools.cycle('a,bc')
n = 1
for i in cy:
    if n == 9:
        break
    print(i)
    n = n+1

print("'a'重复3次")
re = itertools.repeat('a', 3)
for i in re:
    print(i)

print("把两个迭代器组合起来")
ch = itertools.chain('abc', co)
for i in ch:
    if i == 10:
        break
    print(i)

print('挑出相邻的相同元素！')
gr = itertools.groupby('aabb  cc ddee  eaaa ')
for key, i in gr:
    print(key, '=>', i, tuple(i))
