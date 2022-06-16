# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 16:02:10 2022
@FileName: 18352.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/18352
"""


#18352

'''
Sort를 안해서 애먹었따... 그러지말자...
'''

def bfs( V, K ):
    global graph;
    from collections import deque;
    
    
    answer = [];
    deq = deque();
    visit[ V ] = 0; 
    deq.append( ( V, 0 ) ); # ( position, distance )
    while deq:
        pos, dis = deq.popleft();
        if( dis == K ):
            answer.append( pos );
            
        for i in graph[ pos ]:
            if( visit[ i ] ):
                visit[ i ] = 0;
                deq.append( ( i, dis + 1 ) );
                
    
    return answer;

N, M, K, V = map( int, input().split() );

graph = [ [] for i in range( N + 1 ) ];
visit = [ 1 for i in range( N + 1 ) ];


for i in range( M ):
    x, y = map( int, input().split() );
    graph[ x ].append( y );

rs = bfs( V, K );

if( len( rs ) ):
    rs = sorted( rs );
    for i in rs:
        print( i );
else:
    print( -1 );
