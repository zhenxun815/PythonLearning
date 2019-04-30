#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Description: 
# @File: io_pickle.py
# @Project: PythonLearning
# @Author: Yiheng
# @Email: GuoYiheng89@gmail.com
# @Time: 4/11/19 10:33 PM
import pickle

shop_list_file = 'shop_list.data'
shop_list = ['apple', 'mango', 'carrot']

with open(shop_list_file, 'wb') as f:
    pickle.dump(shop_list, f)

del shop_list

with open(shop_list_file, 'rb') as f:
    store_list = pickle.load(f)
    print(store_list)
