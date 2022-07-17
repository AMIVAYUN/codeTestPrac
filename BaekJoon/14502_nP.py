# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:02:00 2022
@FileName: 14502.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/14502
"""

from collections import deque;
dx, dy = [ 1, -1, 0, 0 ], [ 0, 0, 1, -1 ]
def infect( temp ):
    deq = deque();
    global dx, dy, n, m, stack;
    visit = [ [ 1 ] * m for _ in range( n ) ]
    for i in range( n ):
        for j in range( m ):
            if( visit[ i ][ j ] and temp[ i ][ j ] == 2 ):
                visit[ i ][ j ] = 0;
                deq.append( ( i, j ) );
                while deq:
                    x, y = deq.popleft();
                    
                    for a in range( 4 ):
                        nx = x + dx[ a ];
                        ny = y + dy[ a ];
                        
                        if( 0<= nx < n and 0<= ny < m ):
                            if( visit[ nx ][ ny ] and ( temp[ nx ][ ny ] == 0 or temp[ nx ][ ny ] == 2 ) ):
                                temp[ nx ][ ny ] = 2;
                                visit[ nx ][ ny ] = 0;
                                deq.append( ( nx, ny ) );
    sum_ = 0;
    
    for i in range( n ):
        sum_ += temp[ i ].count( 0 );
    
    stack.append( sum_ );
    
    return;


n, m = map( int, input().split() );

graph = [];
stack = [];
for i in range( n ):
    graph.append( list( map( int, input().split() ) ) );



lst = [ ( i, j ) for i in range( n ) for j in range( m ) ];

import itertools;

cmb = list( itertools.combinations( lst, 3 ) );

Mx = 0;
import copy;
for i in cmb:
    temp = copy.deepcopy( graph )
    for j in i:
        x, y = j[ 0 ], j[ 1 ]
        temp[ x ][ y ] = 1;

    infect( temp );

print( max( stack ) )    
    
