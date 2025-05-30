# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 12:59:45 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
def calc0( n, start, graph, idx ):
    for i in range( start, n - start + 2 ):
        graph[ i ].append( idx );
        idx += 1;
    
    return idx, graph;

def calc1( n, start, graph, idx ):
    for i in range( n - start - 1 ):
        
        graph[ n - start + 1 ].append( idx );

        idx += 1;
    
    return idx, graph;

def calc2( n, start,graph, idx ):
    for i in range( n - start + 1, start , -1 ):
        graph[ i ].append( idx );
        idx += 1;
    
    return idx, graph;

def solution(n):
    answer = []
    
    idx = 1;
    start = 1;
    graph = [ [] for i in range( n + 1 ) ];
    
    while start <= n // 2:
        idx, graph = calc0( n, start,graph, idx );
        print( graph );
        idx, graph = calc1( n, start,graph, idx );
        print( graph );
        idx, graph = calc2( n, start,graph, idx );
        print( graph );
        start += 2;
    
    
    return answer
'''



idx = 1;

def solution(n):
    lst = [];
    graph = [[0] * j for j in range( 1, n + 1 ) ]
    idx = 1;
    x, y = -1, 0;
    
    for i in range( n ):
        for j in range( i, n ):
            if( i % 3 == 0 ):
                x += 1;
            elif( i % 3 == 1 ):
                y += 1;
            else:
                x -= 1;
                y -= 1;
            graph[ x ][ y ] = idx;
            idx += 1;
        
    answer = sum( graph, [] );
    return answer