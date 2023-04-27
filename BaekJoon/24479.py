# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:16:07 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
    N, R, root = map( int, input().split() );
graph = [ [] for _ in range( N + 1 ) ];
import bisect;
for i in range( R ):

    
    a, b = map( int, input().split() );
    '''
    a, b = -a, -b;
    ax, bx = bisect.bisect_left( graph[ a ], b ), bisect.bisect_left( graph[ b ], a );
    
    graph[ a ] = graph[ a ][ :ax ] + [ b ] + graph[ a ][ ax: ];
    graph[ b ] = graph[ b ][ :bx ] + [ a ] + graph[ b ][ bx: ];
    '''
    graph[ a ].append( b );
    graph[ b ].append( a );
    
#SOL DFS RECURSION TO LOOF
#root = -root;
stack = [ root ];
cnt = 1;
visit = [ 0 ] * ( N + 1 );



while stack:
    now = stack.pop();
    
    if( visit[ now ] ):
        continue;
    
    

    visit[ now ] = cnt;
    cnt += 1;
    graph[ now ].sort( reverse = True );    
    '''
    stack += graph[ now ];
    '''
    
    for next in graph[ now ]:
        if( visit[ next ] == 0 ):
            stack.append( next );
    
    



for i in range( 1, N + 1 ):
    print( visit[ i ] );
'''
SOL8 T,O

N, R, root = map( int, input().split() );
graph = [ [] for _ in range( N + 1 ) ];
import bisect;
for i in range( R ):

    
    a, b = map( int, input().split() );
    a, b = -a, -b;
    ax, bx = bisect.bisect_left( graph[ a ], b ), bisect.bisect_left( graph[ b ], a );
    
    graph[ a ] = graph[ a ][ :ax ] + [ b ] + graph[ a ][ ax: ];
    graph[ b ] = graph[ b ][ :bx ] + [ a ] + graph[ b ][ bx: ];

    
#SOL DFS RECURSION TO LOOF
root = -root;
stack = [ root ];
cnt = 1;
visit = [ 0 ] * ( N + 1 );



while stack:
    now = stack.pop();
    
    if( visit[ now ] ):
        continue;
    
    

    visit[ now ] = cnt;
    cnt += 1;
    
    
    stack += graph[ now ];

    
    


visit = visit[ 1: ];
while visit:
    print( visit.pop() );

'''

'''
#SOL2 WA
graph = [ set() for _ in range( N + 1 ) ]
for i in range( R ):
    a, b = map(int, input().split() );
    
    
    graph[ a ].add( b );
    graph[ b ].add( a );
'''
'''
SOL3 TimeOut
'''
'''
S4 TIMEOUT
graph = [ [] for _ in range( N + 1 ) ];
import bisect;
for i in range( R ):

    
    a, b = map( int, input().split() );
    a, b = -a, -b;
    ax, bx = bisect.bisect_left( graph[ a ], b ), bisect.bisect_left( graph[ b ], a );
    
    graph[ a ] = graph[ a ][ :ax ] + [ b ] + graph[ a ][ ax: ];
    graph[ b ] = graph[ b ][ :bx ] + [ a ] + graph[ b ][ bx: ];

    a, b = map( int, input().split() );
    a, b = -a, -b;
    
    graph[ a ].append( b );
    graph[ b ].append( a );
    
    
for i in range( 1, N + 1 ):
    graph[ i ] = list( sorted( graph[ i ] ) );
cnt = 1;
visit = [ 0 ] * ( N + 1 );
root = -root;
visit[ root ] = 1;
def dfs( graph, visit, now ):
    global answer,cnt;

    while graph[ now ]:
        next = graph[ now ].pop();
        if( visit[ next ] == 0 ):
            cnt += 1
            visit[ next ] = cnt;
            dfs( graph,visit, next );
    
    
    

dfs( graph, visit, root );

visit = visit[ 1: ];
while visit:
    print( visit.pop() );
    
    '''    
    
'''
graph = [ [] for _ in range( N + 1 ) ];
import bisect;
for i in range( R ):
    a, b = map( int, input().split() );
    a, b = -a, -b;
    ax, bx = bisect.bisect_left( graph[ a ], b ), bisect.bisect_left( graph[ b ], a );
    
    graph[ a ] = graph[ a ][ :ax ] + [ b ] + graph[ a ][ ax: ];
    graph[ b ] = graph[ b ][ :bx ] + [ a ] + graph[ b ][ bx: ];

cnt = 1;
visit = [ 0 ] * ( N + 1 );
visit[ root ] = 1;
def dfs( graph, visit, now ):
    global answer,cnt;

    
    for next in graph[ now ]:
        if( visit[ next ] == 0 ):
            cnt += 1;
            visit[ next ] = cnt;
            dfs( graph, visit, next );
    
    
    

dfs( graph, visit, root );


for i in range( 1, N + 1 ):
    print( visit[ i ] );
'''  
    
    
'''
#SOL 1 MemoryOut
import sys
sys.setrecursionlimit( int(1e6))
N, R, root = map( int, input().split() );

graph = [ set() for _ in range( N + 1 ) ]
for i in range( R ):
    a, b = map(int, input().split() );
    
    
    graph[ a ].add( b );
    graph[ b ].add( a );


visit = [ 1 ] * ( N + 1 );
visit[ root ] = 0;
answer = [ 0 ] * ( N + 1 );
def dfs( cnt,graph, visit, now ):
    global answer;
    answer[ now ] = cnt;
    
    for next in graph[ now ]:
        if( visit[ next ] ):
            visit[ next ] = 0;
            dfs( cnt + 1, graph, visit, next );
    
    
    

dfs( 1,graph, visit, root );


for i in range( 1, N + 1 ):
    print( answer[ i ] );



'''