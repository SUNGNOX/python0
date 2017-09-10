#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2017.9.5
import re
class __regex():
    #正则表达式

    re.match(r'(0[0-9]|1[0-9])\:(2[a-z])', '115:2w')
    #拆分
    SP = re.split(r'\s+', 'wo shi shui!')
    #加'?'防止贪婪匹配
    m = re.match(r'^(\d+?)(0*)$', '1023400000').groups()


r = __regex()
a = re.match(r'(0[0-9]|1[0-9]):(2[a-z])', '11:2w')
s = r.SP
print(s[1])