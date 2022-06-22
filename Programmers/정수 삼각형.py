# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:37:34 2022
@FileName: 정수 삼각형.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/43105
"""


def solution(lst):
    N = len( lst );
    if( N == 1 ):
        return lst[ 0 ][ 0 ];
    

    dp = [ [ 0 ] * len( lst[ i ] ) for i in range( len( lst ) ) ]
    
    dp[ 0 ][ 0 ] = lst[ 0 ][ 0 ];

    
    
    for i in range( N ):
        for j in range( len( lst[ i ] ) ):
            if( j == 0 ):
                dp[ i ][ j ] = dp[ i - 1 ][ j ] + lst[ i ][ j ]
                
            elif( j == i ):
                dp[ i ][ -1 ] = dp[ i - 1 ][ -1 ] + lst[ i ][ -1 ];
            else:
                dp[ i ][ j ] = max( dp[ i - 1 ][ j - 1 ], dp[ i - 1 ][ j ] ) + lst[ i ][ j ];
            
    
    return ( max( dp[ N - 1 ] ) );


