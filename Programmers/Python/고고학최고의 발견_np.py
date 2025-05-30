# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:24:09 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


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
'''

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
    
'''
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

def solution(clockHands):
    answer = 0;
    
    dx, dy = [ -1, 1, 0, 0 ],[ 0, 0, -1, 1 ];
    '''
    퍼즐은 시계들이 행렬을 이루는 구조물 // 시곗바늘 하나가 시계방향으로만 돈다.
    90도씩 돌릴 수 있다. 
    하나를 돌리면 인접한 상하좌우 시곗바늘도 함께돌아감.
    
    길이 2*2 ~ 8*8;
    
    '''
    leng = len( clockHands );
    while getNextpos( clockHands ) != [ 0, ( 0, 0 ) ]:
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