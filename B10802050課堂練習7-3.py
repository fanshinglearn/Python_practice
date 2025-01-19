# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:08:03 2022

@author: USER
"""
animal1 = {'dog', 'cat', 'bird', 'sheep', 'pig'}
animal2 = {'dog', 'horse', 'mouse', 'cat', 'bird'}
for i in range(len(animal1)):
    x = animal1.pop()
    if x in animal2:
        animal2.remove(x)
print(animal2)

animal1 = {'dog', 'cat', 'bird', 'sheep', 'pig'}
animal2 = {'dog', 'horse', 'mouse', 'cat', 'bird'}
print(animal2-(animal1&animal2))