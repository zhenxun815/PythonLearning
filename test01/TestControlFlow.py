#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: TestControlFlow.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 2019/1/6 19:14

# while 循环
"""
number = 55
flag = True
while flag:
    guess = int(input('Enter aninteger: '))
    if guess < number:
        print('Higher...')
    elif guess > number:
        print('Lower...')
    else:
        flag = False
else:
    print('Congratulation!')

print('Loop has finished')
"""

# for循环
"""
for i in range(1, 10, 2):
    print(i)
else:
    print('Loop has finished...')
"""

# break

while True:
    str = input('Enter command: ')

    if 'quit' == str:
        break
    elif 'copy' == str:
        print('Input is: ' + str)
    else:
        continue
print('Loop has finished...')
