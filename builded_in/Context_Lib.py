from contextlib import contextmanager


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

#contextmanager装饰器提供上下文输出，yield语句断开上下文。with语句块中输入正文
@contextmanager
def Query0(m):
    print(u'上文')
    yield
    print(u'下文%d' % m)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()
print('------------我是分割线-----------------')
with Query0(5):
    print('xia wen!!')


print('------------我是分割线-----------------')

#如果一个对象没有实现上下文，我们就不能把它用于with语句。
from contextlib import closing
#closing的实现
@contextmanager
def closing0(thing):
    try:
        yield thing
    finally:
        thing.close()

from urllib.request import urlopen
# #
# with closing(urlopen('https://www.python.org')) as p:
#     for line in p:
#         print(line)
# print(p.read())
pu = urlopen('https://www.python.org')
for line in pu:
    print(line)
pu.close()#关闭不了
print(pu.read())

def Query1():
    return open('a', 'a')

# closing0(Query0(5))
print('------------我是分割线-----------------')
with closing(Query1()) as p:
    p.write('asdsa\n')
    print('正文')
# p.read()
@contextmanager
def Query2():
    try:
        print('开始')
        yield open('a', 'a')
    finally:
        print('结束')
print('------------我是分割线-----------------')
with Query2() as p:
    p.write('crcrev\n')
    p.close()
    p = open('a', 'r')
    print(p.read())
    p.close()

