#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hello,python,world
# print('hello', 'python', 'world', sep=',', end='\n')

# 100 + 200 = 300
# print('100 + 200 =', 100 + 200)

# name = input('enter a name:')
# print('name =', name)

# r'',单引号中间内容默认不转义,但是只写一个转移符\会报错
# 输出:'
# print('\'')
# 输出:\'
# print(r'\'')

# 三个引号可以实现输出内容内部换行
"""
print('''换行
换行
换行''')

print(r'''\'换行
\'换行
\'换行''')

print('''\'换行
\'换行
\'换行''')
"""
# Python中布尔值True,False首字母大写
# Python中逻辑运算符为and,or,not,也可以用&,|,但是没有!,也没有&&和||
# print(3 < 2)
# print(not True)
# print(True | False)
# print(True or False)

# 结果:3.3333333333333335
# print(10/3)
# //向下取整除,结果:3
# print(10//3)

# b''表示bytes类型
# str -> bytes,默认转为utf-8
# print('一恒'.encode())
# bytes -> str
# print(b'\xe4\xb8\x80\xe6\x81\x92'.decode('utf-8'))

# 字符数,结果:2
# print(len('一恒'))
# 字节数,结果:6
# print(len(b'\xe4\xb8\x80\xe6\x81\x92'))

# 占位符%s:字符串,%d:整数,%f:浮点数,%x:十六进制数,%%:转义%
# 结果:hello, 一恒
# print('hello, %s' % '一恒')
# 结果:hello, 一恒, you have $100
# print('hello, %s, you have $%d' % ('一恒', 100))
# 结果:  3 , 01
# print('%3d , %02d' % (3, 1))
# 结果:3 , 3.14
# print('%.0f , %.2f' % (3.1415926, 3.1415926))
