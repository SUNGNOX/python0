def foo(n):
    m = 10/int(n)
    if n == 0:
        raise ValueError('invalid value: %s' % n)
    return m


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar()