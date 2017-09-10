# -*- coding: utf-8 -*-
#2017.9.2
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)#python27/python35
        # super().__init__(**kw)#python35
        self.N = None
        self.key = None

    def __getattr__(self, key):
        try:
            S = self[key]
            # print('unknow attribute!')
            return S
        #以上只会抛出KeyError
        except KeyError as er:
            #若属于AttributeError则抛出以下错误否则还是KeyError
            # print(isinstance(er, AttributeError))
            # print(isinstance(er, KeyError))
            # raise#不跟异常类型，trace信息在try语句块的错误处截断
            raise AttributeError("'Dict' object has no attribute '%s'" % key)#捕获异常后又重新抛出另一个异常会导致trace信息在此处截断
            # raise KeyError('没有这项！！')#捕获异常后尽量不要抛出统一异常
        # finally:
            # print('finally!')

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # D =Dict(a=1, b=2)
    # D['a']
    # D['c'] = 2
    # print('D.c')
    #
    # try:
    #     print(D.d)
    # except KeyError:
    #     print('D.d: error!!!!!!!!!!')
    #
    # # D.d#AttributeError
    # print(r"D['d']")
    # try:
    #     D['d']#KeyError
    # except KeyError:
    #     print("D['d']: error!!!!!!!!!!")