# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:12:12 2023

@author: 주석
"""

cnt = 1;
Mn = 2147483647;
#visit = [];
#end = [];
dxys = [ [ 1, -1 ], [ 1, 0 ], [ 1, 1 ], [ 0, 1 ] ];


def isRight( n, x, y ):
    return 0<= x < n and 0<= y < 3


while True:
    n = int( input() );

    if( n == 0 ):
        break;

    Mn = 2147483647;


    dp = [ [ 0 ] * 3 for _ in range( n ) ];

    graph = [];


    for i in range( n ):
        
        row = list( map( int, input().split() ) );

        graph.append( row );


    dp[ 1 ][ 0 ] = graph[ 0 ][ 1 ] + graph[ 1 ][ 0 ];
    dp[ 1 ][ 1 ] = graph[ 1 ][ 1 ] + min(dp[ 1 ][ 0 ], graph[ 0 ][ 1 ], graph[ 0 ][ 2 ]+graph[ 0 ][ 1 ] );    
    dp[ 1 ][ 2 ] = graph[ 1 ][ 2 ] + min(dp[ 1 ][ 1 ], graph[ 0 ][ 1 ], graph[ 0 ][ 2 ] + graph[ 0 ][ 1 ] );
    
    for x in range( 2, n ):

        for y in range( 3 ):
            val1 = dp[ x ][ y - 1 ] if isRight( n, x, y - 1 ) else Mn;
            val2 = dp[ x - 1 ][ y ] if isRight( n, x - 1, y ) else Mn;
            val3 = dp[x - 1][ y - 1 ] if isRight(n, x - 1, y - 1) else Mn;
            val4 = dp[ x - 1 ][ y + 1 ] if isRight( n, x - 1, y + 1 ) else Mn;
            dp[ x ][ y ] = min( val1, val2, val3, val4 ) + graph[ x ][ y ];
            # val4, val5, val6 
    '''
    
    ----------------
    
    '''
    

    print( str( cnt ) + '.', dp[ n - 1 ][ 1 ] )
    cnt += 1;