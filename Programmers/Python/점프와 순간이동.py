# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:33:58 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution( n ):
    ans = 0;
    
    while n != 1:
        if( n % 2 ):
            ans += 1;
            n -= 1;
        else:
            n = n // 2;
    return ans + 1;

def solution1(n):

    
    dp = [ 0 ] * ( n + 2 );
    
    dp[ 1 ] = 1;
    dp[ 2 ] = 1;

    for i in range( 3, n + 1 ):
        if( i % 2 ):
            dp[ i ] = dp[ i - 1 ] + 1;
        else:
            
            dp[ i ] = min( dp[ i // 2 ], dp[ i - 1 ] + 1 )
    
    return dp[ n ]