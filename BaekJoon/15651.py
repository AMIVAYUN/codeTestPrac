# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:34:09 2022
@FileName: 15651.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/15651
"""


N, M = map( int, input().split() );

lst = [ i for i in range( 1, N + 1 ) ];

res = [];

def dfs( depth, str0 ):
    global N, M;
    
    if( depth == M ):
        res.append( str0 );
        return;
    for i in range( N ):
        dfs( depth + 1, str0 + str( lst[ i ] ) + " " );
        
dfs( 0, "" )

for i in res:
    print( i )