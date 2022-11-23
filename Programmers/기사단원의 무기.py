# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 10:00:54 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(number, limit, power):
    answer = 0;
    dp = [ 0 ] * ( number + 1 );
        
    for i in range( 1, number + 1 ):
        
        for j in range( i, number + 1, i ):
            dp[ j ] += 1;
        
        if( dp[ i ] > limit ):
            dp[ i ] = power
    
    return sum( dp );