# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:32:38 2022
@FileName: 2178.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2178
"""

graph = [];

N, M = map( int, input().split() );

visit = [ [ 1 ] * M for _ in range( N ) ];


from collections import deque;

deq = deque();


for i in range( N ):
    graph.append( input() );
    

deq.append( ( ( 0, 0 ), 1 ) );

visit[ 0 ][ 0 ] = 0;

dx, dy = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ];

Mn = N * M * 2;

while deq:

    pos, cnt = deq.popleft();
    
    x, y = map( int, pos );
    
    if( x == N - 1 and y == M - 1 ):
        Mn = min( Mn, cnt );
        continue;
        
    for i in range( 4 ):
        nx = x + dx[ i ];
        ny = y + dy[ i ];
        if( 0 <= nx < N and 0<= ny < M ):
            if( visit[ nx ][ ny ] and graph[ nx ][ ny ] == '1' ):
                visit[ nx ][ ny ] = 0;
                deq.append( ( ( nx, ny ), cnt + 1 ) );
        

print( Mn );
    
    
