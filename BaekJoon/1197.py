# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:09:36 2022
@FileName: 1197.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1197
"""

def find( x ):
    global parent;
    
    if( parent[ x ] != x ):
        parent[ x ] = find( parent[ x ] );
        
    return parent[ x ];


def union( a, b ):
    root_a = find( a );
    root_b = find( b );
    if( root_a > root_b ):
        parent[ root_a ] = root_b;
        
    else:
        parent[ root_b ] = root_a;

        
vertexes = [];




V, E = map( int, input().split() );

parent = [ i for i in range( V )];


for i in range( E ):
    A,B,cost = map( int, input().split() );
    A-= 1; B -= 1;
    vertexes.append( ( A, B, cost ) );
    
    
vertexes = list( sorted( vertexes, key = lambda x: x[ 2 ] ) )

total = 0;

for vertex in vertexes:
    
    a, b, cost = vertex;
    
    if( a != b ):
        if( find( a ) != find( b ) ):
            union( a, b );
            total += cost;

print( total )