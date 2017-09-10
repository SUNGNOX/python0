#用type定义的元类
def fn(self):
    print('method!')
Hello = type('Hello', (object, ), dict(a=1,b=2,hello=fn))
s=Hello()
print(s.hello())
print(s.a)
print('************metaclass*******************')
#metaclass
class MetaclassFn(type):
    def __new__(cls, name, base, attrs):
        if name=='Model':
            return type.__new__(cls, name, base, attrs)
        print('Call metaclass!!')
        return type.__new__(cls, name, base, attrs)


class Model(dict, metaclass=MetaclassFn):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
        
        self['city'] = 'XIAN'
    @property
    def talk(cls):
        cls._talk = 'Can you talk with me!!!!'
        return cls._talk

class User(Model):
    print('User!!')

c=User()
print(c.talk)
print(c['city'])
print('************list*******************')
#****************list**********************
class Model0(list):
    def __init__(self):
        super(Model0, self).__init__()
        self.name='philip'
    @property
    def talk(cls):
        cls._talk = 'Can you talk with me!!!!'
        return cls._talk
    def __str__(cls):
        return 'I\'m a list!!'

c=Model0()
c.append('lenov')
c.append('xiaomi')

print(c.name)
print(c[0])
print(c[1])
