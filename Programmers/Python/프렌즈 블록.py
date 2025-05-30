# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:03:21 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(m, n, board):
    answer = 0;
    from collections import defaultdict;
    for x in range( m ):
        board[ x ] = list( board[ x ] );
    standard = m * n;
    while True:
        ddit = defaultdict( set );
        visit = [ [ 1 ] * n for _ in range( m ) ];

        for x in range( m ):
            for y in range( n ):
                if( board[ x ][ y ] == '0' ):
                    continue;
                if( x + 1 < m and y + 1 < n ):

                    if( board[ x ][ y ] == board[ x + 1 ][ y ] == board[ x ][ y + 1 ] == board[ x + 1 ][ y + 1 ] and visit[ x ][ y ] ):
                        visit[ x ][ y ] = 0;
                        ddit[ board[ x ][ y ] ].add( ( x,y ) )
                        ddit[ board[ x ][ y ] ].add( ( x + 1,y ) )
                        ddit[ board[ x ][ y ] ].add( ( x,y + 1 ) )
                        ddit[ board[ x ][ y ] ].add( ( x + 1 ,y + 1 ) )
        sum_ = 0;

        for i in range( m ):
            sum_ += sum( visit[ i ] );

        if( sum_ == standard ):
            break;
        for key in ddit:
            answer += len( ddit[ key ] );
            for x, y in ddit[ key ]:
                board[ x ][ y ] = "0";
        for y in range( n ):
            for x in range( m - 1, 0, -1 ):
                if( board[ x ][ y ] == "0" ):
                    idx = x;
                    while idx > 0 and board[ idx ][ y ] == "0":
                        idx -= 1;
                    board[ idx ][ y ], board[ x ][ y ] = board[ x ][ y ], board[ idx ][ y ];





            
    return answer