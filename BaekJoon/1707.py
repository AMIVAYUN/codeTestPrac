# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:38:08 2022
@FileName: 1707.py
@author: YUNJUSEOK

@Link:https://www.acmicpc.net/problem/1707
"""

#dfs Memory Exceeded 

# 앞으로 메모리 , 시간 초과가 뜰 경우에는 항상 빠르게 BFS로 먼저 풀어보자
def dfs( y, con ):
    global graph,visited;
    
    
    if( visited[ y ] == con ):
        return True;
    if( visited[ y ] == con * -1 ):
        return False;
    

    visited[ y ] = con;
    
    
    
    for i in range( 1, V + 1 ):
        if( graph[ y ][ i ] == 1 ):
            graph[ y ][ i ] = 0;
            graph[ i ][ y ] = 0;
            if( visited[ i ] == con ):
                return False;
            elif( visited[ i ] == con * -1 ):
                return True;
            else:
                dfs( i, con * -1 );
    
    return True;


def bfs( y ):
    global visit,adj,color;
    from collections import deque;
    deq = deque();
    deq.append( y )
    if( visit[ y ] == 0 ):
        visit[ y ] = 1;
    while deq:
        i = deq.popleft();
        con = visit[ i ];
    
        for k in adj[ i ]:
            if visit[ k ] == 0:
                deq.append( k );
                visit[ k ] = con * -1;
            elif con == visit[ k ]:
                return False;
            
                
            
    
    return True;
        
        
    


K = int( input() );

for i in range( K ):
    V, E = map( int, input().split() );
    adj = [ [] for i in range( V + 1 ) ];
    color = [ 0 ] * ( V + 1 );
    visit = [0] * ( V + 1 ); 
    for i in range( E ):
        a, b = map( int, input().split() );
        adj[ a ].append( b );
        adj[ b ].append( a );
    result = None;
    for j in range( 1, V + 1 ):
        if( not( bfs( j ) ) ):
            result = 0;
            
        
    
    print( "No" if result == 0 else "YES" );
        
        
    
        
    

    



            
    
    
    
        
