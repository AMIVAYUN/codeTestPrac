# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:08:46 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n):

    dp = [ 0 ] * 100001;
    
    dp[ 1 ] = 1;
    
    for i in range( 2, n + 1 ):
        dp[ i ] = dp[ i - 1 ] + dp[ i - 2 ];
    
    
    return dp[ i ] % 1234567