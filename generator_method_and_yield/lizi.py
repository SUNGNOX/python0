class SpamException(Exception):
    pass

def writer():
    while True:
        try:
            w = (yield)
        except SpamException:
            print('***')
        else:
            print('>> ', w)


def writer_wrapper(coro1):
    coro1.send(None)  # 生成器准备好接收数据
    while True:
        try:
            try:
                x = (yield)  # x接收send传进的数据
                coro1.send(x)  # 然后将x在send给writer子生成器
            except Exception as er:
                coro1.throw(er)
        except StopIteration:    # 处理子生成器返回的异常
            pass


w = writer()
wrap = writer_wrapper(w)
wrap.send(None)  # "prime" the coroutine
for i in [0, 1, 2, 'spam', 4, 4, 4]:
    if i == 'spam':
        wrap.throw(SpamException)
    else:
        wrap.send(i)