# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:27:44 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def bfs( start, objective ):
    from collections import deque;
    global visit, graph;
    
    deq = deque();
    
    deq.append( ( start, 0 ) );
    
    visit[ start ] = 0;
    
    
    while deq:
        pos, chon = deq.popleft();
        
        if( pos == objective ):
            print( chon );
            return;
        
        for family in graph[ pos ]:
            if( visit[ family ] ):
                deq.append( ( family, chon + 1 ) );
                visit[ family ] = 0;
    
    print( -1 );
    return;
    
N = int ( input() );
graph = [ [] for _ in range( N + 1 )];

x , y = map( int, input().split() );

m = int( input() );

visit = [ 1 ] * 101;

for i in range( m ):
    a, b = map( int, input().split() );
    
    graph[ a ].append( b );
    
    graph[ b ].append( a );
    

bfs( x, y );
