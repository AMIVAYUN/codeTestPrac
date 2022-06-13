# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:41:17 2022
@FileName: 1939.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1939

배운 점:
    # 1.dfs/bfs를 사용할거면  방문 검사를 미리하자. 이는 자칫하면 더 많은 루프를 돌게 된다. 이유: a -> b -> c -> d 순이 아닌 a ->b ->d -> c 이런 식으로
     옆자리 부터 가기 때문. 또한 DICT는 무거우니 그래프 문제에서 N이 크면 쓰지 말자.
    # 2.메모리 초과가 바로 뜰 시 BFS 넘어가는 판단은 잊지말자.
    
    # 3. 방문 그래프는 외부에 있어도 된다. 내가 실수한 점은 한 컨텍스트가 목표 정점에 가는 과정에서 다른 길목이 간 길 또한 알아야 하는데, 나는 가고 있는
     컨텍스트 별로 방문 체크를 했으니 경우의 수가 엄청났을 것이다.
    # 4. 찾고자 하는 그래프가 N이 100을 넘을시 기본적으로 N by N을 전부 할당하지 말고 갈 수 있는 간선 갯수 만큼만 할당할 수 있도록 하자.
    # 4. 문제 조건을 잘 읽자 오늘도 답은 나왔을 지언정 min max로 후반부 퍼센트에서 틀렸을 것이다.
    
"""


#1 dfs Memory Exceeded
import sys;
sys.setrecursionlimit( int( 1e5 ) );

def canDeploy( visit, islnum ,w ):
    global legDit,fr,to;
    visit[ islnum ] = 1;
    if( islnum == to ):
        return True;
    
    for i in legDit[ islnum ]:
        if( i[ 1 ] >= w and visit[ i[ 0 ] ] != 1 ):
            if( canDeploy( visit[:], i[ 0 ], w ) ):
                return True;
    return False;
    

N,M = map( int, input().split() );

island = [ i + 1 for i in range( N ) ];
visit = [ 0 ] * ( N + 1 );
legDit= { i : [] for i in island };
min_ = 0;
maxw = 0;
minw = 0;
possiblew = 0;
for i in range( M ):
    start, end, weight = map( int, input().split() );
    maxw = max( weight, maxw );
    #사전 정렬
    legDit[ start ].append( ( end, weight ) );
    legDit[ end ].append( ( start, weight ) );


fr, to = map( int, input().split() );

visit[ fr ] = 1;
'''
for i in legDit[ fr ]:
    if( i[ 1 ] >= 3 and visit[ i[ 0 ] ] != 1 ):
        if( canDeploy( visit, i[ 0 ], 3 ) ):
            min_ = 3;
'''

lt = 0; rt = maxw
while( lt <= rt ):
    midw = ( lt + rt ) // 2 
    result = False;

    for i in legDit[ fr ]:
        if( i[ 1 ] >=  midw and visit[ i[ 0 ] ] != 1 ):
            if( canDeploy( visit[:], i[ 0 ], midw ) ):
                result = True;
                possiblew = midw;
                break;
                         
    
    if( result ):

        lt = midw + 1;
    
    else:

        rt = midw - 1;
    
    
print( possiblew );


#2. dfs by 2D List
import sys;
sys.setrecursionlimit( int( 1e5 ) );

def canDeploy( visit, islnum ,w ):
    global island,fr,to,N;
    visit[ islnum ] = 1;
    if( islnum == to ):
        return True;
    
    for i in range( 1, N + 1 ):
        if( island[ islnum ][ i ] >= w and visit[ i ] != 1 ):
            if( canDeploy( visit[:], i, w ) ):
                return True;
    return False;
    

N,M = map( int, input().split() );

island = [ [0] * ( N + 1 ) for _ in range( N + 1 ) ]
visit = [ 0 ] * ( N + 1 );
min_ = 0;
maxw = 0;
minw = 0;
possiblew = 0;
for i in range( M ):
    start, end, weight = map( int, input().split() );
    maxw = max( weight, maxw );
    #2D array
    island[ start ][ end ] = weight;
    island[ end ][ start ] = weight;


fr, to = map( int, input().split() );

visit[ fr ] = 1;


lt = 0; rt = maxw
while( lt <= rt ):
    midw = ( lt + rt ) // 2 
    result = False;

    for i in range( 1, N + 1 ):
        if( island[ fr ][ i ] >=  midw and visit[ i ] != 1 ):
            if( canDeploy( visit[:], i, midw ) ):
                result = True;
                possiblew = midw;
                break;
                         
    
    if( result ):

        lt = midw + 1;
    
    else:

        rt = midw - 1;
    
    
print( possiblew );


# 3 dfs by 2d List

import sys;
sys.setrecursionlimit( int( 1e3 ) );

def canDeploy( visit, islnum ,w ):
    global legDit,fr,to;
    visit[ islnum ] = 1;
    if( islnum == to ):
        return True;
    
    for i in legDit[ islnum ]:
        if( i[ 1 ] >= w and visit[ i[ 0 ] ] != 1 ):
            if( canDeploy( visit[:], i[ 0 ], w ) ):
                return True;
    return False;
    

N,M = map( int, input().split() );

island = [ i + 1 for i in range( N ) ];
visit = [ 0 ] * ( N + 1 );
legDit= { i : [] for i in island };
min_ = 0;
maxw = 0;
minw = 0;
possiblew = 0;
for i in range( M ):
    start, end, weight = map( int, input().split() );
    maxw = max( weight, maxw );
    #사전 정렬
    legDit[ start ].append( ( end, weight ) );
    legDit[ end ].append( ( start, weight ) );


fr, to = map( int, input().split() );

visit[ fr ] = 1;


lt = 0; rt = maxw
while( lt <= rt ):
    midw = ( lt + rt ) // 2 
    result = False;

    for i in legDit[ fr ]:
        if( i[ 1 ] >=  midw and visit[ i[ 0 ] ] != 1 ):
            if( canDeploy( visit[:], i[ 0 ], midw ) ):
                result = True;
                possiblew = midw;
                break;
                         
    
    if( result ):

        lt = midw + 1;
    
    else:

        rt = midw - 1;
    
    
print( possiblew );


# 3. BFS by dict memory exceeded
def bfs(fr, maxw, to):
    global legDit;
    from collections import deque;
    
    visit = [ 0 ] * ( N + 1 );
    min_ = 0;
    minw = 0;
    possiblew = 0;
    
   
    
    lt = 0 ; rt = maxw;
    while( lt <= rt ):
        midw = ( lt + rt ) //2 
        result = False;
        
        deq = deque();
        deq.append( ( fr, visit[:] ) );
   
        
        while deq:
            
            val =  deq.popleft();
            pos, visited = val[ 0 ], val[ 1 ]
            visited[ pos ] = 1;
            if( pos == to ):
                result = True;
                possiblew = max( possiblew , midw );
                break;
            for i in legDit[ pos ]:
                if( visited[ i[ 0 ] ] != 1 and i[ 1 ] >= midw ):
                    deq.append( ( i[ 0 ], visited[:] ) )
                
        
        if( result ):
            lt = midw + 1;
        else:
            rt = midw - 1;
    
    return possiblew
            
    
N,M = map( int, input().split() );

island = [ i + 1 for i in range( N ) ];
legDit= { i : [] for i in island };
maxw = 0;
for i in range( M ):
    start, end, weight = map( int, input().split() );
    maxw = max( weight, maxw );
    #사전 정렬
    legDit[ start ].append( ( end, weight ) );
    legDit[ end ].append( ( start, weight ) );


fr, to = map( int, input().split() );



result = bfs(fr, maxw, to );

print( result );

# 3 - 1 BFS by 2DList
def bfs(fr, maxw, to):
    global island, N;
    from collections import deque;
    min_ = 0;
    minw = 0;
    possiblew = 0;
    
    lt = 0 ; rt = maxw;
    while( lt <= rt ):
        midw = ( lt + rt ) //2 
        result = False;
        visit = [ 1 for i in range( N + 1 )]
        
        visit[ fr ] = 0;
        deq = deque();
        deq.append( fr );
   
        
        while deq:
            
            pos =  deq.popleft();
            
            if( pos == to ):
                result = True;
                possiblew = max( possiblew , midw );
                break;
            for i in range( 1, N + 1 ):

                if( visit[ i ] and island[ pos ][ i ] >= midw ):
                    visit[ i ] = 0;
                    deq.append( i );
                
        
        if( result ):
            lt = midw + 1;
        else:
            rt = midw - 1;
    
    return possiblew
            
    
N,M = map( int, input().split() );

island = [ [ 0 ] * ( N + 1 ) for i in range( N + 1 )  ];

maxw = 0;
for i in range( M ):
    start, end, weight = map( int, input().split() );
    maxw = max( weight, maxw );
    #2D-array
    island[ start ][ end ] = weight
    island[ end ][ start ] = weight


fr, to = map( int, input().split() );



result = bfs(fr, maxw, to );

print( result );

# 4 BFS BY 2DLIST 변형 + 문제 요건에 맞는 min max;

def bfs(w):
    global island, N, visit, deq;
    result = False;
    while deq:

        pos =  deq.popleft();
            
        if( pos == to ):
            result = True;
            break;
        
        for i in range( len( island[ pos ] ) ):
            j = island[ pos ][ i ];
            if( visit[ j[ 0 ] ] and j[ 1 ] >= w ):
                visit[ j[ 0 ] ] = 0;
                deq.append( j[ 0 ] );
                
        
       
    
    return result
            
from collections import deque;

N,M = map( int, input().split() );
island = [ [] for i in range( N + 1 ) ];


for i in range( M ):
    start, end, weight = map( int, input().split() );
    # By 2D list
    island[ start ].append( ( end, weight ) );
    island[ end ].append( ( start, weight ) );



fr, to = map( int, input().split() );



possiblew = 0;
    
lt = 1 ; rt = 1000000000;
    
while( lt <= rt ):
    midw = ( lt + rt ) //2 
    visit = [ 1 for i in range( N + 1 )]
    visit[ fr ] = 0;
    deq = deque();
    deq.append( fr );
    result = bfs( midw );
    if( result ):
        lt = midw + 1;
        possiblew = midw
    else:
        rt = midw - 1;


print( possiblew );


