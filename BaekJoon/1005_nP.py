# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:32:23 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def bfs( N, graph, start, D ):
    from collections import deque;
    
    deq = deque();
    
    deq.append( ( start, 0 ) )
    
    visit = [ 1 ] * N;
    visit[ start ] = 0;
    depthMx = [ 0 ] * N;
    print( D )
    depthMx[ 0 ] = D[ start ];
    print( depthMx );
    while deq:
        print( deq, visit );
        pos, depth = deq.popleft();
        
        if( depth == N ):
            continue; 
            
        for i in graph[ pos ]:
            if( visit[ i ] ):
                visit[ i ] = 0;    
                depthMx[ depth + 1 ] = max( D[ i ], depthMx[ depth + 1 ] );
                deq.append( ( i, depth + 1 ) );
        
        
    print( depthMx );
    return sum( depthMx );
#Memory Out
def bfs2( N, graph, start, D ):
    from collections import deque;
    
    deq = deque();
    
    deq.append( ( start, 0 ) )
    
    visit = [ 1 ] * N;
    visit[ start ] = 0;
    TechTree = [ set() for _ in range( N ) ];
    TechTree[ 0 ].add( start );

    while deq:
        
        pos, depth = deq.popleft();
        
        if( depth == N ):
            continue; 
            
        for i in graph[ pos ]:
            
            if( visit[ i ] == 0 ):
                TechTree[ depth + 1 ].add( i );
                deq.append( ( i, depth + 1 ) );
            
            else:
                visit[ i ] = 0;
                TechTree[ depth + 1 ].add( i );
                deq.append( ( i, depth + 1 ) )
    
    
    union = TechTree[ len( TechTree ) - 1 ];
    for idx in range( len( TechTree ) - 2, 0, -1 ):
 
        TechTree[ idx ] = TechTree[ idx ] - union;
        union = union | TechTree[ idx ];

    

    res = [ 0 ] * N ;
    
    for i in range( N ):
        res[ i ] = max( [ D[ idx ] for idx in TechTree[ i ] ] + [ 0 ] );
    return sum( res );    

T = int( input() );

for i in range( T ):
    N , K = map( int, input().split() );
    D = list( map( int, input().split() ) ) ;
    graph = [ [] for _ in range( N ) ];
    for i in range( K ):
        a, b = map( int, input().split() );
        
        graph[ b - 1 ].append( a - 1 );
        
    
    start = int( input() );
    
    start -= 1;
    
    
    print( bfs2( N, graph, start, D ) );
    
    


