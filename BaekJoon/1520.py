# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:52:59 2022
@FileName: 1520.py
@author: YUNJUSEOK
@Link : https://www.acmicpc.net/problem/1520

DFS + DP의 방식을 지키도록 노력하자

"""

import sys;
sys.setrecursionlimit( int( 1e5 ) )
cnt = 0;
dx = [ 0, 0, -1, 1 ];
dy = [ 1, -1, 0, 0 ];
lst = [];
M, N = map( int, input().split() );

table = [[-1] * N for i in range( M ) ]

for i in range( M ):
        lst.append( list( map( int, input().split() ) ) )
def dfs( x, y ):
    global dx, dy,M, N,table ;
    if( x == N - 1 and y == M - 1 ):
        return 1;
    if( table[ y ][ x ] != -1 ):
        return table[ y ][ x ];
    
    table[ y ][ x ] = 0;
    for i in range( 4 ):
        nx = x + dx[i];
        ny = y + dy[i];
        
        if( -1 < nx < N  and -1< ny < M and ( lst[ny][nx] < lst[y][x] ) ):
            table[ y ][ x ] += dfs( nx, ny );
    
    return table[ y ][ x ];

print( dfs( 0, 0 ) );

    


    
    

    

