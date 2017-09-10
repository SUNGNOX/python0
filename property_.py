# -*- coding:utf-8 -*-
#2017.9.2
#property和定制类的使用
class Screen(object):
    __slots__ = ('_width', '_high', 'ite')
    def __init__(self):
        self.ite = 190


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    #只读属性high
    @property
    def high(self):
        self._high = 175
        return self._high

    #配合__iter__使用，使Screen像list和tuple一样可以用于for循环，但不能像list那样访问元素
    def __iter__(self):
        return self

    def __next__(self):
  #      self.ite = self.high
        if self.ite > 200:
            raise StopIteration()
        self.ite = self.ite+5
        return self.ite

    #getitem,，使Screen像list那样能够访问元素
    def __getitem__(self, item):
        #item也可以看成dict的KEY
        if isinstance(item, int):
            item = item+10
            return item
        #slice为切片类型
        if isinstance(item, slice):
            s = item.start
            e = item.stop
            L = []
            for x in range(s,e):
                L.append(x+10)
            return L

    def __setitem__(self, key, value):
        S = dict()
        S[key]=value
        print(S[key])#python27
        return#python27
        # return print(S[key])#python35

    #定义没有初始化的属性，为只读
    def __getattr__(self, attr):
        if attr == 'scale':
            return 256

    #把实例作为函数调用，函数参数为__call__的输入参数
    def __call__(self, s):
        print('__call__参数为: %s!' % s)
        print('把实例作为函数调用，Screen的初始化参数为：%s, %s!' % (self._width, self._high))

    def __len__(self):
        return self.high*self.width

    def __str__(self):
        return '类：Screen'

a = Screen()
print(a)
a.ert

a.width=50
print(a.width)
print(a.high)
print(len(a))
#a.age = 3
#print(a.age)
print(Screen().ite)
for high0 in Screen():
    print(high0)

print(a[15])
print(a[3:5])
a['a']=2
print(a['a'])

print(a.scale)
a('arg')
