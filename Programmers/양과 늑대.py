# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 00:17:56 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(info, edges):
    from collections import deque;
    answer = 0;
    
    graph = [[] for _ in range( len( info ) ) ];
    
    for edge in edges:
        graph[ edge[ 0 ] ].append( edge[ 1 ] );
    
    dq = deque();
    remain = [];
    dq.append( ( 0, 1, 0,remain ) );
    
    
    
    while dq:
        pos,sheep,wolf,remain = dq.popleft();
        
        answer = max( sheep, answer );
        
        
        for next in graph[ pos ]:
            remain.append( next );
            
        
        for var in remain:
            tmp = remain[:]
            if( info[ var ] ):
                if( sheep > wolf + 1 ):
                    
                    tmp.remove( var );
                    
                    dq.append( ( var, sheep, wolf + 1, tmp ) );
            else:
                tmp.remove( var );
                dq.append( ( var, sheep + 1, wolf, tmp ) );
                
    
    return answer