# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 12:02:54 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def dfs( node, conn, visited ):
    
    visited[ node ] = True;
    
    children =[ next_node for next_node in conn[ node ] if not visited[ next_node ] ];
    print( node, visited , children )
    pick, not_pick = 1, 0;
    
    if not children:
        return( pick, not_pick );


    else:
        for child in children:
            child_pick, child_not_pick = dfs( child, conn, visited );
            
            pick += min( child_pick, child_not_pick );
            not_pick += child_pick
        return ( pick, not_pick );
    
    
    
def solution( n, lighthouse ):
    
    graph =  [ [] for _ in range( n + 1 ) ];
    
    for x, y in lighthouse:
        graph[ x ].append( y );
        graph[ y ].append( x );
        
    
    visited = [ False for _ in range( n + 1 ) ];
    
    root = 1;
    result = dfs( root, graph, visited );
    
    return result;


solution( 8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]] )