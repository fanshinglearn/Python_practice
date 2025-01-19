# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:44:38 2022

@author: USER
"""

t = ('吃', '葡', '萄', '不', '吐', '葡', '萄', '皮', '不', '吃', '葡', '萄', '倒', '吐', '葡', '萄', '皮')

print(t[::2])
print(t.index('葡'))
print(t.index('葡',2))
t2=t[::2]
print(t2.count('葡'))