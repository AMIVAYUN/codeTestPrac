# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 11:35:22 2022
@FileName: 5582.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/5582
"""

def f1():
    a = input();

    b = input();


    dp = [ [ 0 ] * ( len( b ) + 1 ) for _ in range( len( a ) + 1 ) ];

    for i in range( 1, len( a ) + 1 ):
        for j in range( 1, len( b ) + 1 ):
            if( a[ i - 1 ] != b[ j - 1 ] ):
                dp[ i ][ j ] = max( dp[ i - 1 ][ j ], dp[ i ][ j - 1 ] );
            
            else:
                dp[ i ][ j ] = dp [ i - 1 ][ j - 1 ] + 1;

    print( dp )
    #for i in range( 1, len( b ) + 1 ):
    idx = 0;
    Mx = 0;
    dp [ len( a ) ] = dp[ len( a ) ] + [ dp[ -1 ][ -1 ] ]
    while idx < len( b ) + 1 :
        if( dp[ len( a ) ][ idx ] + 1 == dp[ len( a ) ][ idx + 1 ] ):
            start = idx;
            while( idx < len( b ) + 1 and dp[ len( a ) ][ idx ] + 1 == dp[ len( a ) ][ idx + 1 ] ):
                idx += 1;
            Mx = max( Mx, idx - start );
        idx += 1;
    
    print( Mx )
# memory out
def f2():
    import itertools
    
    
    a = input();
    
    b = input();
    
    lena = len( a );
    
    lst = [ i for i in range( 1, lena + 1 ) ];
    
    cmb = list( itertools.combinations( lst, 2 ) );
    
    cmb = [ ( i[ 0 ], i[ 1 ], i[ 1 ] - i[ 0 ] ) for i in cmb ];
    
    cmb = sorted( cmb, key = lambda x: x[ 2 ],reverse = True );
    
    print( cmb );
    for i in cmb:
        if( a[ i[ 0 ]: i[ 1 ] ] in b ):
            print( i[ 2 ]  );
            break;
            
    
def f3():
    a = input();

    b = input();

    ans = 0 ;
    dp = [ [ 0 ] * ( len( b ) + 1 ) for _ in range( len( a ) + 1 ) ];

    for i in range( 1, len( a ) + 1 ):
        for j in range( 1, len( b ) + 1 ):
            if( a[ i - 1 ] == b[ j - 1 ] ):
                dp[ i ][ j ] = dp[ i - 1 ][ j - 1 ] + 1 ;
                ans = max( ans, dp[ i ][ j ] );   


    print( ans )
    
    
f3()