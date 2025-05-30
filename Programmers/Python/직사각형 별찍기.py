# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:49:16 2022
@FileName: 직사각형 별찍기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12969
"""


a, b = map(int, input().strip().split(' '))
for i in range( b ):
    print( "*" * a );