#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: test inheritance
# @File: test1.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/8/19 10:18 PM
from test02.teacher import Teacher
from test02.student import Student

t = Teacher('Mr Guo', 40, 10000)
s = Student('tt', 20, 99)

t.tell()
s.tell()

print('#############')

members = [t, s]
for member in members:
    member.tell()
