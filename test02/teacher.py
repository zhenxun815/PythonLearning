#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: teacher.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/8/19 10:10 PM
from test02.person import Person


class Teacher(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary
        print('Initialized Teacher: {}'.format(self.name))

    def tell(self):
        Person.say_hi(self)
        print('Salary: {:d}'.format(self.salary))
