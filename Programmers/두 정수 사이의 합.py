# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:34:45 2022
@FileName: 두 정수 사이의 합.py
@author: YUNJUSEOK
https://programmers.co.kr/learn/courses/30/lessons/12912
"""

def solution(a, b):
    ran = range( a, b + 1 ) if a < b else range( b, a + 1 )
    return sum( [ i for i in ran ])

