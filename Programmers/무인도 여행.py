# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 11:15:04 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


from collections import deque;
from collections import deque;
lenx, leny = 0, 0;
def bfs( x, y, maps, check ):
    global lenx, leny;
    dq = deque();
    dx , dy = [ 0, 0, -1, 1 ], [ 1, -1, 0, 0 ];
    sum_ = int( maps[ x ][ y ] )
    dq.append( ( x, y ) )
    check[ x ][ y ] = 1;
    while dq:
        
        x, y = dq.popleft();

        for i in range( 4 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];
            
            if( 0<= nx < lenx and 0 <= ny < leny ):
                if( check[ nx ][ ny ] == 0 and maps[ nx ][ ny ] != 'X'):
                    check[ nx ][ ny ] = 1;
                    sum_ += int( maps[ nx ][ ny ] )
                    
                    dq.append(  (nx, ny)  )
    return sum_, check;
    
def solution(maps):
    global lenx, leny;
    lenx, leny = len( maps ), len( maps[ 0 ] );

    check = [ [ 0 for y in range( leny ) ] for x in range( lenx ) ];
    answer = [];
    
    for x in range( lenx ):
        
        for y in range( leny ):
            if( check[ x ][ y ] ):
                continue;
            if( maps[ x ][ y ] == 'X' ):
                check[ x ] [ y ] = 1;
                continue;
            
            else:
                sum_, check =  bfs( x, y, maps, check );
                answer.append( sum_ );
          
    
    return list( sorted( answer )  ) if( len( answer ) ) else [-1]