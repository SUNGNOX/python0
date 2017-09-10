# -*- coding:utf-8 -*-
#2017.9.5
from collections import namedtuple
# namedtuple('名称', [属性list]):
circle = namedtuple('circle', ['x','y','z'])#'名称'参数不影响结果
# point = namedtuple('point', ['x','y'])
c = circle(2,3,4)
print(c.z)
###############################
from collections import deque
c = deque(['x', 'y', 'z'])
c.append('w')
c.appendleft('c')
print(c)
c.pop( )
c.popleft( )
print(c)
#################################
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值
#####################################
from collections import OrderedDict
od = OrderedDict(a = 1, b = 2, c = 3)
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
#****************************************#
from collections import Counter
c = Counter()
for aph in 'alphabate':
    c[aph] = c[aph] + 1

print(c)
