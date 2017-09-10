# -*- coding: utf-8 -*-
import os
print(os.getcwd())
import sys
# print(sys.path)
# sys.path.append(r"D:\python0\web_development\wsgi")
# from dir.hello import application
from dir import application#pycharm标记有问题，诸如此情况会有红色波浪下划线。而from .dir import application语法错误，而无标记
# from hello import application

from wsgiref.simple_server import make_server

httpd = make_server('127.0.0.1', 8000, application)

print('Serving HTTP on port 8000...')

httpd.serve_forever()
