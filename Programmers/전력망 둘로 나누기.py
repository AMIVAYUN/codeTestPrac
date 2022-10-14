# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:46:32 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


parent = [];
def find( x ):
    global parent;
    
    if( parent[ x ] != x ):
        return find( parent[ x ] );
    
    else:
        return x;

    
def union( x, y ):
    global parent;
    root_x = find( x );
    root_y = find( y );
    
    if( root_x > root_y ):
        parent[ root_x ] = root_y;
        
    else:
        parent[ root_y ] = root_x;
    
    return;

    
    
def solution(n, wires):
    global parent;
    answer = n;
    
    leng = len( wires );
    import itertools;

    cmb = list( itertools.combinations( wires, leng - 1 ) );
    from collections import defaultdict;
    for case in cmb:
        parent = [ i for i in range( n + 1 ) ];
        
        for a, b in case:
            union( a, b );
            
        dit = defaultdict( int );
        
        for i in range( 1, n + 1 ):
            root_i = find( i );
            dit[ root_i ] += 1;

        answer = min( answer, max( dit.values() ) - min( dit.values() ) );
    
    return answer;



# TC 1, 10, 11, 12 OUT;
'''
parent = [];
def find( x ):
    val, childs = parent[ x ];
    if( val != x ):
        parent[ x ] = find( val );
    return parent[ x ];

def union( x, y ):
    global parent;
    root_x, x_childs = find( x );
    root_y, y_childs = find( y );
    
    if( x > y ):
        parent[ root_x ] = [ root_y, x_childs ];
        parent[ root_y ] = [ root_y, y_childs + x_childs ];
    else:
        parent[ root_y ] = [ root_x, y_childs ];
        parent[ root_x ] = [ root_x, y_childs + x_childs ];
        
    return;
def solution(n, wires):
    from collections import defaultdict;
    global parent;
    answer = -1;
    leng = len( wires );
    import itertools;
    Mx = n;
    cmb = list( itertools.combinations( wires, leng - 1 ) );
    
    for case in cmb:
        parent = [ [ i,1 ] for i in range( n + 1 ) ];
        dit = defaultdict( int );
        for vertex in case:
            union( vertex[ 0 ], vertex[ 1 ] );
        
        for res in parent:
            val, childs = res;
            dit[ val ] = max( dit[ val ], childs );
        
        lst = list( sorted( dit.items(), key = lambda x: -x[ 1 ] ) );
        Mx = min( lst[ 0 ][ 1 ] - lst[ 1 ][ 1 ] , Mx );
    return Mx
'''