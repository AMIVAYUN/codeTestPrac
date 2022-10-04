# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:21:37 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n):
    answer = 0
    dp = [ 0 ] * ( n + 2 );
    dp [ 1 ] = 1
    dp [ 2 ] = 2
    for i in range( 3, n + 1 ):
        dp[ i ] = dp[ i - 2 ] + dp[ i - 1 ] 

    return dp[ n ] % 1234567