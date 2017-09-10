def add_val(L=[]):
    L.append('end')
    return L

add_val()
add_val()
#L = [1,2,3]
#L.append(4)
print(add_val())
print(add_val())
##########################
def add_val1(L=None):
    if L is None:
        L=[]
    L.append('end')
    return L
#调试：
add_val1()
add_val1()
print(add_val1())

###########################参数组合
def func(a,b,c=0,*args,d,**kw):
    print(a,b,c,args,d,kw)

func(2,1,0,*['k1','k2'],d=3,**{'w':1,'e':2})
func(2,1,d=3,**{'w':1,'e':2})
func(2,1,0,'k1','k2',d=3,**{'w':1,'e':2})
func(2,1,d=3)
#########################
def func1(a,b,c=0,*,d,**kw):
    print(a,b,c,d,kw)

func1(2,1,d=3,**{'w':1,'e':2})

#################################尾递归
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(3,1))
