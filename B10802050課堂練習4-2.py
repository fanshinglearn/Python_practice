# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:34:06 2022

@author: USER
"""

year = input("年分 : ")
print(year, " 年是閏年 is ",(year%4 == 0 and year%100 != 0) or year%400 == 0)