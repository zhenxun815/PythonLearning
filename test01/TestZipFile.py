#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: TestZipFile.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/1/27 13:11
import os
import time

source = ['D:/python_work/test_source/test0.txt', 'D:/python_work/test_source/test1.txt']
target_dir = 'D:/python_work/test_source/backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('zip command is: ')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
    print('success backup to:', target)
else:
    print('back failed')
