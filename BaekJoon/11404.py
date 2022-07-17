# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:05:07 2022
@FileName: 11404.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11404

플로이드 

문제
n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

"""
graph = []
def dijkstra( n, start ):
    global graph;
    import heapq;
    
    Mx = 10000001;
    dists = [ Mx ] * n;
    dists[ start ] = 0;
    lst = [ ( 0, start ) ] 
    
    heapq.heapify( lst );
    
    while lst:
        cost, pos = heapq.heappop( lst );
        if( dists[ pos ] < cost ):
            continue;
        
        for i in range( n ):
            if( graph[ pos ][ i ] ):
                dist = graph[ pos ][ i ] + cost;
                if( dist < dists[ i ] ):
                    dists[ i ] = dist;
                    heapq.heappush( lst, ( dist, i ) );
            
    dists = [ i if i != Mx else 0  for i in dists ];
    return dists;

def f1():
    global graph;
    n = int( input() );
    
    m = int( input() );
    
    graph = [ [ 10000001 ] * ( n ) for _ in range( n ) ]  
    for i in range( n ):
        graph[ i ][ i ] = 0;
    
    
    rs = [];
    
    for i in range( m ):
        a, b, c = map( int, input().split() );
        
        graph[ a - 1 ][ b - 1 ] = min( graph[ a - 1 ][ b - 1 ], c );
    
    
    for i in range( n ):
        rs.append( dijkstra( n, i ) );
    
    for val in rs:
        for j in val:
            print( j , end = " " )
        print();
        
f1()  