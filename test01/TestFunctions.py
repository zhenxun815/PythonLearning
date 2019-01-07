#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: TestFunctions.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/1/6 22:25

"""
def print_max(num_a, num_b):
    '''
    DocStrings,文档字符串
    :param num_a: value a
    :param num_b: value b
    :return: the bigger one between num_a and num_b
    '''
    if num_a > num_b:
        return num_a
    elif num_a < num_b:
        return num_b
    else:
        print(num_a, 'is equal to ', num_b)
        return num_a


a = input('input a: ')
b = input('input b: ')

print(print_max(a, b))
# 打印文档
print(print_max.__doc__)

"""

"""
# 默认实参值,Default Argument Values

def print_with_time(msg, times=1):
    print(msg * times)


print_with_time('hello')
print_with_time('world', 5)
"""

"""
# 关键字实参,Keyword Arguments
# 不用考虑参数顺序

def func(a, b=5, c=10):
    print('a:', a, 'b:', b, 'c:', c)


func(1)
func(c=20, a=30)
"""

"""
# 可变参数,VarArgs parameters
# * 表示元组tuple,** 表示字典dictionary

def total(a=5, *numbers, **phonebook):
    print('a', a)

    # 遍历元组
    for num in numbers:
        print('num:', num)

    # 遍历字典
    for key, value in phonebook.items():
        print('key:', key, 'value:', value)


total(0, 1, 2, 3, aa=10, bb=20, cc=30)
# 输出:
# a 0
# num: 1
# num: 2
# num: 3
# key: aa value: 10
# key: bb value: 20
# key: cc value: 30
"""



