# -*- coding:utf-8 -*-
#2017.9.9
#关于yield的方法探究

def myGenerator():
    value = 1
    while True:
        try:
            print(value + 10)
            yield value
            print(value+100)
            value += 1
        except Exception:
            print('............%s')


gen = myGenerator()
#说明
#第一次调用从函数头开始到yield语句输出
print(gen.next())#python27
#接下来的调用从yield的下条语句开始，循环一次再到yield语句输出
print(next(gen))#python27, python34
#throw语句的运行顺序一样，生成器收到异常后略过except异常处理之前的语句继续循环执行到yield语句输出
gen.throw(Exception, "Method throw called!")#throw