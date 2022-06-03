# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:40:41 2022
@FileName: 7569.py
@author: YUNJUSEOK
@Link : https://www.acmicpc.net/problem/7569
"""


dx, dy = [ 0, 0, -1, 1 ], [ 1, -1, 0, 0 ]
M, N =  map( int, input().split() ) ;
farm = [];
for i in range( N ):
    farm.append( list( map( int, input().split() ) ) )
def main():
    global farm, M, N, dx, dy;
    from collections import deque;
    deq = deque([]);
    for i in range( N ):
        for j in range( M ):
            if( farm[ i ][ j ] == 1 ):
                deq.append( [ j, i ] );
    result = 0;
    while deq:
        dt = deq.popleft();
        x , y = dt[ 0 ], dt[ 1 ]
        for i in range( 4 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];

            if( -1 < nx < M and -1 < ny < N and farm[ ny ][ nx ] == 0):
                deq.append( ( nx, ny ) )
                farm[ ny ][ nx ] = farm[ y ][ x ] + 1;
    
    day = 0;

    for i in farm:
        for j in range( M ):
            if( i[j] == 0 ):
                
                return -1;
        day = max( day, max( i ) );
    
    
    return day - 1;

result = main()

print( result )


            
