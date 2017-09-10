class Screen(object):
#    def __init__(self, width, height):
#        self.width=width
#        self.height=height
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, str):
            raise ValueError('width非法属性！！！')
        else:
            self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, (str,)):
            raise ValueError('heigh非法属性！！！')
        else:
          self._height=value

    @property
    def resolve(self):
        self._solve = self._width*self._height
        print('分辨率是%d' % self._solve)
        return self._solve

s=Screen()
s.height=768
s.width=1024
s.resolve
#s.resolve=123