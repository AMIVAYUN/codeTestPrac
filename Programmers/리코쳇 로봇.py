# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:32:35 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def HowFar( dx, dy , now ):
    global graph,lenx,leny
    bias = 1;
    # 상하
    if( dx != 0 ):
        
        while 0 <= now[ 0 ] + ( dx * bias ) < lenx and graph[ now[ 0 ] + ( dx * bias ) ][ now[ 1 ] ] != 'D':
            bias += 1;
            
    #좌우
    else:
        while 0 <= now[ 1 ] + ( dy * bias ) < leny and graph[ now[ 0 ] ][ now[ 1 ] + ( dy * bias ) ] != 'D':
            bias += 1;
    
    return bias - 1;

def bfs( graph, start, checker, obj ):
    from collections import deque;
    
    dq = deque();
    
    dq.append( start );
    
    
    while dq:
        pos = dq.popleft();
        
        if( pos == obj ):
            return checker[ obj[ 0 ] ][ obj[ 1 ] ] -1;
        
        for i in range( 4 ):
            
            bias = HowFar( dx[ i ], dy[ i ], pos );
            
            nx, ny = pos[ 0 ] + ( dx[ i ] * bias ) , pos[ 1 ] + ( dy[ i ] * bias );
            
            if( checker[ nx ][ ny ] == 0 ):
                dq.append( ( nx, ny ) );
                checker[ nx ][ ny ] = checker[ pos[ 0 ] ][ pos[ 1 ] ] + 1;
    
    
    return -1;    

lenx, leny = 0, 0;
answer = 0;
graph = [];

dx, dy = [ 1, -1, 0 , 0 ], [ 0, 0, -1, 1 ];

def solution(board):
    global lenx, leny, graph,dx,dy;
    
    lenx , leny = len( board ), len( board[ 0 ] ) ;
    checker = [ [ 0 ] * leny for _ in range( lenx ) ];
    pos = ( 0, 0 );
    obj = ( 0, 0 );
    for x in range( lenx ):
        for y in range( leny ):
            if( board[ x ][ y ] == 'R' ):
                pos = ( x, y );
            elif( board[ x ][ y ] == 'G' ):
                obj = ( x, y );
    
    if( pos == obj ):
        return 0;
    
    
    checker[ pos[ 0 ] ][ pos[ 1 ] ] = 1;
    
    graph = [ list( row[:] ) for row in board ];
    graph[ pos[ 0 ] ][ pos[ 1 ] ] = '.'
    
    answer = bfs( graph, pos, checker, obj )
    return answer
    
    
    
'''
def HowFar( dx, dy , now ):
    global graph,lenx,leny
    bias = 1;
    # 상하
    if( dx != 0 ):
        
        while 0 <= now[ 0 ] + ( dx * bias ) < lenx and graph[ now[ 0 ] + ( dx * bias ) ][ now[ 1 ] ] != 'D':
            bias += 1;
            
    #좌우
    else:
        while 0 <= now[ 1 ] + ( dy * bias ) < leny and graph[ now[ 0 ] ][ now[ 1 ] + ( dy * bias ) ] != 'D':
            bias += 1;
    
    return bias - 1;

#SOL2 TIMEOUT 33.3

lenx, leny = 0, 0;
answer = 0;
graph = [];

dx, dy = [ 1, -1, 0 , 0 ], [ 0, 0, -1, 1 ];
def dfs( cnt, checker, now, obj ):

    global answer, dx, dy, lenx, leny, graph;
    row, col = 0, 1;
    x, y = now;
    if( cnt > answer ):
        return;
    
    if( now == obj ):
        answer = cnt;
        return;
    
    for i in range( 4 ):

        bias = HowFar( dx[ i ], dy[ i ], now );
        
        nx , ny = x + ( dx[ i ] * bias ) , y + ( dy[ i ] * bias );
        
        if( checker[ nx ][ ny ] != 1 ):
            checker[ nx ][ ny ] = 1;
            
            dfs( cnt + 1 , checker, ( nx, ny ), obj );
            
            checker[ nx ][ ny ] = 0;
            

            #if( checker[ nx ][ ny ] == 0 and graph[ nx ][ ny ] != 'D' ):
            #    checker[ nx ][ ny ] = 1;
            #    dfs( cnt + 1, checker, ( nx, ny ), obj );
            #    checker[ nx ][ ny ] = 0;

def solution(board):
    global answer, lenx, leny, graph,dx,dy;
    
    lenx , leny = len( board ), len( board[ 0 ] ) ;
    answer = ( lenx * leny ) ** 2;
    checker = [ [ 0 ] * leny for _ in range( lenx ) ];
    pos = ( 0, 0 );
    obj = ( 0, 0 );
    for x in range( lenx ):
        for y in range( leny ):
            if( board[ x ][ y ] == 'R' ):
                pos = ( x, y );
            elif( board[ x ][ y ] == 'G' ):
                obj = ( x, y );
    
    checker[ pos[ 0 ] ][ pos[ 1 ] ] = 1;
    
    graph = [ list( row[:] ) for row in board ];
    graph[ pos[ 0 ] ][ pos[ 1 ] ] = '.'
    
    dfs( 0,checker, pos ,obj );
    

    
    
    return answer if answer != ( lenx * leny ) ** 2 else -1;




#SOL1

def solution(board):
    answer = float( 'inf' );
    dx = [ -1, 1 ,0 ,0 ]; 
    dy = [ 0 , 0, -1, 1 ];
    lenx = len( board );
    leny = len( board[ 0 ] );
    pos = ( 0, 0 );
    checker = [ [ 0 for i in range( leny ) ]for _ in range( lenx ) ]
    for x in range( lenx ):
        for y in range( leny ):
            if( board[ x ][ y ] == 'R' ):
                pos = ( x, y );
                break;
    checker[ x ][ y ] = 1;
    from collections import deque;
    
    dq = deque();
    
    dq.append( ( 0, x, y ) );
    
    while dq:
        print( dq );
        cnt, x, y = dq.popleft();
        
        if( cnt > answer ):
            continue;
            
        if( board[ x ][ y ] == 'G' ):
            answer = cnt;
            continue;
    
        for i in range( 4 ):

            if( i < 2 ):
                # 상하
                direc = dx[ i ];
                bias = 1;
                
                while -1 < x + ( direc * bias  ) < lenx and board[ x + ( direc * bias ) ][ y ] != 'D':

                    bias += 1;
                
                nx = x + ( direc * bias )
                if nx < 0:
                    nx = 0;
                elif nx == lenx:
                    nx -= 1;
                
                if( x != nx and checker[ nx ][ y ] ):
                    print( nx , y );
                    checker[ nx ][ y ] = 1;
                    dq.append( ( cnt + 1, nx, y ) );
                    
                    
                    
            else:
                # 좌우
                direc = dy[ i ];
                bias = 1;
                
                while -1 < y + ( direc * bias  ) < leny and board[ x ][ y + ( direc * bias ) ] != 'D':
                    bias += 1;
                ny = y + ( direc * bias )
                if ny < 0:
                    ny = 0;
                elif ny == leny:
                    ny -= 1;
                if( y != ny and checker[ x ][ ny ] ):
                    print( x, ny )
                    checker[ x ][ ny ] = 1;
                    dq.append( ( cnt + 1, x, ny ) );
  
    print( answer );
    return answer 
'''