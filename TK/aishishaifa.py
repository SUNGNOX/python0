#1.
s=list(range(2, 10))
L = []

while(len(s) != 0):
    def filter0(m, n=s[0]):
        return m % n != 0
    L.append(s[0])
    s=list(filter(filter0, s))
print(L)
#2.
#产生一个2到无穷的迭代器
def generate0():
    n = 1
    while(True):
        n = n+1
        yield n

#滤波函数,返回一个匿名函数
def lvbo(n):
    return lambda x: x % n > 0

def get_sushu():
    it = generate0()
    while(True):
        n = next(it)
        it = filter(lvbo(n), it)
        yield n


a = get_sushu()
while(True):
    n = next(a)
    if n > 10:
        break
    print(n)
