# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:50:40 2023
@FileName: 1504.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1504
"""


'''

1번에서 N번 정점으로 가려함. 최단거리로

    조건
    
    1. 왔던길 다시가기 가능
    
    2. 임의로 주어진 두 정점은 반드시 통과해야함.
    

'''

N, E = map( int, input().split() );

graph =[ [] for _ in range( N + 1 ) ];


for i in range( E ):
    x, y, weight = map(int, input().split() )
    
    graph[ x ].append( ( y, weight ) )
    graph[ y ].append( ( x, weight ) )

obj1, obj2 = map( int, input().split() );


    

def dijkstra( n, graph, start ):
    import heapq;
    
    dists = [ float('inf') ] * ( n + 1 );
    dists[ start ] = 0;
    heap = [ ( 0, start ) ];
    
    heapq.heapify( heap );
    
    while heap:
        
        w, pos = heapq.heappop( heap );
        
        if( dists[ pos ] < w ):
            continue;
        
        for next, w1 in graph[ pos ]:
            if( dists[ next ] >= w + w1 ):
                heapq.heappush(heap, ( w + w1 , next ) );
                dists[ next ] = w + w1;
    
    return dists;
dists_1 = dijkstra( N, graph, 1 );

if( N <= 3 ):
    print( dists_1[ N ] if dists_1[ N ] != float('inf') else -1 );

else:
    
    dists_obj1 = dijkstra( N, graph, obj1 );
    dists_obj2 = dijkstra( N, graph, obj2 );
    dists_N = dijkstra( N, graph, N );
    result =  min( [dists_1[ obj1 ] + dists_obj1[ obj2 ] + dists_obj2[ N ],dists_1[ obj2 ] + dists_obj2[ obj1 ] + dists_obj1[ N ], dists_1[ N ] + dists_N[ obj2 ] + dists_obj2[ obj1 ] +dists_obj1[ N ],dists_1[ N ] + dists_N[ obj1 ] + dists_obj1[ obj2 ] + dists_obj2[ N ]] )
    print( result if result != float( 'inf' ) else -1 ) 
    
    
    
    

    