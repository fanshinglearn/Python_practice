# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 23:08:13 2022

@author: USER
"""

input_msg = ''
count = 0
sum = 0
high_score = 0
low_score = 100
while True:
    count += 1
    input_msg = input('請輸入第 %d 位學生的成績：' %count)
    if input_msg == '結束':
        break
    score = int(input_msg)
    sum += score
    high_score = max(high_score, score)
    low_score = min(low_score, score)
print('平均分數： %.2f 分，最高分： %d ，最低分： %d ' %(sum / (count - 1), high_score, low_score))