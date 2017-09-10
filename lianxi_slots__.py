class S0(object):
    __slots__=('hight','name')#__slots__只对实例绑定属性有限制
class S1(S0):
    pass
 #   __slots__ = ('home', 'town')

S=S1()
S.t=174
print(S.t)