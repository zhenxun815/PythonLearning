#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: student.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/8/19 10:22 PM

from test02.person import Person


class Student(Person):
    def __init__(self, name, age, marks):
        Person.__init__(self, name, age)
        self.marks = marks
        print('Initialized Student: {}'.format(self.name))

    def tell(self):
        Person.say_hi(self)
        print('Marks is {:d}'.format(self.marks))
