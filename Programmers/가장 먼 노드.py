# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:46:15 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n, edge):
    answer = 0;
    graph = [ [] for _ in range ( n + 1 ) ];
    for vertex in edge:
        x, y = vertex;
        
        graph[ x ].append( y );
        graph[ y ].append( x );
    
    from collections import deque;
    visit = [ 1 ] * ( n + 1 )
    
    
    dq = deque();
    visit [ 1 ] = 0;
    dq.append( ( 1 , 0 ) );
    Mx = ( 0, [] );
    while dq:

        pos, cnt = dq.popleft();
        
        if( cnt > Mx[ 0 ] ):
            Mx = ( cnt, [ pos ] );
        
        elif( cnt == Mx[ 0 ] ):
            tmp = Mx[ 1 ];
            tmp.append( pos );
            Mx = ( Mx[ 0 ], tmp );
        
        
        for dest in graph[ pos ]:
            if( visit[ dest ] ):
                dq.append( ( dest, cnt + 1 ) );
                visit[ dest ] = 0;

    return len( Mx[ 1 ] );