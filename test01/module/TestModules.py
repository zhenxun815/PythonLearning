#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 所有的.py程序都是一个module
# @File: TestModules.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/1/8 22:09

from module import Module1
from module.Module2 import __version__, fun

"""
for i in sys.argv:
    print('argv:', i)

print('\n\n The PYTHONPATH is ', sys.path, '\n')

print('current working dir:', os.getcwd())
print('current working pid:', os.getppid())
"""

"""
print('Module1 version:', Module1.__version__)
print('Module2 version:', __version__)
Module1.fun()
fun()
"""

# dir()函数返回一个list,list中为module里包含的函数,类,变量
print(dir())
print(dir(Module1))
