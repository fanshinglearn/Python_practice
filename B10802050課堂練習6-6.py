# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:08:03 2022

@author: USER
"""

怪獸 = ['哥吉拉', '魔斯拉', '迷你拉', '巴特拉', '基多拉', '伊比拉', '蝶龍', '安基拉斯', '金剛']
while 怪獸:
    index_monster = 怪獸.pop()
    if '拉' in index_monster:
        print(index_monster)
