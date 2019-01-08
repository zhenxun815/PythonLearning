#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: Module1.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/1/9 1:02

__version__ = 'module1 1.0'


def fun():
    # if __name__ == '__main__' 则为module自身单独运行,否则为被导入到其他module中执行
    if __name__ == '__main__':
        print('module1 running by self...')
    else:
        print('module1 being imported...')


# 被导入时会自动执行
fun()
