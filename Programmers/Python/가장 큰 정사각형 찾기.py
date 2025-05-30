# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:37:18 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

'''#WA 10 & Timeout
def checkMx( Mx,board, m, n, x, y ):
    mx = min( m, n )
    lst = [ i for i in range( 1, mx - x + 1 ) ]
    Mx = 0;
    for side in lst:
        if( side < Mx ):
            continue;
        flag = False;
        for i in range( x, x + side ):
            for j in range( y, y + side ):
               
                if( 0<= i < m and 0<= j < n ):
                    
                    if( board[ i ][ j ] == 0 ):
                        flag = True;
                        break;
                else:
                    flag = True;
                    break;
            if( flag ):
                
                break;
        
        if( flag ):
            continue;
            
        Mx = max( side , Mx );
    
    return Mx;
def solution(board):
    answer = 1234;
    m = len( board );
    n = len( board[ 0 ] );

    Mx = 0;
    for x in range( m ):
        for y in range( n ):
            if( board[ x ][ y ] ):
                Mx = max( Mx, checkMx( Mx,board,m,n, x, y ) );

    return Mx ** 2;

'''


def solution(board):
    
    m, n = len( board ), len( board[ 0 ] );
    dp = [ [ 0 ] * n for _ in range( m ) ];
    for i in range( m ):
        dp[ i ][ 0 ] = board[ i ][ 0 ]
    dp[ 0 ] = board[ 0 ][:]
    Mx = 0;
    for x in range( 1, m ):
        for y in range( 1, n ):
            if( dp[ x - 1 ][ y - 1 ] and dp[ x - 1 ][ y ] and dp[ x ][ y - 1 ] and board[ x ][ y ]):
                dp[ x ][ y ] = dp[ x - 1 ][ y - 1 ] + 1;
                Mx = max( Mx, dp[ x ][ y ] );
            else:
                dp[ x ][ y ] = board[ x ][ y ];

    return Mx ** 2;


solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])