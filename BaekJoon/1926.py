# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 10:36:17 2022
@FileName: 1926.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1926
    
    시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	19331	8089	5703	40.762%
문제
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와,
 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이
 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

입력
첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 
가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다.
 (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 
  0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

출력
첫째 줄에는 그림의 개수, 둘째 줄에는 
그 중 가장 넓은 그림의 넓이를 출력하여라.
 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
"""
from collections import deque

X,Y = map( int, input().split() );

dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, -1, 1 ]
graph = [];

Mx = 0;


for i in range( X ):
    row = list( map( int, input().split() ) );
    
    
    graph.append( row );

def bfs( a, b ):
    global graph,X,Y;
    q = deque();
    cost = 1;
    q.append( ( a, b ) );
    
    while q:
        
        x,y = q.popleft()
        for i in range( 4 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];
            if( 0<= nx < X and 0<= ny < Y ):
                if( graph[ nx ][ ny ] ):
                    graph[ nx ][ ny ] = 0;
                    cost += 1
                    q.append( ( nx, ny ) );
                    
    return cost;

num = 0;

for x in range( X ):
    for y in range( Y ):
        if( graph[ x ][ y ] ):
            graph[ x ][ y ] = 0;
            num +=1
            val = bfs( x, y );
            Mx = max( val , Mx );
print( num )
print( Mx )
        
    