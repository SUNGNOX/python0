# -*- coding: utf-8 -*-
#2017.9.2
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)#python27/python35
        # super().__init__(**kw)#python35

    def __getattr__(self, key):
        try:
            # if key not in self:
            #     pass
                # raise AttributeError('没有这项！！')
            return self[key]
        #以上只会抛出KeyError
        except KeyError as er:
            #若属于AttributeError则抛出以下错误否则还是KeyError
            print(isinstance(er, AttributeError))
            print(isinstance(er, KeyError))
            raise AttributeError('没有这项！！')#在语句块中可以抛出除KeyError的所有异常

    def __setattr__(self, key, value):
        self[key] = value


D =Dict(a=1, b=2)
print(type(D))
print(D)
D.c = 2
print(D.c)
# D.d#AttributeError
D['d']#KeyError
