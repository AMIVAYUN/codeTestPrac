# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:29:58 2022
@FileName: 11055.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11055
"""


n = int( input() );

num = list( map( int, input().split() ) );

dp = [ 0 ] * n;


for i in range( n ):
    dp[ i ] = num[ i ]  
    for j in range( i ):
        if( num[ j ] < num[ i ] ):
            dp[ i ]= max( dp[ i ], dp[ j ] + num[ i ] )
            

print( max( dp ) )
        