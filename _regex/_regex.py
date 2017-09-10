#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2017.9.5
class __regex():
    '''
    >>> r = __regex()
    >>> print(r.a)
    <_sre.SRE_Match object; span=(0, 5), match='15:2w'>
    >>> print(r.m)
    ('10234', '00000')
    >>> print(r.SP)
    ['wo', 'shi', 'shui!']
    >>> print(r.p)
    ('wo de dian hua hao ma shi:', '151 9142 6523')
    '''

    #正则表达式
    import re
    a = re.match(r'(0[0-9]|1[0-9])\:(2[a-z])', '15:2w')
    #拆分。生成列表
    SP = re.split(r'\s+', 'wo shi shui!')
    #分组。加'?'防止贪婪匹配
    m = re.match(r'^(\d+?)(0*)$', '1023400000').groups()
    # m = re.match(r'^(\d*?)(0*)$', '1023400000').groups()
    #预编译
    precom = re.compile(r'(wo de dian hua hao ma shi:)(\s?\d{3}\s?\d{4}\s?\d{4})')
    p = precom.match('wo de dian hua hao ma shi:151 9142 6523').groups()

# r = __regex()
if __name__ == '__main__':
    import doctest
    doctest.testmod()
