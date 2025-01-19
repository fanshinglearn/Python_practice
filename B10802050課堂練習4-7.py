# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:48:18 2022

@author: USER
"""

import random

x = random.randrange(1,101)

if x % 2 !=0:
    if x > 50:
        y = x - 50
    else:
        y = x * 1.5
else:
    if x >70:
        y = x - 20
    else:
        y = x / 10

print("原本數值 : ", x)

print("轉換後數值 :", y)