# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:08:03 2022

@author: USER
"""
S = {1,2,3,4,5,6,7,8,9,10}
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(S-A)
print(A^B)
print(A|B)
print(A^B == A|B)
print(5 in A|B)
print(S-(A&B))
print((S-A)|(S-B))
print(S-(A&B) == (S-A)|(S-B))