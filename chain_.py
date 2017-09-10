#实现链式调用
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def show(self):
        return 'API:%s' % self._path

p = Chain()
print(Chain().a.b.c.e.show())