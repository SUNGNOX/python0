# -*- coding:utf-8 -*-
#2017.9.9


class SignException(Exception):
    pass


def tree():
    num = 0
    while True:
        try:
            n = yield num
            print('有 %d 棵树' % n)
            num += n
        except SignException:
            print('........')
        except TypeError:
            print('tree ResultException!')
            return num#只要有返回运算结果的或break都会引发StopIterator异常

#yield from 的参考实现
def tool():
    ntree = tree()
    num = 0
    print('哇！好多树！！')
    ntree.send(None)
    while True:
        try:
            m = yield num
            num = ntree.send(m)
        except StopIteration:#tree()的return语句会在tool()中引发StopIteration错误，退出循环，之后在主程序中引发StopIteration错误
            break
        except Exception as er:
            # print('tool Exception!')
            ntree.throw(er)
    print('就这么多棵树呀！%d' % num)


# def tool():
#     print('哇！好多树！！')
#     while True:
#         num = yield from tree()
#         print('就这么多棵树呀！%d' % num)

# #使用yield from实现
# def tool():
#     print('哇！好多树！！')
#     num = yield from tree()
#     print('就这么多棵树呀！%d' % num)


its = tool()
L = [1,1,0,1,0,2,1,0]
its.send(None)
for i in L:
    if i == 0:
        its.throw(SignException)
    else:
        its.send(i)

# its.send(None)

try:
    its.send(None)
except StopIteration:
    print( "end!")

