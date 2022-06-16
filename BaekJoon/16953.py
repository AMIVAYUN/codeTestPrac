# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 14:04:55 2022
@FileName: 16953.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/16953
"""


# 16953

a, b = map( int, input().split() )

def bfs( a, b ):
    from collections import deque;
    result = [];
    deq = deque();
    deq.append( ( a, 1 ) );
    while deq:
        value, cnt = map( int, deq.popleft() );
        if( value == b ):
            result.append( cnt );
        
        if( value < b ):
            deq.append( ( value * 2, cnt + 1 ) );
            deq.append( ( int ( str( value ) +"1" ),cnt + 1 ) );
        
    return result

rs = bfs( a, b )

if( len( rs ) ):
    print( min( rs ) );
else:
    print( -1 )
