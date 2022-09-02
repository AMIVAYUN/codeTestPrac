# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 14:37:08 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N = int ( input() );

graph = [];


ans = 0;
for i in range( N ):
    row = list( map( int, input().split() ) );
    graph.append( row );


dx , dy = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ];




def bfs( k, pos ):
    global dx, dy, visit, graph;
    from collections import deque;
    
    deq = deque();
    
    deq.append( ( pos ) )
    
    visit[ pos[ 0 ] ][ pos [ 1 ] ] = 0;
    
    while deq:
        x, y = deq.popleft();
        
        
        for i in range( 4 ):
            
            nx = x + dx[ i ];
            
            ny = y + dy[ i ];
            
            if( 0<= nx < N and 0<= ny < N ):
                if( visit[ nx ][ ny ] and graph[ nx ][ ny ] > k ):
                    visit[ nx ][ ny ] = 0; 
                    deq.append( ( nx, ny ) );
    
    return ;

for k in range( 0, N + 1 ):
    temp = 0;
    visit = [ [ 1 ] * N for _ in range( N ) ];
    for x in range( N ):
        for y in range( N ):

            if( graph[ x ][ y ] > k and visit[ x ][ y ] ):
                bfs( k, ( x, y ) );
                temp += 1;
    ans = max( temp, ans );

print( ans );