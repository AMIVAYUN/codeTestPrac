# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:11:37 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def find( x ):
    global p_Nodelst;
    
    if( p_Nodelst[ x ] != x ):
        p_Nodelst[ x ] = find( p_Nodelst[ x ] );
    
    return p_Nodelst[ x ];


def union( x, y ):
    global p_Nodelst;
    root_x = find( x );
    root_y = find( y );
    if( root_x != root_y ):
        if( root_x > root_y ):
            p_Nodelst[ root_x ] = root_y;
        else:
            p_Nodelst[ root_y ] = root_x;
        

N = int( input() );

p_Nodelst = [ i for i in range( N ) ];

M = int( input() );

for i in range( N ):
    lst = list( map( int, input().split() ) );
    for idx in range( N ):
        if( lst[ idx ] ):
            union( i, idx ) ;


params = list( map( int, input().split() ) );

start = find( params[ 0 ] - 1 );
ans = "YES"
for parameter in params[1:]:
    if( find( parameter - 1 ) != start ):
        ans = "NO";
        break;

print( ans );
    
            
    
    