# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 12:45:00 2022
@FileName: 11057.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11057
"""
'''
0 1 2 3 4 5 6 7 8 9 

1 1 1 1 1 1 1 1 1 1 

1 2 3 4 5 6 7 8 9 10

1 2 
'''
dp = [ [ 0 ] * 10 for _ in range( 1001 ) ];

dp[ 1 ] = [ 1 ] * 10;

N = int( input() );



for i in range( 2, N + 1 ):
    for idx in range( 10 ):
        dp[ i ][ idx ] = sum( dp[ i - 1 ][ :idx + 1 ] )

print( sum( dp[ N ] ) )

