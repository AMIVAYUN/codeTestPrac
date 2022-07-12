# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:51:37 2022
@FileName: 11057.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11057
"""

def sum_( a ):
    return ( a ) * ( a + 1 ) // 2;
n = int( input() );

dp = [ [ 0 ] * ( 10 ) for _ in range( n + 1 ) ];

dp[ 1 ] = [ 1 ] * 10;


for i in range( 2, n + 1 ):
    
    
    for j in range( 10 ):
        sum_ = 0;
        for k in range( j + ( i - 1 ), 10 ):
            sum_ += 
    