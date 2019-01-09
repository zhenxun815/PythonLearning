#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: TestDataStructures.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/1/9 22:36

# List: 类比Java中List,有序,长度可变,元素可重复


"""
fruits = ['apple', 'mongo', 'carrot', 'banana', 'mongo']

print('length of fruits:', len(fruits))

for item in fruits:
    print(item, end=' ')

fruits.append('rice')
print('fruits is:', fruits)

fruits.sort(reverse=True)
print('sorted reverse:', fruits)

print('first element in fruits:', fruits[0])
del fruits[0]
print('first element in fruits after delete:', fruits[0])

print('index of', fruits[1], 'is', fruits.index(fruits[1]))
print('fruits has', fruits.count('mongo'), 'mongo')


def join_by(delimiter):
    if type(delimiter) == str:
        return delimiter.join(fruits)


print(join_by('@@@'))
"""

"""
# Tuple:类比Java中数组,有序,长度不可变,元素可重复
# 可以不加括号
tuple1 = ('apple', 'mongo', 'carrot', 'banana', 'mongo')
print('tuple1:', tuple1)
print('tuple1 length:', len(tuple1))

# 二维数组
tuple2 = ('java', 'python', tuple1)
print('tuple2:', tuple2)
print('tuple2 length:', len(tuple2))
print('tuple2[2][2]:', tuple2[2][2])
print('tuple2[2][2][2]:', tuple2[2][2][2])

# 声明一个只有一个元素的数组
tuple3 = ('single',)
tuple4 = ('single')
print('type of tuple3', type(tuple3))
print('length of tuple3', len(tuple3))
print('type of tuple4', type(tuple4))
print('length of tuple4', len(tuple4))
"""

# Dictionary:类比Java中Map,key-value

"""
hero = {
    'superman': 'dc',
    'batman': 'dc',
    'ironman': 'marvel',
    'antman': 'marvel'
}


def print_hero(msg='print hero info:'):
    print(msg)
    for name, company in hero.items():
        print('name:', name, ', company:', company)


def print_name():
    print('print names:')
    for name in hero:
        print(name, end=' ')
    print()


print_name()

print_hero()
print('length of hero', len(hero))
print('superman is from:', hero['superman'])

del hero['superman']
print_hero('delete superman...')

hero['deadpool'] = 'marvel'
print_hero('add deadpool')

if 'deadpool' in hero:
    print(hero['deadpool'])
"""

# Sequence:Tuple,List,string都是Sequence,
# Sequence 都可以对元素进行in 或者 not in 判断
# Sequence 支持通过角标(index)操作元素,负号表示倒数,-1倒数第一个
# Sequence 支持slice操作,[start(include):end(exclude):step]
"""

character_list = ['a', 'b', 'c', 'd', 'e']
# 包头不包尾,下面两个输出结果相同
print('list[1:3]:', character_list[1:3])
print('list[1:-1]:', character_list[1:-2])
print('list[:-]:', character_list[:])
print('list[::2]:', character_list[::2])

character_str = 'abcde'
print('str[1:3]:', character_str[1:3])
print('str[1:-1]:', character_str[1:-2])
print('str[:]:', character_str[:])
print('str[::2]:', character_str[::2])
"""

# Set:类比Java中Set,无序,不重复
"""
bri = set(['brazil', 'russia', 'india', 'india'])
print('bri:', bri)  # bri: {'india', 'russia', 'brazil'}
print('length of bri:', len(bri))  # length of bri: 3

bric = bri.copy()
bric.add('china')

bric.issuperset(bri)
bri.remove('russia')

# 求交集
print('bri & bric:', bri & bric)
br = bri.intersection(bric)
print(br)

bru = br.copy()
bru.add('usa')
# 求差集
print('bri ^ bru:', bri ^ bru)
print(bru.difference(bric))

# 求并集
print('bri | bru:', bri | bru)
print(bri.union(bru))
"""

# 注意!!
"""
print('直接赋值')
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist  # 指向同一内存地址
del shoplist[0]
print('shoplist is', shoplist)  # shoplist is ['mango', 'carrot', 'banana']
print('mylist is', mylist)  # mylist is ['mango', 'carrot', 'banana']

print('复制')
mylist = shoplist[:]  # 创建新的内存
del mylist[0]
print('shoplist is', shoplist)  # shoplist is ['mango', 'carrot', 'banana']
print('mylist is', mylist)  # mylist is ['carrot', 'banana']
"""
