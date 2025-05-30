# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:15:40 2022
@FileName: 내적.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/70128
"""
def solution(a, b):
    sum = 0 ; 
    for i in range( len( a ) ):
        sum += a[ i ] * b[ i ];
    
    return sum

