# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 22:01:07 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def turn( board, leng ,x, y, cnt ):
    dxy = [ ( 0, 0 ), ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ) ];
    
    for i in range( 5 ):
        nx , ny = x + dxy[ i ][ 0 ], y + dxy[ i ][ 1 ];
        
        if( 0 <= nx < leng and 0 <= ny < leng ):
            board[ nx ][ ny ] = ( board[ nx ][ ny ] + cnt ) % 4;
    
    return board;

def getCase( case, board ):

    origin = [ row[: ] for row in board[ :2 ] ]; 
    
    sum_ = sum( case );
    
    leng = len( case );

    for idx, c in enumerate( case ):
        board = turn( board, leng, 0, idx, c );

    
    
    for x in range( 1, leng ):
        for y in range( leng ):
            
            turncnt = ( 4 - board[ x - 1 ][ y ] ) % 4;
            
            turn( board, leng, x, y, turncnt );
            sum_ += turncnt;
   
      
    flag = sum( [ sum( row ) for row in board ] );
    

    return sum_ if flag == 0 else 4 ** 8 + 1; 

def solution( clockHands ):
    import itertools;
    cases = list( itertools.product( [ 0, 1, 2, 3 ], repeat = len( clockHands ) ) );

    answer = 4**64 + 1;
    for case in cases:
        tmp = [ row[ : ] for row in clockHands[ : ] ];
        
        result = getCase( case , tmp );
        
        answer = min( answer, result );
    
    return answer;
'''
#sol2 wa
def turn( board, leng ,x, y, cnt ):
    dxy = [ ( 0, 0 ), ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ) ];
    
    for i in range( 5 ):
        nx , ny = x + dxy[ i ][ 0 ], y + dxy[ i ][ 1 ];
        
        if( 0 <= nx < leng and 0 <= ny < leng ):
            board[ nx ][ ny ] = ( board[ nx ][ ny ] + cnt ) % 4;
    
    return board;

def getCase( case, board ):
    origin = board[ 0 ][:]
    
    sum_ = sum( case );
    
    leng = len( case );

    for idx, c in enumerate( case ):
        board = turn( board, leng, 0, idx, c );

    
    
    
    for x in range( 1, leng ):
        for y in range( leng ):
            
            if( x > 2 and sum( board[ x - 2 ] ) != 0 ):
                return 4 ** 8 + 1;
            
            if( board[ x ][ y ] != 0 and board[ x - 1 ][ y ] != 0 ):
                turncnt = 4 - board[ x ][ y ];
                turn( board, leng, x, y, turncnt );
                sum_ += turncnt;            
        
            
    
    
    return sum_; 

def solution( clockHands ):
    import itertools;
    cases = list( itertools.product( [ 0, 1, 2, 3 ], repeat = 4 ) );
    answer = 4**64 + 1;
    for case in cases:
        tmp = [ row[ : ] for row in clockHands[ : ] ];
        
        result = getCase( case , tmp );
        
        answer = min( answer, result );
    
    
    return answer;


'''

        
'''
#answer = float( "inf" );
import sys;
sys.setrecursionlimit( int( 1e6 ) );
def getNext( direction ):
    return ( direction + 1 ) % 4;

def isValid( graph ):
    leng = len( graph );
    sum_ = 0;
    for i in range( leng ):
        sum_ += sum( graph[ i ] );
    
    return sum_ == 0;


def dfs( cnt, graph ):
    dx, dy = [ -1, 1, 0, 0 ],[ 0, 0, -1, 1 ];
    global answer;
    if( cnt > answer ):
        return;
    
    if( isValid( graph ) ):
        answer = min( cnt, answer );
        return;
    
    leng = len( graph );
    
    for x in range( leng ):
        for y in range( leng ):
            
            if( graph[ x ][ y ] ):
                now = [ graph[ i ][ : ] for i in range( leng ) ];
                
                now[ x ][ y ] = getNext( now[ x ][ y ] );
                
                for i in range( 4 ):
                    nx, ny = x + dx[ i ], y + dy[ i ];
                    
                    if( 0<= nx < leng and 0<= ny < leng ):
                        now[ nx ][ ny ] = getNext( now[ nx ][ ny ] );
                        
                dfs( cnt + 1, now );
    
    return;
    

def getNextpos( graph ):
    leng = len( graph );
    Mx = ( 0, [ 0, 0 ] );
    dx, dy = [ -1, 1, 0, 0 ],[ 0, 0, -1, 1 ];
    for x in range( leng ):
        for y in range( leng ):
            if( graph[ x ][ y ] ):
                sum_ = 0;
                for i in range( 4 ):
                    nx = x + dx[ i ];
                    ny = y + dy[ i ];
                    
                    if( 0<= nx < leng and 0<= ny < leng ):
                        sum_ += graph[ nx ][ ny ];
            
                if( Mx[ 0 ] < sum_ ):
                    Mx = ( sum_, [ x, y ] );
    
    return Mx;



#SOL1 완탐 T.O
def solution(clockHands):
    answer = 0;
    
    dx, dy = [ -1, 1, 0, 0 ],[ 0, 0, -1, 1 ];

    leng = len( clockHands );
    while not( isValid( clockHands ) ):
        next = getNextpos( clockHands );
        x, y = next[ 1 ];
        clockHands[ x ][ y ] = getNext( clockHands[ x ][ y ] );
        for i in range( 4 ):
            nx = next[ 1 ][ 0 ] + dx[ i ];
            ny = next[ 1 ][ 1 ] + dy[ i ];
                    
            if( 0<= nx < leng and 0<= ny < leng ):
                clockHands[ nx ][ ny ] = getNext( clockHands[ nx ][ ny ] );
        
        answer += 1;
    
    
    return answer
'''