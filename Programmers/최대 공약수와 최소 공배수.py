# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:18:26 2022
@FileName: 최대 공약수와 최소 공배수 .py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12940
"""


def solution(n, m):
    answer = gcd( n, m );
    return [ answer ,(n * m) // answer]

def gcd( a, b ):
    if( a == b ):
        return a;
    if( a > b ):
        return gcd( a - b, b );
    if( a < b ):
        return gcd( b , a );