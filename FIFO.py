#https://my.oschina.net/lvyi/blog/383454
#!/usr/bin/env python
#-*- coding: utf8 -*-
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        #super(LastUpdatedOrderedDict, self).__init__()
        OrderedDict.__init__(self)#注意这里有self
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        super(LastUpdatedOrderedDict, self).__setitem__(key, value)
        #OrderedDict.__setitem__(self, key, value)

FIFO = LastUpdatedOrderedDict(5)
FIFO.__setitem__('huangyi', 'lz')
FIFO.__setitem__(1, 1)
FIFO.__setitem__(1, 1)
FIFO.__setitem__(2, 2)
FIFO.__setitem__(3, 3)
FIFO.__setitem__(4, 4)
FIFO.__setitem__(5, 5)