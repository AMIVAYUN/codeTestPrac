# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:28:04 2022
@FileName: 11052.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11052
"""


N = int( input() );

lst = [ 0 ] + list( map( int, input().split() )  );


dp = [ 0 ] * ( N + 1 );


for i in range( 1, N + 1 ):
    Mx = lst[ i ];
    
    for j in range( 1, i ):
        Mx = max( Mx, dp[ i - j ] + lst[ j ] );
        
    dp[ i ] = Mx;

print( dp[ N ] )