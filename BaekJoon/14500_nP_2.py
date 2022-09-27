# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:01:02 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

import itertools;
n, m = map( int, input().split() );
Mx = 0
graph = [];

for i in range( n ):
    graph.append( list( map( int, input().split() ) ) )

dx = [ -1, 1, 0, 0 ];

dy = [ 0, 0, -1, 1 ];

lst = [ i for i in range( 4 ) ];
perm = itertools.combinations_with_replacement( lst, 3 );
Poliomino = list( perm )
sett = set();

for case in Poliomino:
    
    a = list( itertools.permutations( list( case ), 3 ) )
    sett = sett | set( a )


Mx = 0;
def bfs( case, pos ):
    global graph,n,m, Mx;
    from collections import deque;
    
    
    x, y = pos;
    sum_ = graph[ x ][ y ];
    
    for number in case:
        nx = x + dx[ number ];
        ny = y + dy[ number ];
        
        if( 0<= nx < n and 0<= ny < m ):
            sum_ += graph[ nx ][ ny ]
            x = nx; y = ny;
        
        else:
            break;
            return;
    
    Mx = max( sum_, Mx );
    
for i in range( n ):
    for j in range( m ):
        for case in sett:
            bfs( case, ( i, j ) )



print( Mx )

