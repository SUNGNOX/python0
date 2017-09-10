class Father(object):
    def func(self):
        print('I\'m your father!!')

class Pat(object):
    def func(self):
        print('I\'m your pat!!')
#***************************************
class my_class(Pat, Father):
    pass

s = my_class()
s.func()
#***************************************
class my_class(Father, Pat):
    pass

s = my_class()
s.func()