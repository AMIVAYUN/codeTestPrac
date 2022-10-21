# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:50:42 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


parent = [];
def find( x ):
    global parent;
    
    if( parent[ x ] != x ):
        parent[ x ] = find( parent[ x ] );
    
    return parent[ x ];

def union( x, y ):
    global parent;
    root_x,root_y = find( x ), find( y );
    
    if( root_x > root_y ):
        parent[ root_x ] = root_y;
    
    else:
        parent[ root_y ] = root_x;
    
    return;

def solution(n, costs):
    global parent;
    answer = 0;
    
    parent = [ i for i in range( n ) ];
    
    costs = list( sorted( costs , key = lambda x: x[ 2 ] ) )
    
    for cost in costs:
        x, y, cost = cost;
        
        root_x, root_y = find( x ), find( y );
        
        if( root_x != root_y ):
            union( x, y );
            answer += cost;
        
    return answer