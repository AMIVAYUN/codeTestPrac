# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:11:48 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

'''
유현이가 새 집으로 이사했다. 새 집의 크기는 N×N의 격자판으로 나타낼 수 있고, 
1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 (r, c)로 나타낼 수 있다. 
여기서 r은 행의 번호, c는 열의 번호이고, 행과 열의 번호는 1부터 시작한다. 
각각의 칸은 빈 칸이거나 벽이다.

오늘은 집 수리를 위해서 파이프 하나를 옮기려고 한다. 파이프는 아래와 같은 형태이고, 
2개의 연속된 칸을 차지하는 크기이다.



파이프는 회전시킬 수 있으며, 아래와 같이 3가지 방향이 가능하다.



파이프는 매우 무겁기 때문에, 유현이는 파이프를 밀어서 이동시키려고 한다. 
벽에는 새로운 벽지를 발랐기 때문에, 파이프가 벽을 긁으면 안 된다. 즉, 파이프는 항상 빈 칸만 차지해야 한다.

파이프를 밀 수 있는 방향은 총 3가지가 있으며, →, ↘, ↓ 방향이다. 파이프는 밀면서 회전시킬 수 있다. 
회전은 45도만 회전시킬 수 있으며, 미는 방향은 오른쪽, 아래, 또는 오른쪽 아래 대각선 방향이어야 한다.

파이프가 가로로 놓여진 경우에 가능한 이동 방법은 총 2가지, 세로로 놓여진 경우에는 2가지, 
대각선 방향으로 놓여진 경우에는 3가지가 있다.

아래 그림은 파이프가 놓여진 방향에 따라서 이동할 수 있는 방법을 모두 나타낸 것이고, 
꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.
'''
'''
#SOL1 WA
N = int( input() );
graph = [];
for i in range( N ):
    graph.append( list( map( int, input().split() ) ) );
dp = [ [ 0 ] *( N + 1 ) for _ in range( N + 1 ) ];

dp[ 1 ][ 1 ] = 0;
dp[ 1 ][ 2 ] = 1;
dp[ 2 ][ 2 ] = 1;
dp[ 2 ][ 1 ] = 1;


for x in range( 1, N + 1 ):
    for y in range( 1, N + 1 ):
        if( dp[ x ][ y ] or graph[ x - 1 ][ y - 1 ] ):
            continue;
        if( x == N  and y == N  ):
            dp[ x ][ y ] = dp[ x - 1 ][ y - 1 ] if graph[ x - 2 ][ y - 2 ] == 0 else 0;
            
        else:
            a = dp[ x - 1 ][ y ] if graph[ x - 2 ][ y - 1 ] == 0 else 0;
            b = dp[ x ][ y - 1 ] if graph[ x - 1 ][ y - 2 ] == 0 else 0;
            c = dp[ x - 1 ][ y - 1 ] if graph[ x - 2 ][ y - 2 ] == 0 else 0;
            dp[ x ][ y ] = a + b + c;
        print( ( x, y ), dp[ x ][ y ])
print( dp[ N ][ N ] );
'''

        
가로, 세로, 대각 = 0, 1, 2;

dit = { 0: [ 0, 2 ], 1: [ 1, 2 ], 2: [ 0, 1, 2 ] };

dxy = [ [ 0, 1 ], [ 1, 0 ], [ 1, 1 ] ];

        
N = int( input() );
graph = [];
for i in range( N ):
    graph.append( list( map( int, input().split() ) ) );
dp = [ [ [ 0, 0, 0 ] for x in range( N ) ] for _ in range( N ) ];

dp[ 0 ][ 1 ][ 가로 ] = 1;



for x in range( N ):
    
    for y in range( N ):
        if( graph[ x ][ y ] ):
            continue;
        for 방향 in range( 3 ):
            
            
            for 가기 in dit[ 방향 ]:
                if( 가기 == 대각 ):
                    nx, ny = x + dxy[ 가기 ][ 0 ], y + dxy[ 가기 ][ 1 ];
                    if( 0<= nx < N and 0<= ny < N ):
                        if( graph[ nx - 1 ][ ny ] or graph[ nx ][ ny - 1 ] or graph[ nx ][ ny ] ):
                            continue;
                        else:
                            dp[ nx ][ ny ][ 가기 ] += dp[ x ][ y ][ 방향 ];
                    
                else:
                    
                    nx, ny = x + dxy[ 가기 ][ 0 ], y + dxy[ 가기 ][ 1 ];
                    
                    if(  0<= nx < N and 0<= ny < N and graph[ nx ][ ny ] != 1):
                        
                        dp[ nx ][ ny ][ 가기 ] += dp[ x ][ y ][ 방향 ];


print( sum( dp[ N - 1 ][ N - 1 ] ) );                    
        

