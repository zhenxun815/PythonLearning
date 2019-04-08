#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: io_input.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/8/19 11:47 PM


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input('Enter text: ')
if is_palindrome(something):
    print('Yes')
else:
    print('No')
