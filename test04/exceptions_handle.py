#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: exceptions_handle.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/14/19 4:58 PM

try:
    text = input('enter someting...')
except EOFError:
    print('catch a EOF!')
except KeyboardInterrupt:
    print('user cancelled')
else:
    print('user entered {}'.format(text))
