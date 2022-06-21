# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:24:33 2022
@FileName: 1024.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1024
"""

def Nsum( n ):
    return ( ( n ) * ( n + 1 ) ) // 2;


def Sn( n, a ):
    return ( n * ( 2 * a + ( n - 1 ) )  // 2 );


def getA( N, l ):
    a = ( (2 * N) - l**2 + l ) / ( 2*l )
    return a if( a>= 0 ) else 0.1 ;

def f1():
    N, L = map( int, input().split() );

    for i in range( L, N//L + 1 ):
        diff = Nsum( i - 1 )
        for j in range( 1, N//2 ):
            if( ( j * i + diff == N ) ):
                
                lst = [ j + _ for _ in range( i ) ];
                
                if( i <= 100 ):
                    for k in range( len( lst ) ):
                        print( lst[ k ] , end = " " );
                    return
                
                else:
                    continue;

    print( -1 );
    return
#f1();


def f2():
    N, L = map( int, input().split() );
    
    for i in range( L, 101 ):
        a = getA( N, i );
        
        if( a.is_integer() ):
            a = int( a )
            if( i <= 100 ):
                lst = [ a + _ for _ in range( i ) ]
                for k in lst:
                    print( k, end = " " );
                return
    print( -1 );
    return
#f2()

def f3():
    N, L = map( int, input().split() );

    for i in range( L, 101 ):
        