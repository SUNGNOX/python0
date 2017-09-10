  # !/usr/bin/env python3
 # -*- coding: utf-8 -*-


 # metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='MyList':
            return type.__new__(cls, name, bases, attrs)
        attrs['add'] = lambda self, value: self.append(value)
        attrs['s'] = 'call meatclass!!!!!!!'
        return super(ListMetaclass, cls).__new__(cls, name, bases, attrs)

  # 指示使用ListMetaclass来定制类
#NE = ListMetaclass('NE', (list, ), {})
#print(NE.s)
class MyList(list, metaclass=ListMetaclass):
    print('1')
    pass

class User(MyList):
    a=1
    b=2
    c=3

L = MyList()
print(L.s)
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)
L.pop(0)
print(L)
