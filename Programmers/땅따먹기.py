# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:46:05 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


#N행 4열
from collections import deque;
#1
'''
def bfs( N, land ):

    csum = max( land[ 0 ] );
    prev = land[ 0 ].index( csum );
    
    for i in range( 1, N ):
        pos, cost = 0, land[ i ][ 0 ];
        for j in range( 1, 4 ):
            if( j == prev ):
                continue;
            if( cost < land[ i ][ j ] ):
                pos, cost = j, land[ i ][ j ];
        
        
        csum += cost;
    
    return csum;
              
'''
#2
'''
def bfs( N, idx, land ):
    dq = deque();
    Mx = 0;
    dq.append( ( 1, idx, land[ 0 ][ idx ] ) );
    
    while dq:

        depth, idx, csum = dq.popleft();
        if( depth == N ):
            Mx = max( csum, Mx );
            continue;
        rowMx = 0;
        for i in range( 4 ):
            if( rowMx < land[ depth ][ i ] and i != idx ):
                rowMx = land[ depth ][ i ]

        rowMxs = [];
        
        for i in range( 4 ):
            if(  i != idx and land[ depth ][ i ] == rowMx ):
                rowMxs.append( i );
        
        for next in rowMxs:
            dq.append( ( depth + 1, next, csum + land[ depth ][ next ] ) )
    
    return Mx;


def solution(land):
    
    N = len( land );
    
    start = land[ 0 ].index( max( land[ 0 ] ) );
    
    answer = bfs( N, start, land );
    
    return answer


'''
def solution( land ):
    N = len( land );
    dp = [ [ 0 ] * 4 for _ in range( N ) ]
    dp[ 0 ] = land[ 0 ]
    
    for x in range( 1, N ):

        for i in range( 4 ):
            dp[ x ][ i ] = max( dp[ x - 1 ][ ( i + 3 ) % 4 ], dp[ x - 1 ][ ( i + 2 ) % 4 ] , dp[ x - 1 ][ ( i + 1 ) % 4 ] ) + land[ x ][ i ]

            
    return max( dp[ N - 1 ] );