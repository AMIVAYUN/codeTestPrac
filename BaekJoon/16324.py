# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:53:28 2023

@author: 주석
"""

N, L, R = map( int, input().split() );


graph = [];

for i in range( N ):
    graph.append( list( map( int, input().split() ) ) );



dx = [ 0, 0, 1, -1 ];
    
dy = [ 1, -1, 0, 0 ];
from collections import deque;

def Go( graph, N, L, R):
    global dx, dy;
    
    marker = 0;
    
    visit = [ [ 0 ] * N for _ in range( N ) ];
    
    
    
    for x in range( N ):
        for y in range( N ):
            dq = deque();
            sum_ = 0;
            cnt = 0;
            if( visit[ x ][ y ] ):
                continue;
            
            if( ( x + 1 < N and L<= abs(graph[ x + 1 ][ y ] - graph[ x ][ y ] ) <=R ) or ( y + 1 < N and  L <= abs( graph[ x ][ y + 1 ] - graph[ x ][ y ] ) <=R ) ):
                dq.append( ( x, y ) );
                marker += 1;
                visit[ x ][ y ] = marker;
                sum_ += graph[ x ][ y ];
                
                

                while dq:

                    a, b = dq.popleft();
                    cnt += 1;
                    
                    for i in range( 4 ):
                        na = a + dx[ i ];
                        nb = b + dy[ i ];
                        
                        if( 0 <= na < N and 0 <= nb < N and L <= abs( graph[ na ][ nb ] - graph[ a ][ b ] ) <= R and visit[ na ][ nb ] < 1):
                            visit[ na ][ nb ] = marker;
                            sum_ += graph[ na ][ nb ];
                            dq.append( ( na, nb ) );

            if( cnt != 0 and marker != 0):
                for sx in range( N ):
                    for sy in range( N ):
                        if( visit[ sx ][ sy ] == marker ):
                            graph[ sx ][ sy ] = sum_ // cnt;
    
    
    
    return ( graph, sum( [ sum( row[:] )for row in visit[:] ] ) ); 

cnt = 0;

subcnt = 0;
while True:
    graph, tot = Go( graph, N, L, R );

    if( tot == 0 ):
        break;
    subcnt += 1;
        

print( subcnt );
                        
                
                
                        