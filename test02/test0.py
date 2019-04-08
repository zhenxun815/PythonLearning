#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: test variables
# @File: test0.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/8/19 10:31 PM

from test02.person import Person

p1 = Person('Yiheng', 30)
p1.say_hi()
Person.how_many()

p2 = Person('test', 99)
p2.say_hi()
Person.how_many()

print('kill test')
p2.die()
Person.how_many()
