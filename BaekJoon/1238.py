# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 14:06:38 2022
@FileName: 1238.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1238


http://www.secmem.org/blog/2019/01/09/wrong-dijkstra/


"""



N, M, X = map( int, input().split() );

graph = [ [] for _ in range( N + 1 ) ]

for i in range( M ):
    a, b, t = map( int, input().split() );
    graph[ a ].append( ( b, t ) );

inf = 1e10;

def dijkstra( x ):
    global graph, N ;
    import heapq;
    seconds = [ inf ] * ( N + 1 );
    
    seconds[ x ] = 0;
    
    
    lst = [];
    heapq.heapify( lst );
    heapq.heappush( lst, ( x, seconds[ x ] ) );
    
    while lst:
       
        pos, sec = heapq.heappop( lst );
        
        if( seconds[ pos ] < sec ):
            continue;
        
        for idx,s in graph[ pos ]:
            tcost = sec + s;
            if( tcost < seconds[ idx ] ):
                seconds[ idx ] = tcost;
                heapq.heappush( lst,( idx, tcost ) );
    
    
    
    
    
    return seconds;
from1 = dijkstra( X );
go1 = [ 0 ];
result = 0
for i in range( 1, N + 1 ):
    rs = dijkstra( i )[ X ]
    result = max( rs + from1[ i ], result )



print( result );
    

