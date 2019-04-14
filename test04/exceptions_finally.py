#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: exceptions_finally.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/14/19 5:40 PM
import sys
import time

f = None
try:
    f = open('test.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print('Press ctrl+c now')
        time.sleep(5)
except IOError:
    print('Could not read test.txt')
except KeyboardInterrupt:
    print('User cancelled')
finally:
    if f:
        f.close()
    print('Cleaning up: Closed the file')
