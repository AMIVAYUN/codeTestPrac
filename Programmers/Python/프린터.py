# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:02:13 2022
@FileName: 프린터.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/42587
"""
from collections import deque

def solution(priorities, location):
    import heapq;
    
    sub = [ ( -i , i ) for i in priorities ]
    priorities = [ ( priorities[ i ], i ) for i in range( len( priorities ) ) ]
    heapq.heapify( sub );
    cnt = 0;
    print( sub )
    while sub:
        val = heapq.heappop( sub );
        val = val[ 1 ]
        for i in range( 0, len( priorities ) ):
            if( priorities[ i ][ 0 ] == val ):
                cnt += 1;
                if( priorities[ i ][ 1 ] == location ):
                    return cnt;
                priorities = priorities[ i: ] + priorities[ :i ];
                
                priorities.pop( 0 );
                break;
        
    return 0

from collections import deque

def solution(priorities, location):
    answer = 0;
    idx, pri = 0, 1;
    q = [ ( i, p ) for i,p in enumerate( priorities ) ]
    while q:
        pos = q.pop( 0 );
        if( any( pos[ pri ] < some[ pri ] for some in q ) ):
            q.append( pos );
        else:
            answer += 1;
            if( pos[ idx ] == location ):
                return answer;
            
    return;