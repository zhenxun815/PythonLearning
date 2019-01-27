#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: TestZipFile2.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/1/27 22:50
import os
import time
from zipfile import ZipFile


def verify_dir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


source = ['D:/python_work/test_source/test0.txt', 'D:/python_work/test_source/test1.txt']
target_dir = 'D:/python_work/test_source/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

verify_dir(target_dir)
verify_dir(today)

comment = input('enter comment..')

if len(comment) == 0:
    zip_file = today + os.sep + now + '.zip'
else:
    zip_file = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

with ZipFile(zip_file, 'w') as myzip:
    for file in source:
        myzip.write(file)
