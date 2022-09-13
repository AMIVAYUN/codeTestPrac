# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:53:04 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def sol1():
   
    #sol1

    N, M = map( int, input().split() )

    graph = [];

    col = [];

    now = ( N * M ) + 2;

    for i in range( N ):
        row = input();
        introw = [];
        for y in range( M ):
            introw.append( int( row[ y ] ) );
            if( introw[ y ] ):
                col.append( ( i, y ) ) 
                
        graph.append( introw );
            

    def bfs( graph, N, M ):
        global now;
        dx, dy = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ];
        from collections import deque;
        deq = deque();
        
        visit = [ [ 1 ] * M for _ in range( N ) ];
        visit[ 0 ][ 0 ] = 0;
        deq.append( ( ( 0, 0 ), 1 ) );
        
        while deq:
            print( deq )
            pos, cnt = deq.popleft();
            
            x, y = map( int, pos );
            
            if( cnt > now ):
                break;
            
            if( x == N - 1 and y == M - 1 ):
                now = min( now, cnt );
                break;
            
            
            for i in range( 4 ):
                nx = x + dx[ i ];
                ny = y + dy[ i ];
                
                if( 0<= nx < N and 0<= ny < M ):
                    if( visit[ nx ][ ny ] and graph[ nx ][ ny ] != 1):
                        visit[ nx ][ ny ] = 0;
                        
                        deq.append( ( ( nx, ny ), cnt + 1 ) );
            
        
        return


    bfs( graph, N, M );


    for pos in col:
        tmp = [ row[:] for row in graph[:] ];
        
        tmp[ pos[ 0 ] ][ pos[ 1 ] ] = 0;
        
        bfs( tmp, N, M );


    print( now ) if now != ( N * M ) + 2 else -1

def sol2():
    N, M = map( int, input().split() )

    graph = [];

    col = [];

    now = ( N * M ) + 2;

    for i in range( N ):
        row = input();
        introw = [];
        for y in range( M ):
            introw.append( int( row[ y ] ) );
            if( introw[ y ] ):
                col.append( ( i, y ) ) 
                
        graph.append( introw );
            
    ans = [];
    def bfs2( graph, N, M ):
        global ans;
        dx, dy = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ];
        from collections import deque;
        deq = deque();
        
        visit = [ [ 1 ] * M for _ in range( N ) ];
        visit[ 0 ][ 0 ] = 0;
        
        
        deq.append( ( ( 0, 0 ), ( 1, 0 ), [ row[:] for row in visit[:] ] ) ) # pos, ( cnt, 1의 개수 );
        
        while deq:
            pos, cnttup, visit = deq.popleft();
            
            cnt, num1 = map( int, cnttup );
            if( num1 > 1 ):
                continue;
            x, y = map( int, pos );
            if( pos[ 0 ] == N - 1 and pos[ 1 ] == M - 1 ):
                if( num1 < 2 ):
                    ans.append( cnt );
            
            for i in range( 4 ):
                nx = x + dx[ i ];
                ny = y + dy[ i ];
                
                if( 0<= nx < N and 0<= ny < M ):
                    if( num1 ):
                        if( visit[ nx ][ ny ] and graph[ nx ][ ny ] != 1 ):
                            tmp = [ row[:] for row in visit[:] ];
                            tmp[ nx ][ ny ] = 0;
                            deq.append( ( ( nx, ny ), ( cnt + 1, num1 + graph[ nx ][ ny ] ), tmp ) ) 
                    else:
                        
                        if( visit[ nx ][ ny ] ):
                            tmp = [ row[:] for row in visit[:] ];
                            tmp[ nx ][ ny ] = 0;
                            deq.append( ( ( nx, ny ), ( cnt + 1, num1 + graph[ nx ][ ny ] ), tmp ) ) 
            
        return;
        

    bfs2( graph, N, M );

    print( min( ans ) if len( ans ) else -1 ) ;


def sol3():
    N, M = map( int, input().split() )

    graph = [];

    col = [];

    now = ( N * M ) + 2;

    for i in range( N ):
        row = input();
        introw = [];
        for y in range( M ):
            introw.append( int( row[ y ] ) );
            if( introw[ y ] ):
                col.append( ( i, y ) ) 
                
        graph.append( introw );
            
    ans = [];
    def bfs3( graph, N, M ):
        global ans;
        dx, dy = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ];
        from collections import deque;
        deq = deque();
        
        visit = [ [ 1 ] * M for _ in range( N ) ];
        visit[ 0 ][ 0 ] = 0;
        
        
        deq.append( ( ( 0, 0 ), ( 1, 0 ) ) ) # pos, ( cnt, 1의 개수 );
        
        while deq:
            pos, cnttup = deq.popleft();
            
            cnt, num1 = map( int, cnttup );
            
            x, y = map( int, pos );
            if( pos[ 0 ] == N - 1 and pos[ 1 ] == M - 1 ):
               ans.append( cnt );
               continue;
            
            for i in range( 4 ):
                nx = x + dx[ i ];
                ny = y + dy[ i ];
                
                if( 0<= nx < N and 0<= ny < M ):
                    if( visit[ nx ][ ny ] ):
                        
                        if( num1 ):
                            if( graph[ nx ][ ny ] != 1 ):
                                visit[ nx ][ ny ] = 0;
                                deq.append( ( ( nx, ny ), ( cnt + 1, num1 ) ) ) 
                        else:
                            
                            visit[ nx ][ ny ] = 0;
                            deq.append( ( ( nx, ny ), ( cnt + 1, num1 + graph[ nx ][ ny ] ) ) ) 
            
        return;
        

    bfs3( graph, N, M );

    print( min( ans ) if len( ans ) else -1 ) ;


def sol4():
    N, M = map( int, input().split() )

    graph = [];

    col = [];

    now = ( N * M ) + 2;

    for i in range( N ):
        row = input();
        introw = [];
        for y in range( M ):
            introw.append( int( row[ y ] ) );
            if( introw[ y ] ):
                col.append( ( i, y ) ) 
                
        graph.append( introw );
            
    ans = [];
    def bfs4( graph, N, M ):
        global ans;
        dx, dy = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ];
        

        result = [ [ ( ( N * M ) + 2, 0 ) ] * M for _ in range( N ) ]
        result[ 0 ][ 0 ] = ( 1, 0 );
        
        from collections import deque;
        deq = deque();
        

        
        deq.append( ( ( 0, 0 ), ( 1, 0 ) ) ) # pos, ( cnt, 1의 개수 );
        while deq:
            pos, cnttup = deq.popleft();
            
            cnt, num1 = map( int, cnttup );
            
            x, y = map( int, pos );
            if( cnt > result[ x ][ y ][ 0 ] ):
                continue;
            if( x == N - 1 and y == M - 1 ):
                case = result[ x ][ y ];
                if( case[ 0 ] < cnt ):
                    continue;
                else:
                    result[ x ][ y ] = ( cnt, num1 )
                
                    continue;
                    
            for i in range( 4 ):
                nx = x + dx[ i ];
                ny = y + dy[ i ];
                
                if( 0<= nx < N and 0<= ny < M ):
                    if( num1 ):
                        if( graph[ nx ][ ny ] != 1 and result[ nx ][ ny ][ 0 ] > cnt + 1 ):
                            result[ nx ][ ny ] = ( cnt + 1, num1 );
                            deq.append( ( ( nx, ny ), ( cnt + 1, num1 ) ) )
                    else:
                        if( result[ nx ][ ny ][ 0 ] > cnt + 1 or result[ nx ][ ny ][ 1 ] > num1 ):
                            result[ nx ][ ny ] = ( cnt + 1, num1 + graph[ nx ][ ny ] );
                            deq.append( ( ( nx, ny ), ( cnt + 1, num1 + graph[ nx ][ ny ] ) ) )
                    

        return result[ N - 1 ][ M - 1 ][ 0 ];
        
    ans = bfs4( graph, N, M )
    print( ans if ans != ( N * M ) + 2 else -1 );

def ans():
    

    N, M = map( int, input().split() )

    graph = [];

    col = [];

    now = ( N * M ) + 2;

    for i in range( N ):
        row = input();
        introw = [];
        for y in range( M ):
            introw.append( int( row[ y ] ) );
            if( introw[ y ] ):
                col.append( ( i, y ) ) 
                
        graph.append( introw );
            
    ans = [];
    def bfs5( graph, N, M ):
        global ans;
        dx, dy = [ -1, 1, 0, 0 ], [ 0, 0, -1, 1 ];
        

        result = [ [ [ ( N * M ) + 2 ,( N * M ) + 2 ] for row in range( M ) ]  for _ in range( N ) ]
        result[ 0 ][ 0 ] = [ 1, 1 ];
        from collections import deque;
        deq = deque();
        

        
        deq.append( ( ( 0, 0 ), ( 1, 0 ) ) ) # pos, ( cnt, 1의 개수 );
        while deq:
            pos, cnttup = deq.popleft();
            
            cnt, num1 = map( int, cnttup );
            
            x, y = map( int, pos );
            
        
            if( cnt > result[ N - 1 ][ M - 1 ][ 0 ] ):
                continue;
            if( x == N - 1 and y == M - 1 ):
                result[ x ][ y ][ num1 ] = min( result[ x ][ y ][ num1 ], cnt );
                
                continue;
                    
            for i in range( 4 ):
                nx = x + dx[ i ];
                ny = y + dy[ i ];
                
                if( 0<= nx < N and 0<= ny < M ):

                    if( num1 ):
                        if( graph[ nx ][ ny ] != 1 and result[ nx ][ ny ][ num1 ] > cnt + 1 ):
                            result[ nx ][ ny ][ num1 ] = cnt + 1;
                            deq.append( ( ( nx, ny ), ( cnt + 1, num1 ) ) )
                    else:
                        if( result[ nx ][ ny ][ num1 ] > cnt + 1 ):
                            num1_ = num1 + graph[ nx ][ ny ];
                            result[ nx ][ ny ][ num1_ ] = cnt + 1;
                            deq.append( ( ( nx, ny ), ( cnt + 1, num1_ ) ) )
                    

        return min( result[ N - 1 ][ M - 1 ] );
        
    ans = bfs5( graph, N, M )
    print( ans if ans != ( N * M ) + 2 else -1 );