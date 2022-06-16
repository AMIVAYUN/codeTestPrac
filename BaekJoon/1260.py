# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:26:26 2022
@FileName: 1260.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1260
"""


#dfs & bfs 1260

def dfs( V ):
    global graph,visit1,dfslst;
    
    for i in graph[ V ]:
        if( visit1[ i ] ):
            visit1[ i ] = 0
            dfslst.append( i );
            dfs( i );
        
def bfs( V ):
    global graph,visit2,bfslst;
    from collections import deque;
    deq = deque();
    bfslst.append( V );
    visit2[ V ] = 0;
    deq.append( V );
    
    while deq:
        pos = deq.popleft();
        
        for i in graph[ pos ]:
            if( visit2[ i ] ):
                visit2[ i ] = 0;
                bfslst.append( i );
                deq.append( i );
                
        

N, M, V = map( int, input().split() );

graph =[ [] for i in range( N + 1 ) ]

visit1 ,visit2 = [ 1 for i in range( N + 1 ) ],[ 1 for i in range( N + 1 ) ]
dfslst = []; bfslst = [];

for i in range( M ):
    x, y = map( int, input().split());
    graph[ x ].append( y );
    graph[ y ].append( x );
    

for i in range( len( graph ) ):
    graph[ i ] = sorted( graph[ i ] ); 

dfslst.append( V );
visit1[ V ] = 0;
dfs( V )
bfs( V )

for i in dfslst:
    print( i, end = " " );
print();
for i in bfslst:
    print( i, end = " ")