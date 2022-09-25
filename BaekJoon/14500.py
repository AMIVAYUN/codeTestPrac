# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:58:37 2022
@FileName: 14500.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/14500
"""

dx = [ -1, 1, 0, 0 ];

dy = [ 0, 0, -1, 1 ];

def checkT( x, y,value ):
    global graph,dx,dy,n,m,Mx;
    lst = [ 0 ] * 4;
    for i in range( 4 ):
        nx = x + dx[ i ];
        ny = y + dy[ i ];
        
        if( 0<= nx < n and 0<= ny < m ):
            lst[ i ] = graph[ nx ][ ny ];
    
    if( lst.count( 0 ) > 1 ):
        return;
    
    elif( lst.count( 0 ) == 1 ):
        Mx = max( Mx, sum( lst ) + value );
    
    else:
        lst = list( sorted( lst ) );
        Mx = max( Mx, sum( lst[ 1: ] ) + value )

    return;
def dfs( depth,x,y, weight ):
    global graph,Mx,dx,dy,visit,n,m
    if( depth == 3 ):
        Mx = max( Mx, weight)
        
    else:
        for i in range( 4 ):
            nx = x + dx[ i ];
            ny = y + dy[ i ];
            
            if( 0<= nx < n and 0<= ny < m ):
                if( visit[ nx ][ ny ] ):
                    visit[ nx ][ ny ] = 0;
                    dfs( depth + 1, nx, ny, weight + graph[ nx ][ ny ] );
                    visit[ nx ][ ny ] = 1;
                    
n, m = map( int, input().split() );

visit =[ [ 1 ] * m for _ in range( n ) ];
graph = [];
Mx = 0;

for i in range( n ):
    graph.append( list( map( int, input().split() ) ) );
    

for x in range( n ):
    for y in range( m ):
        if( visit[ x ][ y ] ):
            visit[ x ][ y ] = 0;
            dfs( 0, x, y, graph[ x ][ y ] );
            checkT( x, y, graph[ x ][ y ] )
            visit[ x ][ y ] = 1;
    

print( Mx )    



