# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 16:15:48 2022
@FileName: 1647.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1647
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

#Timeout
def t1():
    parent = [ i for i in range( N ) ]        
    vertexes = [];
    
    costsum_ = 0;
    
    for i in range( M ):
        A,B,cost = map( int, input().split() );
        A-= 1; B -= 1;
        vertexes.append( ( A, B, cost ) );
        costsum_ += cost 
        
        
    vertexes = list( sorted( vertexes, key = lambda x: x[ 2 ] ) )
    
    total = 0;
    
    for vertex in vertexes:
        
        a, b, cost = vertex;
        
        if( a != b ):
            if( find( a ) != find( b ) ):
                union( a, b );
                total += cost;
    
        cnt = len( set( parent ) );
        
        if( cnt == 2 ):
            break;
    
    print( total )
    
N, M = map( int, input().split() )

def t2():
    

    parent = [ i for i in range( N ) ]        
    vertexes = [];
    
    costsum_ = 0;
    
    for i in range( M ):
        A,B,cost = map( int, input().split() );
        A-= 1; B -= 1;
        vertexes.append( ( A, B, cost ) );
        costsum_ += cost 
        
        
    vertexes = list( sorted( vertexes, key = lambda x: x[ 2 ] ) )
    
    total = 0;
    
    import heapq;
    
    heap = [];
    
    heapq.heapify( heap );
    
    for vertex in vertexes:
        
        a, b, cost = vertex;
        
        if( a != b ):
            if( find( a ) != find( b ) ):
                union( a, b );
                total += cost;
                
                heapq.heappush(heap, -1 * cost )
    
        
    
    print( total + heapq.heappop( heap ) )
    
