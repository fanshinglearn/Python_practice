# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:33:14 2022

@author: USER
"""

list1 = [1, 2, 3, 4]
list1_append = [1, 2, 3, 4]
list1_extend = [1, 2, 3, 4]

list1_append.append([5, 6, 7, 8])
list1_extend.extend([5, 6, 7, 8])

print('目前串列內容 = ', list1_append)
print('目前串列內容 = ', list1_extend)
print()

list1_append.append('test')
list1_extend.extend('test')

print('目前串列內容 = ', list1_append)
print('目前串列內容 = ', list1_extend)
print()

list1_append.append(['a', 'b', 'c'])
list1_extend.extend(['a', 'b', 'c'])

print('目前串列內容 = ', list1_append)
print('目前串列內容 = ', list1_extend)
print()

list1_append.append('阿貓')
list1_extend.extend('阿貓')

print('目前串列內容 = ', list1_append)
print('目前串列內容 = ', list1_extend)
print()

list1_append.append(['阿貓', '阿狗'])
list1_extend.extend(['阿貓', '阿狗'])

print('目前串列內容 = ', list1_append)
print('目前串列內容 = ', list1_extend)
print()

list1_append.append(0)
list1_extend.extend(0)

print('目前串列內容 = ', list1_append)
print('目前串列內容 = ', list1_extend)
print()