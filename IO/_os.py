# -*- coding: utf-8 -*-
#2017.9.3
from os import path
import os
import shutil

print(path.isdir('_os.py'))
print(path.abspath('.'))
print(path.dirname('__file__'))

shutil.copyfile('test', 'oh')
