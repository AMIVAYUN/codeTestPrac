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
    
#f2()

#92퍼 아웃
def f3():
    
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
    lst = [ 0 ] * ( 301 ) 
    for i in range( N ):
        lst[ i ] = int( input() );

    result = [ 0 ] * ( 301 ) ;
    result[ 0 ] = 0;
    
    result[ 1 ] = lst[ 1 ]; result [ 2 ] = max( lst[ 2 ] + lst[ 1 ], lst[ 2 ] ); result[ 3 ] = max( lst[ 2 ] + lst[ 3 ], lst [ 1 ] + lst[ 3 ] )
    
    for i in range( 4, N + 1 ):
        result[ i ] = max( result[ i - 2 ] + lst[ i ], result[ i - 3 ] + lst[ i - 1 ] + lst[ i ] )

    print( result[ N ] )
    
#f3()


def f4():
    N = int( input( ) );
    lst = [ 0 ] * ( 301 );
    for i in range( N ):
        lst[ i ] = int( input() );
        
    result = [ 0 ] * 301;
    result[ 0 ] = lst[ 0 ]; result[ 1 ] = max( lst[ 1 ] + lst[ 0 ], lst[ 1 ] ); result[ 2 ] = max( lst[ 1 ] + lst[ 2 ], lst[ 0 ] + lst[ 2 ] );
    
    for i in range( 3, N ):
        result[ i ] = max( result[ i - 2 ] + lst[ i ], result[ i - 3 ] + lst[ i - 1 ]+ lst[ i ] )
        
    print( result[ N - 1 ] )
f4();