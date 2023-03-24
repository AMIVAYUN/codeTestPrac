# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 12:37:17 2023
@FileName: 13905.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/13905
"""


V , E = map( int, input().split() );

start, end = map( int, input().split() );

graph = [ [] for _ in range( V + 1 ) ];

for i in range( E ):
    a,b,w = map( int, input().split() );
    graph[ a ].append( ( b, w ) );
    graph[ b ].append( ( a, w ) );
    

def dijkstra( n, graph, start, end ):
    import heapq;
    dists = [ 0 for _ in range( n + 1 ) ];
    dists[ start ] = float('inf');
    
    heap = [ ( -float('inf'), start ) ];
    
    heapq.heapify( heap );
    
    while heap:

        dist, pos = heapq.heappop( heap );
        dist *= -1;
        if( dists[ pos ] > dist ):
            continue;
        for next, w in graph[ pos ]:
            cost = min( w, dist );
            if( cost > dists[ next ] ):
                dists[ next ] = cost;
                heapq.heappush( heap, ( -cost, next ) ) ;

    return dists[ end ];

print( dijkstra( V, graph, start, end ) );
        
    
    


#SOL1 6% WA UnionFind
'''
V , E = map( int, input().split() );

start, end = map( int, input().split() );

parent = [ i for i in range( V + 1 ) ];

def find( x ):
    if( parent[ x ] != x ):
        parent[ x ] = find( parent[ x ] );
    
    return parent[ x ];

def union( x, y ):
    root_x, root_y = find( x ), find( y );
    

        
    if( root_x > root_y ):
        parent[ root_x ] = root_y;
        
    else:
        parent[ root_y ] = root_x;
            
    return


vertexes = [];

for i in range( E ):
    a,b,w = map( int, input().split() );
    
    vertexes.append( ( w, a, b ) );
from collections import deque;
vertexes = deque( sorted( vertexes, key = lambda x: ( -x[ 0 ] ) ) );

Mx = 1000001;

while vertexes and parent[ start ] != parent[ end ]:
    
    w, a, b = vertexes.popleft();
    
    if( a!= b and find( a ) != find( b ) ):
        union( a, b );
        Mx = min( Mx, w );
    

print( Mx if Mx != 1000001 else 0 )
    
    

        
'''

