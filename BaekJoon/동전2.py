# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:17:36 2022
@FileName: 2294.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2294
"""
'''
동전 1 알고리즘
'''
#100% out


def f1():
    n, k = map( int, input().split() );

    coin = set()
    for i in range( n ):
        coin.add( int( input() ) );


    dp = [ ( 0, 0 ) ] * ( 100001 );
    num = 0;


    for i in coin:
        
        dp[ i ] = ( dp[ i ][ 0 ] + 1, dp[ i ][ 1 ] + 1 );
        for j in range( i, k + 1 ):
            if( dp[ j ][ 1 ] > 0 and dp[ j - i ][ 1 ] > 0 ):
                val = min( dp[ j ][ 1 ], dp[ j - i ][ 1 ] + 1 )
            elif( dp[ j ][ 1 ] <= 0 and dp[ j - i ][ 1 ] > 0):
                val = dp[ j - i ][ 1 ] + 1;
            elif( dp[ j ][ 1 ] > 0 and dp[ j - i ][ 1 ] <= 0 ):
                val = dp[ j ][ 1 ]
            else:
                val = 0;
            dp[ j ] = ( dp[ j - i ][ 0 ] + dp[ j ][ 0 ], val );
            
        
    print( dp[ k ][ 1 ] if dp[ k ][ 0 ] > 0 else -1 );
    
def f2():
    n, k = map( int, input().split() );
    inf = 100001;
    coin = set()
    for i in range( n ):
        coin.add( int( input() ) );

    coin = sorted( coin );
    dp = [ inf ] * ( inf );


    for i in coin:
        dp[ i ] = 1
        for j in range( i, k + 1 ):
            dp[ j ] = min( dp[ j - i ] + 1 , dp[ j ] );
            
        
    print( dp[ k ] if dp[ k ] != inf else -1 )
def main():
    f2();        





    


if( __name__ == "__main__" ):
    main()