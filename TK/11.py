import functools


def log(func):
    if isinstance(func, (str,int)):
        def decorator(func_):
            @functools.wraps(func_)
            def wraper(*args, **kw):
                print('%s %s():' % (func, func_.__name__))
                def end():
                    print('%s excute finall!!' % func_.__name__)
                return func_(*args, **kw), end()
            return wraper
        return decorator
    else:
        @functools.wraps(func)
        def wraper(*args, **kw):
            print('%s():' % func.__name__)#出了个错误，__name__写成了__name_，不知何时丢了个下划线
            func(*args, **kw)
            print('end!!!!!!!!')
            return
        return wraper

#@log('excute')
@log
def now():
    print('2017-7-14')
now()


#@log('excute')
def f_square():
    fs = []
    def f(j):
 #       def g():
 #           return j*j
 #       return g
        g = lambda: j*j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f = f_square()

f1=f[0]
f2=f[1]
f3=f[1]
print(f1())
print(f2())
print(f3())
#print(f)