# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 14:52:29 2022
@FileName: 배달.py
@author: YUNJUSEOK
@Link:https://school.programmers.co.kr/learn/courses/30/lessons/12978
"""


def dijkstra( N, graph ):
    Mx = 500001;
    dists = [ Mx ] * N;
    import heapq;
    hq = [ ( 0, 0 ) ]
    dists[ 0 ] = 0;
    
    heapq.heapify( hq );
    
    while hq:
        pos, dist = heapq.heappop( hq );

        if( dists[ pos ] < dist ):
            continue;
        for i in range( N ):
            if( graph[ pos ][ i ] ):
                cost = graph[ pos ][ i ] + dist;
                if( cost < dists[ i ] ):
                    heapq.heappush( hq, ( i, cost ) );
                    dists[ i ] = cost;
            
    
    return dists;
n            
    
    
    
    
    
    
    
def solution(N, road, K):
    

    graph = [ [ 0 ] * N for _ in range( N ) ];
    
    for i in road:
        a, b, c = i;
        a -= 1;
        b -= 1;
        if( graph[ a ][ b ] ):
            graph[ a ][ b ] = min( graph[ a ][ b ], c );
            graph[ b ][ a ] = min( graph[ b ][ a ], c );
        else:
            graph[ a ][ b ] = c
            graph[ b ][ a ] = c
            

    
    answer = dijkstra( N, graph )
    return len( [ i for i in answer if i <=K] )