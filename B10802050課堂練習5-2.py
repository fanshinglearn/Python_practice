# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:06:20 2022

@author: USER
"""

score = 0
sum = 0
high_score = 0
low_score = 100
count = 0

A = [89, 56, 92 ,79, 51]
B = [70, 86, 77, '缺考', 83]
C = []
D = []

for i in range(0,len(A)):
    if '缺考' in str(A[i]):
        print ('期中考 %d 號缺考'%i)
        break
else:
    print('期中考沒人缺考')

for i in range(0,len(B)):
    if '缺考' in str(B[i]):
        print ('期末考 %d 號缺考'%i)
        break
else:
    print('期中考沒人缺考')

for i in range(0,len(A)):
    if (A[i] == '缺考') or (B[i] == '缺考'):
        C.append('缺考')
    else:
        score = (A[i] + B[i]) / 2
        sum += score
        high_score = max(score, high_score)
        low_score = min(score, low_score)
        C.append(score)
        count += 1

print('學期平均分數是 %.1f 分，最高分是 %d 號 %.1f 分，最低分是 %d 號 %.1f 分。'%(sum / count, C.index(high_score), high_score, C.index(low_score), low_score))

sum = 0
high_score = 0
low_score = 100
count = 0

for i in range(0,len(A)):
    if (A[i] == '缺考') or (B[i] == '缺考'):
        D.append('缺考')
    else:
        score = (A[i] * 40 + B[i] * 60) / 100
        sum += score
        high_score = max(score, high_score)
        low_score = min(score, low_score)
        D.append(score)
        count += 1

print('重新計算後\n學期平均分數是 %.1f 分，最高分是 %d 號 %.1f 分，最低分是 %d 號 %.1f 分。'%(sum / count, D.index(high_score), high_score, D.index(low_score), low_score))
