# -*- coding: utf-8 -*-
#2017.9.2
#enumerate
L = ['app', 'table','horse']
for key, value in enumerate(L):
    print('%d=>%s' % (key, value))

#枚举类的使用, 有三种表示方法
from enum import Enum, unique
Animal = Enum('Animal', 'ant bee cat dog')
Things = Enum('Things',('app', 'table','horse'))
for name, member in Animal.__members__.items():
    print(name, '=>', member, ',', member.value)
for name, member in Things.__members__.items():
    print(name, '=>', member, ',', member.value)

print(Animal.__members__)#OrderedDict

try:
    @unique
    class Animals(Enum):
        ant = 1
        bee = 2
        cat = 1
        dog = 4
    #抛出ValueError错误, 因为ant和cat的值一样
    for name, member in Animals.__members__.items():
        print(member.value)
except ValueError as er:
 #   print(ValueError('error:ValueError!!'))#自定义错误输出
    print('ValueError error:',er)
finally:
    print('finally!!')



try:
    10/0
except ZeroDivisionError:
    print(ZeroDivisionError('error:ZeroDivisionError'))
 #  print('ZeroDivisionError error:',er)
finally:
    print('finally!!')

A={'1':1,'2':2}
