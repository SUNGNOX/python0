# -*- coding: utf-8 -*-
#2017.9.2

#单元测试
class Dict(dict):

    def __init__(self, **kw):
        dict.__init__(self, **kw)
        # super(Dict, self).__init__(**kw)
        # super().__init__(**kw)#python2中不行

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# D =Dict()
# D['a']=1
# D['b']=2
# print(D['a'])

D =Dict(a=1, b=2)
print(D)
D.c
