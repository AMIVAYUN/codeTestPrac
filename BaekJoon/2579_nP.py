# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:22:17 2022
@FileName: 2579.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2579
"""
#1
val, cnt = 0 , 1
def f1():
    N = int( input() );
    lst = [ 0 ] * ( N + 1 ) 
    for i in range( N ):
        lst[ i ] = int( input() );

    dp = [ ( lst[ 0 ] , 0) for _ in range( N + 1 ) ]
    dp[ 1 ] = ( lst [ 0 ] + lst[ 1 ] , 1 );
    for i in range( 2, N + 1 ):
        if( dp[ i - 1 ][ cnt ] == 1 ):
            dp[ i ] = ( dp[ i - 2 ][ val ] + lst[ i ], 0 );
        
        else:
            dp[ i ] = max( ( dp[ i - 1 ][ val ] + lst[ i ], dp[ i - 1 ][ cnt ] + 1 ) , ( dp[ i - 2 ][ val ] + lst[ i ], 0 ) )
        
    print( dp[ N ][ val ] )

def f2():
    
    val, cnt = 0 , 1
    '''
    5
    8
    3
    5
    8
    1
    14
    
    ans: 20
    Returns
    -------
    None.

    '''
    N = int( input() );
    lst = [ 0 ] * ( N + 2 ) 
    for i in range( 1, N + 1 ):
        lst[ i ] = int( input() );

    dp = [ ( 0, 0) for _ in range( N + 1 ) ]
    dp[ 1 ] = ( lst [ 1 ]  , 1 );
    for i in range( 2, N + 1 ):
        if( i == N - 1 ):
            if( dp[ i - 1 ][ cnt ] == 1 ):
                dp[ i ] = ( dp[ i - 2 ][ val ] +lst[ i ], 1 );
                continue
        if( dp[ i - 1 ][ cnt ] == 2 ):
            dp[ i ] = ( dp[ i - 2 ][ val ] + lst[ i ], 1 );
        
        else:
            dp[ i ] = max( ( dp[ i - 1 ][ val ] + lst[ i ], dp[ i - 1 ][ cnt ] + 1 ) , ( dp[ i - 2 ][ val ] + lst[ i ], 1 ) )
    print( dp )
    print( dp[ N ][ val ] )
    
f2()