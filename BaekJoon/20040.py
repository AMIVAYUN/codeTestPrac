# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:38:45 2022
@FileName: 20040.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/20040
"""

def find( x ):
    global p_Node;
    
    if( p_Node[ x ] != x ):
        p_Node[ x ] = find( p_Node[ x ] );
        
    return p_Node[ x ];


def union( x, y ):
    root_x,root_y = find( x ), find( y );
    
    
    if( root_x > root_y ):
        p_Node[ root_x ] = root_y;
        
    elif( root_x < root_y):
        p_Node[ root_y ] = root_x;
    
    else:
        return True;
    
    return False;
p_Node = [];

def main_0():
    global p_Node;
    N, M = map( int, input().split() );
    
    TheHighestNode = N;
    p_Node = [ i for i in range( N ) ]
    for i in range( M ):
        a, b = map( int, input().split() );""
        fa, fb = find( a ), find( b )
        if( ( a == TheHighestNode and fb == TheHighestNode ) or ( b == TheHighestNode and TheHighestNode == fa ) ):
            print( i + 1 )
            return;
        TheHighestNode = min( [TheHighestNode,a,b,fa,fb] )
        if( fa != fb ):
            union( a, b );
    
    
    print( 0 );
        

def main_1():
    global p_Node;
    N, M = map( int, input().split() );
    
    p_Node = [ i for i in range( N ) ]
    for i in range( M ):
        a, b = map( int, input().split() );""
        fa, fb = find( a ), find( b )

        flag = union( a, b );
        
        if( flag ):
            print( i + 1 )
            return
    
    print( 0 );
        





if( __name__ == "__main__" ):
    main_1()