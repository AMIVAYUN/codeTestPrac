# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:44:41 2022
@FileName: 나머지가 1이 되는 수 찾기.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/87389
"""

def solution(n):
    for i in range( 1, n ):
        if( n % i == 1 ):
            return i;



