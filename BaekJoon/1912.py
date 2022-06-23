# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:39:17 2022
@FileName: 1912.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1912
"""

N = int( input() );


S = list( map( int, input().split() ) )
dp = [ 0 ] * N ;
dp[ 0 ] = S[ 0 ]
for i in range( 1, N ):
    dp[ i ] = max( dp[ i - 1 ] + S[ i ], S[ i ] )

print( max( dp ) );