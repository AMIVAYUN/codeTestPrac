# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 18:04:40 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
import itertools;
from collections import deque;

dx, dy = [ 0, 0, -1, 1 ], [ -1, 1, 0, 0 ];

N, M = map( int, input().split() );

viruses = [];

graph = [];

blanks = [];

for i in range( N ):
    row = list( map( int, input().split() ) )
    for idx in range( M ):
        if( row[ idx ] == 2 ):
            viruses.append( ( i, idx ) );
        elif( row[ idx ] == 0 ):
            blanks.append( ( i, idx ) );
    graph.append( row );





cmb = list( itertools.combinations( blanks, 3 ) );
Mx = 0;

    
def bfs( graph, viruses ):
    global N, M,dx,dy;
    visit = [ [ 1 ] * M for _ in range( N ) ];
    deq = deque( viruses );
    
    for pos in viruses:
        visit[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
    
    while deq:
        x, y = deq.popleft();
        
        for i in range( 4 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];
            
            if( 0 <= nx < N and 0 <= ny < M ):
                if( visit[ nx ][ ny ] and graph[ nx ][ ny ] == 0 ):
                    graph[ nx ][ ny ] = 2;
                    deq.append( ( nx, ny ) );
                    visit[ nx ][ ny ] = 1;
    
    
    cnt = 0;
    for x in range( N ):
        for y in range( M ):
            if( graph[ x ][ y ] == 0 ):
                cnt += 1;
    
    return cnt;


for case in cmb:
    tmp = [ row[ : ] for row in graph[ : ] ];
    
    for pos in case:
        tmp[ pos[ 0 ] ][ pos[ 1 ] ] = 1;
    
    Mx = max( bfs( tmp, viruses ), Mx );

print( Mx )
    
    
