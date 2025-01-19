# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 23:08:13 2022

@author: USER
"""

#for
n = 1
for i in range(1,100):
    n *= i
    if n > 100000:
        print('最小的 n 值是%d'%i)
        break

#while
n = 1
i = 0
while True:
    i += 1
    n *= i
    if n > 100000:
        print('最小的 n 值是%d'%i)
        break