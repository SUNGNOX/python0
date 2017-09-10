#***************************************
#__getattr__、 __setattr__
class Getattr0(object):
    def __init__(self, path):
        self.path = path
    def __setattr__(self, attr, value):
        self.__dict__['attr'] = value
        return self.attr
    def __getattr__(self,attr):
        return self.attr


s=Getattr0('')
s.a=2
print(s.a)