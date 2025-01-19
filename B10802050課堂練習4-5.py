# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:48:18 2022

@author: USER
"""

import random

x = random.randrange(1,6)

y = input("猜測整數值 : ")

y =int(y)

if y < x:
    print("數字太小，答案是",x)
elif y > x:
    print("數字太，答案是",x)
else:
    print("猜對了")