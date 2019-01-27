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


def verify_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


source = ['D:/python_work/test_source/test0.txt', 'D:/python_work/test_source/test1.txt']
target_dir = 'D:/python_work/test_source/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

verify_dir(target_dir)
verify_dir(today)

comment = input('enter commnent...')

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('zip command is: ')
print(zip_command)
print('Running:')

if os.system(zip_command) == 0:
    print('success backup to:', target)
else:
    print('back failed')
