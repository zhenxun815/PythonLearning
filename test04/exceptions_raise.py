#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: exceptions_raise.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/14/19 5:17 PM


class ShortInputException(Exception):
    """MY custom exception class."""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something..')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('catch a EOF...')
except ShortInputException as ex:
    print('ShotInputException: The input was {0} long, '
          'expected at least {1}'.format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
