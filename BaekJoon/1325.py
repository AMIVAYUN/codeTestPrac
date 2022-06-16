# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 14:06:47 2022
@FileName: 1325.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1325
"""


#1325

N, M = map( int, input().split() );

graph = [ [] for i in range( N + 1 ) ]

Mx = -1;

rs = [];

for i in range( M ):
    x, y = map( int, input().split() );
    graph[ y ].append( ( x ) ); 


def bfs( n ):
    from collections import deque;
    global graph, rs, Mx;
    
    visit = [1] * ( N + 1 ) # 방문 노드
    
    deq = deque();
    cnt = 0;
    deq.append( n );
    visit[ n ] = 0;
    
    while deq:
        
        pos = deq.popleft();
    
        for i in graph[ pos ]:
            if( visit[ i ] ):
                cnt += 1;
                visit[ i ] = 0;
                deq.append( i );
        
    
    if( Mx < cnt ):
        Mx = cnt;
        rs = [ n ];
    
    elif( Mx == cnt ):
        rs.append( n );
    
    
    
    return;
        
                
for i in range( 1, N + 1 ):
    bfs( i )
    
    
print( rs )
    
    