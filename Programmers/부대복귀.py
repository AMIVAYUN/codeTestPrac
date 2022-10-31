# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:39:36 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def dijkstra( n, graph, i ):
    import heapq;
    
    heap = [];
    
    heapq.heapify( heap );
    
    heapq.heappush( heap,( i, 0 ) );
    
    Mx = 500000000001;
    dists = [ Mx ] * ( n + 1 );
    
    dists[ i ] = 0;
    print( heap );

    while heap:
    
        pos, cost = heapq.heappop( heap );
        
        if( dists[ pos ] < cost ):
            continue;
        
        for node in graph[ pos ]:
            
            if( dists[ node ] > cost + 1 ):
                dists[ node ] = cost + 1 
                heapq.heappush( heap, ( node, cost + 1 ) );
    

    return dists;
    
def solution(n, roads, sources, destination):
    Mx = 500000000001;
    answer = []
    graph = [ [] for _ in range( n + 1 ) ]
    for road in roads:
        x, y = road;
        graph[ x ].append( y );
        graph[ y ].append( x );
    
    dists = dijkstra( n, graph, destination );

    
    for source in sources:
        
        answer.append( dists[ source ] if( dists[ source ] != Mx ) else -1 );
    
    return answer

solution( 3,	[[1, 2], [2, 3]],	[2, 3],	1  )