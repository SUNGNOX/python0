#! /usr/bin/env pytho3
# _*_ coding: utf-8 _*_
' my modual '
import sys
__author__ = 'sun'


def par_num():
    m = sys.argv
    if len(m) == 1:
        print('hello world!')
    else:
        print('hello %s!' % m[1])

if __name__ == '__main__':
    par_num()
    print(type(par_num))

