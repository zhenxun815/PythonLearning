#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print 函数,print(self, *args, sep=' ', end='\n', file=None)
# hello,python,world
# print('hello', 'python', 'world', sep=',', end='\n')
# print('hello', end=',')
# print('python',  end=',')
# print('world', end='')

# name = input('enter a name:')
# print('name =', name)

# Raw String
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
# 字符串内\表示不换行
# line = "This is the first sentence. \
# This is the second sentence."
# print(line)

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

# format函数
# 通过位置指定
# age = 20
# name = 'Yiheng'
# print('name: {0} ,age: {1}'.format(name, age))
# 通过字典指定
# info = {'age': 20, 'name': 'Yiheng'}
# print('age: {age}, name: {name}'.format(**info))
# 通过关键字指定
# print('age: {age}, name: {name}'.format(age=20, name='Yiheng'))
# 二进制
# print('{:b}'.format(250))
# 八进制
# print('{:o}'.format(250))
# 十进制
# print('{:d}'.format(250))
# 十六进制
# print('{:x}'.format(250))
# 小数点后显示位数:0.333,0.3333
# print('{0:.3f},{1:.4f}'.format(1.0 / 3, 1.0 / 3))
# 下划线补齐宽度,文字居中显示:___hello___
# print('{0:_^11}'.format('hello'))
# f-string
# age = 20
# name = 'Yiheng'
# print(f'name is: {name}, age: {age}')
