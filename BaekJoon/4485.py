# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 11:40:45 2022
@FileName: 4485.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/4485
"""

dx = [ 1, -1, 0, 0 ];
dy = [ 0, 0, 1, -1 ];
def dijkstra( graph, N ):
    global dx, dy, count;
    import heapq;
    inf = 9 * ( N**2 ) + 1; 
    costs = [ [inf] * N  for _ in range( N ) ]

    lst = [ ( 0, 0 , graph[ 0 ][ 0 ] ) ]
    costs[ 0 ][ 0 ] = graph[ 0 ][ 0 ];
    heapq.heapify( lst );
    
    while lst:
        x, y, cost = heapq.heappop( lst );
        if( costs[ x ][ y ] < cost ):
            continue;
        for i in range( 4 ):
            nx = x + dx[ i ]
            ny = y + dy[ i ];
            if( 0<= nx < N and 0<= ny < N ):
                tcost = cost + graph[ nx ][ ny ];
                if( tcost < costs[ nx ][ ny ] ):
                    heapq.heappush( lst, ( nx, ny, tcost ) )
                    costs[ nx ][ ny ] = tcost; 
                
        
    str0 = "Problem "+ str( count )+": " +str( costs[ N -1 ][ N - 1 ] );
    print( str0 )
    count += 1;
N = int( input() );
count = 1;
while N:
    
    graph = [ [] for i in range( N ) ];
    for i in range( N ):
        graph[ i ] = list( map( int, input().split()) )
        
        
    dijkstra( graph, N );    
        
    
    N = int( input() );
