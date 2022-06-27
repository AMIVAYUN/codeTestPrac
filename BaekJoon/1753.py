# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 17:10:10 2022
@FileName: 1753.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1753
"""


#문제를 잘못 이해
def f1():
    to, weight = 0 , 1
    from collections import deque;
    
    
    Mx = 0 ;
    
    V, E = map( int, input().split() );
    
    start = int( input() );
    
    
    graph = [ [] for i in range( V + 1 ) ];
    
    
    for i in range( E ):
        
        a,b,c = map( int, input().split() );
        
        graph[ a ].append( ( b, c ))
        
    deq = deque();
    
    visit = [ 0 ] * ( V + 1 );
    visit[ 0 ] = 1;
    visit[ start ] = 1;
    deq.append( ( start, 0 , visit ) );
    
    while deq:
        
        pos, val, visit = deq.popleft();
        
        if( sum( visit ) == V + 1 ):
            
            Mx = max( Mx, val );
            continue;
        
        for i in graph[ pos ]:
            if( not( visit[ i[ to ] ] ) ):
                visit[ i[ to ] ] = 1;
                deq.append( ( i[ to ], val + i[ weight ] , visit) );
        
        
    
    print ( Mx );
        
        


#by Dijkstra
def f2():
    import heapq;
    
    V, E = map( int, input().split() );
    
    INF = ( V - 1 ) * 10 + 1
    
    start = int( input() );
    
    graph = [ [] for i in range( V + 1 ) ];
    
    result = [ INF ] * ( V + 1 )
    
    result[ start ] = 0;
    
    for i in range( E ):
        
        a,b,c = map( int, input().split() );
        
        graph[ a ].append( ( b, c ))
        
    
    proc = [ ( 0, start ) ];
    
    heapq.heapify( proc );
    
    while proc:
        cost, pos = heapq.heappop( proc );
        
        if( result[ pos ] < cost ):
            continue;
        
        for i in graph[ pos ]:
            tcost = i[ 1 ] + cost;
            
            if( result[ i [ 0 ] ] > tcost ):
                heapq.heappush( proc, ( tcost, i[ 0 ] ) );
                result[ i[ 0 ] ] = tcost;
        
        
    for i in result[1:]:
        if( i == INF ):
            print( "INF" );
        else:
            print( i );


def main():
    f2();
    






if( __name__ == "__main__" ):
    main();