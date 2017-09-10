# -*- coding: utf-8 -*-
import os
print(os.getcwd())
# import sys
# sys.path.append(r"D:\python0\web_development\wsgi")
from hello import application
from wsgiref.simple_server import make_server

httpd = make_server('127.0.0.1', 8000, application)

print('Serving HTTP on port 8000...')

httpd.serve_forever()
