# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 13:01:57 2022
@FileName: 10282.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/10282


다익스트라 알고리즘을 익히기 위해 푼 문제로서 해당 방법은 최소 힙을 활용하여 다익스트라 알고리즘을 최적화한 형태이다.

기본적으로 매 노드마다 최신화 하는 방법은 같지만 최소힙을 통해 그전에 가장 가까운 거리부터 찾아간다는 개념이 다르다.

일반 다익스트라는 매 회 가장 가까운 노드를 찾아서 그 곳부터 방문하기 때문이다.

"""


def dijkstra( c ):
    global graph;
    import heapq
    
    inf = int( 1e8 );
    lenx = len( graph );
    seconds = [ inf ] * lenx; seconds[ c ] = 0;
    
    lst = []
    heapq.heapify( lst );
    
    heapq.heappush( lst, ( c, seconds[ c ] ) );
    
    while lst:
        pos, sec = heapq.heappop( lst );
        
        if( seconds[ pos ] < sec ):
            continue;
        
        for i in graph[ pos ]:
            cost = i[ 1 ] + sec;
            
            if( cost < seconds[ i[ 0 ] ] ):
                seconds[ i[ 0 ] ] = cost;
                heapq.heappush( lst, ( i[ 0 ], cost ) )
    
    
    cnt = 0;
    timer = 0;
    seconds[ 0 ] = 0
    for i in range( 1, len( seconds ) ):
        if( seconds[ i ] != inf ):
            cnt +=1;
            
        if( seconds[ i ] == inf):
            seconds[ i ] = 0
            
    print( cnt,max( seconds ) );
    
    
    
T = int( input() );






for i in range( T ):
    N, M, C = map( int, input().split() );
    graph =[ [] for i in range( N + 1 ) ];
    for i in range( M ):
        a, b, s = map( int, input().split() );
        graph[ b ].append( ( a, s ) );
    dijkstra( C );   