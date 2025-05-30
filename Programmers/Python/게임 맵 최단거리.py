# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 18:32:06 2022
@FileName: 게임 맵 최단거리.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/1844
"""


def solution(maps):
    from collections import deque;
    dx, dy = [ 1, -1, 0, 0 ], [ 0, 0, -1, 1 ];
    rs = [];
    leny = len( maps );
    lenx = len( maps[ 0 ] );
    visit = [ [ 0 ] * lenx for _ in range( leny ) ];
    
    deq = deque();
    
    deq.append(  ( 0, 0, 1) );
    
    while deq:
        x, y, cnt = deq.popleft();
        
        if( x == lenx -1 and y == leny - 1 ):
            rs.append( cnt );
            continue;
        
        for i in range( 4 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];
            
            if( 0<= nx < lenx and 0<= ny < leny ):
                if( not( visit[ ny ][ nx ] ) and maps[ ny ][ nx ] ):
                    visit[ ny ][ nx ] = 1;
                    deq.append( ( nx, ny, cnt + 1 ) );
                    
                    
            
    
    
    
    answer = max( rs ) if len( rs ) else -1 ;
    return answer