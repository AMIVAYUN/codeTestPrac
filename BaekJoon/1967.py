# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:25:01 2022
@FileName: 1967.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1967
"""


#Memory Exceeded; 1967
N = int( input() )

graph = [ [0 for i in range( N + 1 ) ]  for j in range( N + 1 )];

visit =  [ 1 ] * ( N + 1 ) ;

Mx = 0;

for i in range( N - 1 ):
    x, y, z = map( int, input().split() );
    
    graph[ x ][ y ] = z;
    graph[ y ][ x ] = z;

    

def dfs( x, value ):
    global graph,visit,Mx,N;

    for i in range( 1, N + 1 ):
        if( visit[ i ] and graph[ x ][ i ] != 0 ):
            visit[ i ] = 0;
            dfs( i, value + graph[ x ][ i ]);
            visit[ i ] = 1;
    
    Mx = max( Mx,value );
    return
    
for i in range( 1, N + 1 ):
    visit[ i ] = 0;
    
    for j in range( 1, N + 1 ):
        if( visit[ j ] and graph[ i ][ j ] != 0 ):
            visit[ j ] = 0;
            dfs( j, graph[ i ][ j ] );
            visit[ j ] = 1;
            
    visit[ i ] = 1;
    
    
    
    
print( Mx )
    
    


#2
N = int( input() );
graph = [ [] for i in range( N + 1 ) ];

visit =  [ 1 ] * ( N + 1 ) ;

Mx = 0;

for i in range( N - 1 ):
    x, y, z = map( int, input().split() );
    graph[ x ].append( ( y, z ) );
    graph[ y ].append( ( x, z ) );


    

def dfs( x ,value):
    global graph,visit,Mx,N;
    
    for i in graph[ x ]:
        if( visit[ i[ 0 ] ] ):
            visit[ i[ 0 ] ] = 0;
            dfs( i[ 0 ], value + i[ 1 ] );
            visit[ i[ 0 ] ] = 1;
    Mx = max( Mx,value );
    return



for i in range( 1, N + 1 ):
    visit[ i ] = 0;
    
    for j in graph[ i ]:
        if( visit[ j[ 0 ] ] ):
            visit[ j[ 0 ] ] = 0;
            dfs( j[ 0 ], j[ 1 ] );
            visit[ j[ 0 ] ] = 1;
            
    visit[ i ] = 1;
    
    
    
    
print( Mx )


#3
N = int( input() );
graph = [ [] for i in range( N + 1 ) ];

visit =  [ 1 ] * ( N + 1 ) ;

Mx = 0;

for i in range( N - 1 ):
    x, y, z = map( int, input().split() );
    graph[ x ].append( ( y, z ) );
    graph[ y ].append( ( x, z ) );


    
dis = [ ( -1, 0 ) ] * ( N + 1 );
def dfs( x, value ):
    global graph,dis,N;
    for i in graph[ x ]:
        if( dis[ i [ 0 ] ][ 0 ] == -1 ):
            dis[ i [ 0 ] ] = ( value + i[ 1 ], i[ 0 ] );
            dfs( i[ 0 ] , value + i[ 1 ] );

    
    return

# 트리의 정점은 임의의 정점 x에서 가장 먼 임의의 정점 y가 가장 먼 정점 t 와 의 거리 dis( y, t )이다.
dis[ 1 ] == ( 0, 1 )
dfs( 1, 0 );

faridx = max( dis );

dis = [ ( -1, 0 ) ] * ( N + 1 );


dis[ faridx[ 1 ] ] = ( 0, faridx[ 1 ] );

dfs( faridx[ 1 ], 0 );

print( max( dis )[ 0 ] )


