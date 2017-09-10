#__len__, __slots__, __str__, __iter__, __getitem__, __getattr__, __call__

#可迭代的类
class Iter(object):
    def __init__(self):
        self.a = 0
        self.b = 1
    def __len__(self):
        return 2
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a
print(type(Iter)) #<class 'type'>
s=Iter()
for n in Iter():
    print(n)
print(len(s))
#***************************************
#类作为列表
class Getitem(object):
    def __getitem__(self, n):
        L = []
        for i in range(n):
            L.append(i)
        print(list(L))

s = Getitem()
s[5]
#***************************************
#类作为函数调用
class Call(object):
    def __init__(self):
        self.name='Tom'

    def __call__(self):
        print( '类作为函数调用')
        return '类作为函数调用,name: %s' % self.name

    def __str__(self):
        return 'object'

s=Call()
print(s)
#***************************************
#用__getattr__实现链式调用
class Getattr(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Getattr('%s/%s' % (self._path, path))
 #   def __str__(self):
 #      return self._path

print(Getattr('').a.b.c.d._path)

#***************************************
#__getattr__、 __setattr__
class Getattr0(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self,attr):
        return self.attr
    def __setattr__(self, attr, value):
        self.__dict__['attr'] = value

 #   def __str__(self):
 #      return self._path
s=Getattr0('')
s.m = 200
print(s.m)
