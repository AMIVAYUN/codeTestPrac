# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:26:44 2022
@FileName: 1922.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1922
"""

def find( x ):
    global p_Node;
    
    if( p_Node[ x ] != x ):
        p_Node[ x ] = find( p_Node[ x ] );
    
    return p_Node[ x ];

def union( x, y ):
    global p_Node;
    
    root_x = find( x );
    root_y = find( y );
    
    
    if( root_x > root_y ):
        p_Node[ root_x ] = root_y;
    else:
        p_Node[ root_y ] = root_x;
            
            
    

N = int( input() );

M = int( input() );

p_Node = [ i for i in range( N ) ];

vertexes = [];

for i in range( M ):
    a, b, cost = map( int, input().split() );
    a -= 1;
    b -= 1;
    
    if( a == b and N != 1 ):
        continue;
    
    vertexes.append( ( a, b, cost ) );
    
    

s_vertex = list( sorted( vertexes, key = lambda x: x[ 2 ] ) );
if( N == 1 ):
    for vertex in s_vertex:
        a, b, cost = vertex;
        
        if( a == b ):
            print( cost );
            break;
else:
    
    total = 0;
    for vertex in s_vertex:
        a, b, cost = vertex;
        
        if( find( a ) != find( b ) ):
            union( a, b );
            total += cost
    
    print( total )
    
    
    