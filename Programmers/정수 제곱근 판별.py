# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:06:29 2022
@FileName: 정수 제곱근 판별.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12934
"""


def solution(n):
    if n == 1 :
        return 4;
    for i in range( 1, n//2 ):
        if i**2 == n :
            return ( i + 1 ) ** 2;
        
    return -1;