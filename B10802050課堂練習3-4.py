# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

age, sex = input().split(' ')

print('姓名 \t年齡 \t性別')
print('_________________')
print('班代 \t%d \t%s'%(age, sex))
print('_________________')

print('姓名 \t年齡 \t性別')
print('_________________')
print('班代 \t{} \t{}'.format(age, sex))
print('_________________')