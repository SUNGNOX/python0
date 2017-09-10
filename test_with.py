# -*- coding: utf-8 -*-
#2017.9.3
# with open('error.txt', 'r') as f:
#     for line in f.readlines():
#         print(line)
# f = open('error.txt', 'r', encoding='gbk')
# for line in f.readlines():
#     print(line.strip())#strip()去掉末尾的'\n'
# print(f)
# f.close()

f = open('error.txt', 'r')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
print(f.readlines())
print(type(f.readline()))
f.close()

with open('json.txt', 'r', errors='ignore') as f:
    for line in f.readlines():
        print(line)

print(f)