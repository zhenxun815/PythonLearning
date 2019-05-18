#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: programmer
# @Project: PythonLearning
# @Author: yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/5/18 下午8:49


class Programmer(object):
    hobby = 'programming'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('name is {0}, age is {1}'.format(self.name, self._age))


if __name__ == '__main__':
    programmer = Programmer('Yiheng', 30, 70)
    print('programmer dir: {}'.format(dir(programmer)))

    # programmer dict: {'name': 'Yiheng', '_age': 30, '_Programmer__weight': 70}
    print('programmer dict: {}'.format(programmer.__dict__))

    # programmer get_weight :70
    print('programmer get_weight :{}'.format(programmer.get_weight))

    # programmer _Programmer__weight:70
    # print('programmer _Programmer__weight:{}'.format(programmer._Programmer__weight))

    # programmer ger hobby: programming
    print('programmer ger hobby: {}'.format(Programmer.get_hobby()))

    programmer.self_introduction()