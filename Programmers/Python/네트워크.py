# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:11:02 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


parent = [];
def union( x, y ):
    global parent;
    root_x = find( x );
    root_y = find( y );
    
    if( root_x > root_y ):
        parent[ root_x ] = root_y;
    else:
        parent[ root_y ] = root_x;
def find( x ):
    global parent;
    if( parent[ x ] != x ):
        parent[ x ] = find( parent[ x ] );
    
    return parent[ x ];
def solution(n, computers):
    global parent;
    
    
    answer = 0
    parent = [ i for i in range( n ) ]
    
    
    for x in range( n ):
        for y in range( n ):
            if( x== y ):
                continue
            
            if( computers[ x ][ y ] ):
                union( x, y );
    from collections import defaultdict;
    
    ddit = defaultdict( int );
    for i in range( n ):
        rs = find( i );
        ddit[ rs ] += 1;
    
    
        
    return len( ddit );