# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:44:53 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
Mn = float( 'inf' );
def getMn( graph ):
    global Mn;
    for row in graph:
        Mn = min( Mn, sum( row ) );
    
    return;
    
from collections import deque;
def rotateX( graph, flag ,start, end , dq ):

    #상단
    if( flag ):
        
        x, ny = start[ 0 ] , start[ 1 ] + 1;
        while ny <= end[ 1 ]:

            dq.append( graph[ x ][ ny ] );
            graph[ x ][ ny ] = dq.popleft();
            ny += 1;
    #하단
    else:
        x, ny = end[ 0 ], end[ 1 ] - 1;
        while ny >= start[ 1 ]:
 
            dq.append( graph[ x ][ ny ] );
            graph[ x ][ ny ] = dq.popleft();
            ny -= 1;
    
    return graph, dq;

def rotateY( graph, flag, start, end, dq ):


    if( flag ):
        
        nx, y = start[ 0 ] + 1, end[ 1 ];
        while nx <= end[ 0 ]:
            

            dq.append( graph[ nx ][ y ] );
            graph[ nx ][ y ] = dq.popleft();
            nx += 1;
    #하단
    else:
        nx, y = end[ 0 ] - 1, start[ 1 ];
        while nx >= start[ 0 ]:
            dq.append( graph[ nx ][ y ] );
            graph[ nx ][ y ] = dq.popleft();
            nx -= 1;
    
    return graph, dq;

def FullRotate( graph, start, end ):

    dq = deque();
    if( start[ 0 ] ==  end[ 0 ] and start[ 1 ] == end[ 1 ] ):
        return graph;
    else:
        dq.append( graph[ start[ 0 ] ][ start[ 1 ] ] );
        graph, dq = rotateX( graph, True, start, end, dq );
        graph, dq = rotateY( graph, True, start, end, dq );
        graph, dq = rotateX( graph, False, start, end, dq );
        graph, dq = rotateY( graph, False, start, end, dq );

        return FullRotate( graph, ( start[ 0 ] + 1 , start[ 1 ] + 1 ), ( end[ 0 ] - 1 , end [ 1 ] - 1))
        
x, y, T = map( int ,input().split() );
graph = [];

for i in range( x ):
    graph.append( list( map( int, input().split() ) ) );

cases = [];
for case in range( T ):
    c = tuple( map( int, input().split() ) ); 
    cases.append( ( c[ 0 ] , c[ 1 ], c[ 2 ] ) );
dq = deque( cases );
import itertools;

perm = list( itertools.permutations( cases, T ) )
temp = [ row[:] for row in graph[:] ]
while perm:
    
    graph= [ row[:] for row in temp[:] ]

    case = perm.pop();
    
    for c in case:
        
    
        graph = FullRotate( graph, (c[ 0 ] - c[ 2 ] - 1, c[ 1 ]- c[ 2 ] - 1 ),(c[ 0 ] + c[ 2 ] - 1, c[ 1 ]+ c[ 2 ] -1 ) );
    
    
    getMn( graph );
print( Mn )


'''

from collections import deque;
graph =[  [1, 2, 3, 2, 5, 6 ],[3, 8, 7, 2, 1, 3,],
[8, 2, 3, 1, 4, 5,],
[3, 4, 5, 1, 1, 1,],
[9, 3, 2, 1, 4, 3,] ] 
for row in graph:
    print( row );
    
graph = FullRotate( graph, ( 0, 0 ), ( 4, 4 ) );

for row in graph:
    print( row )
    




dq = deque();

graph = [ [1, 2, 3, 2, 5, 6 ],
[3, 8, 7, 2, 1, 3,],
[8, 2, 3, 1, 4, 5,],
[3, 4, 5, 1, 1, 1,],
[9, 3, 2, 1, 4, 3,] ] 

for row in graph:
    print( row );
    
dq.append( ( graph[ 0 ][ 0 ] ) );

start = ( 0, 0 ); end = ( 4, 5 );
graph, dq = rotateX( graph, True, start, end, dq );
graph, dq = rotateY( graph, True, start, end, dq );
graph, dq = rotateX( graph, False, start, end, dq );
graph, dq = rotateY( graph, False, start, end, dq );

print( "--")

for row in graph:
    print( row );

'''