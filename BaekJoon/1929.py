# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:48:15 2022
@FileName: 1929.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1929
"""


def chkPrime( n ):
    if( n == 1 ):
        return False;
    for i in range( 2, int( n**0.5 + 1 ) ):
        if( n % i == 0 ):
            return False;
    
    return True;

N, M = map( int, input().split() );


for i in range( N , M + 1 ):
    if( chkPrime( i ) ):
        print( i )


3 