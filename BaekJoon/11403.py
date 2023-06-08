# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:49:52 2023

@author: 주석
"""

n = int( input( ) );
graph = [ [] for _ in range( n ) ];
for i in range( n ):
    lst = list( map( int, input().split() ) );
    
    for j in range( n ):
        if( lst[ j ] == 1 ):
            graph[ i ].append( j );

answer = [];

def bfs( n, graph, i ):
    from collections import deque;
    
    visit = [ 0 ] * n;
    
    dq = deque();
    
    for next in graph[ i ]:
        visit[ next ] = 1;
        dq.append( next );
    
    
    while dq:
        
        next = dq.popleft();
        
        
        for n in graph[ next ]:
            if( visit[ n ] == 0 ):
                visit[ n ] = 1 ;
                dq.append( n );
        
        
        
    return visit;


for i in range( n ):
    answer.append( bfs( n,graph, i ) );
        
    
    
for row in answer:
    for c in row:
        print( c, end = " " );
    
    print()
