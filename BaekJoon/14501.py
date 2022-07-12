# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:57:47 2022
@FileName: 14501.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/14501
"""


#n = int( input() );
def s1():
    lst = [ [ 0 ] * ( n + 1 ) for i in range( n + 1 ) ];

    proc = [ ( 0, 0 ) ];

    for i in range( n ):
        proc.append( tuple( map( int, input().split() ) ) );


    for j in range( 1, n + 1 ):
        
        for k in range( j, n + 1, proc[ j ][ 0 ] ):
            if( k + proc[ j ][ 0 ] > n ):
                continue;
            lst[ j ][ k ] = max( lst[ j - 1 ][ k ], lst[ j ][ k - 1 ] + proc[ j ][ 1 ] );
        
        
            

    print( max( lst[ n ] ) )


def s2():
    n = int( input() );
    dp = [ 0 ] * ( n + 2 ) 
    
    proc = [ ( 0, 0 ) ];
    for i in range( n ):
        proc.append( tuple( map( int, input().split() ) ) );
        
    for i in range( 1, n + 1 ):
        
        for j in range( i + proc[ i ][ 0 ], n + 2 ):

            dp[ j ] = max( dp[ j ], dp [ i ] + proc[ i ][ 1 ] );
    

    print( dp[ n + 1 ] )


def s3():
    n = int( input() );
    dp = [ 0 ] * ( n + 2 );
    proc = [ ( 0, 0 ) ];
    
    for i in range( n ):
        proc.append( tuple( map( int, input().split() ) ) );
        
        
        