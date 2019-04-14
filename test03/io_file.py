#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: io_file.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/9/19 9:36 PM

text = 'something to write'

f = open('test.txt', 'w')
f.write(text)
f.close()

f = open('test.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

f.close()

# recommend
print('###################')
with open('test.txt') as f:
    for line in f:
        print(line)
