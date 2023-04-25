# sol3 dfs + marking 
answer = 0;
dx = [ 0, 0, 1, -1 ];
dy = [ 1, -1, 0, 0 ];
flag = False;
'''
해당 로직으로는 가지치기 수가 부족해 Timeout이 난다.
def CanbeLoop( N,R, graph, mapper ,now ):
    global dx, dy;
    
    x , y = now;
    Mx = 0;
    cnt = 0;
    for i in range( 4 ):
        
        dxi = dx[ i ];
        dyi = dy[ i ];
        dxi, dyi = dx[ i ], dy[ i ];

        if( graph[ x ][ y ] == 'H' ):
            break;
            
        nx = x + ( dxi * int( graph[ x ][ y ] ) );
        ny = y + ( dyi * int( graph[ x ][ y ] ) );
        
        
        
        if( 0<= nx < N and 0<= ny < R ):
            Mx += 1;
            if( graph[ nx ][ ny ] != 'H' and mapper[ nx ][ ny ] > 0 and mapper[ nx ][ ny ] < mapper[ x ][ y ]  ):
                cnt += 1;    
    if ( Mx ):
        return Mx == cnt;
    
    return False;
'''
def dfs( N,R,graph, visit,mapper, count, now ):
    global flag;
    global answer;
    global dx, dy;


    x, y = now;
    '''
    if( mapper[ x ][ y ] ):
        if( CanbeLoop( N,R,graph,mapper ,now ) ):
            print( now, mapper)
            flag = True;
            answer = -1;
            return;
    '''
    

        
    if( graph[ x ][ y ] == 'H' ):
        answer = max( answer, count - 1 );
        return;
       
  
        

    for i in range( 4 ):
        
        if( flag ):
            return;
            
        dxi = dx[ i ];
        dyi = dy[ i ];
        dxi, dyi = dx[ i ], dy[ i ];

        nx = x + ( dxi * int( graph[ x ][ y ] ) );
        ny = y + ( dyi * int( graph[ x ][ y ] ) );
        

            
        
        if( 0<= nx < N and 0<= ny < R ):

            if( mapper[ nx ][ ny ] < count + 1 ):
                if( visit[ nx ][ ny ] ):
                    flag = True;
                    answer = -1;
                    return;
                    
                mapper[ nx ][ ny ] = count + 1;
                visit[ nx ][ ny ] = 1;
                dfs( N, R, graph,visit, mapper, count + 1, ( nx, ny ) );
                visit[ nx ][ ny ] = 0;

                
        else:
            answer = max( count , answer );
        
    

    return;
    

def main():
    
    global answer;
    

    
    N, R = map( int, input().split() ) 

    mapper = [ [ 0 ] * R for _ in range( N ) ];    


    graph = [];
    for ro in range( N ):
        graph.append( input() );
    
    
    
    mapper = [ [ 0 for _1 in range( R ) ]  for _ in range( N ) ];
    
    visit = [ row[:] for row in mapper ];
    
    mapper[ 0 ][ 0 ] = 1;
    visit[ 0 ][ 0 ] = 1;
    
    dfs( N,R,graph, visit,mapper, 1, ( 0, 0 ) );
    
    print( answer );

    return;
if( __name__ == "__main__" ):
    main();
'''
# sol2 dfs TIMEOUT
answer = 0;
dx = [ 0, 0, 1, -1 ];
dy = [ 1, -1, 0, 0 ];
flag = False;
def CanbeLoop( N,R, graph, mapper ,now ):
    global dx, dy;
    
    x , y = now;
    for i in range( 4 ):
        
        dxi = dx[ i ];
        dyi = dy[ i ];
        dxi, dyi = dx[ i ], dy[ i ];

        if( graph[ x ][ y ] == 'H' ):
            continue;
            
        nx = x + ( dxi * int( graph[ x ][ y ] ) );
        ny = y + ( dyi * int( graph[ x ][ y ] ) );
        
        
        
        if( 0<= nx < N and 0<= ny < R ):
            if( graph[ nx ][ ny ] != 'H' and mapper[ nx ][ ny ] ):
                return True;
    
    return False;

def dfs( N,R,graph, mapper, count, now ):
    
    global answer;
    global dx, dy;
    global flag;

    x, y = now;
    
    if( mapper[ x ][ y ] ):
        if( CanbeLoop( N,R,graph,mapper ,now ) ):
            flag = True;
            answer = -1;
            return;
    
    
    if( flag ):
        return;
        
    if( graph[ x ][ y ] == 'H' ):
        answer = max( answer, count - 1 );
        return;
       
  
        

    for i in range( 4 ):
        
        if( flag ):
            mapper[ x ][ y ] = 0;
            return;
            
        dxi = dx[ i ];
        dyi = dy[ i ];
        dxi, dyi = dx[ i ], dy[ i ];

        nx = x + ( dxi * int( graph[ x ][ y ] ) );
        ny = y + ( dyi * int( graph[ x ][ y ] ) );
        

            
        
        if( 0<= nx < N and 0<= ny < R ):

            if( mapper[ nx ][ ny ] == 0 and flag != True):

                mapper[ nx ][ ny ] = 1;
                
                dfs( N, R, graph, mapper, count + 1, ( nx, ny ) );
                mapper[ nx ][ ny ] = 0;

                
        else:
            answer = max( count , answer );
        
            

    return;
    

def main():
    
    global answer;
    

    
    N, R = map( int, input().split() ) 

    mapper = [ [ 0 ] * R for _ in range( N ) ];    


    graph = [];
    for ro in range( N ):
        graph.append( input() );
    
    
    
    mapper = [ [ 0 for _1 in range( R ) ]  for _ in range( N ) ];
    
    
    
    mapper[ 0 ][ 0 ] = 1;

    
    dfs( N,R,graph, mapper, 1, ( 0, 0 ) );
    
    print( answer );

    return;
if( __name__ == "__main__" ):
    main();
    
# SOL 6% bfs Timeout;
def isOK( N, R,graph,x, y ):
    dx = [ 0, 0, 1, -1 ];
    dy = [ 1, -1, 0, 0 ];
    for i in range( 4 ):
        
        dxi = dx[ i ];
        dyi = dy[ i ];
        dxi, dyi = dx[ i ], dy[ i ];

    
        nx = x + ( dxi * int( graph[ x ][ y ] ) );
        ny = y + ( dyi * int( graph[ x ][ y ] ) );
        
        
        
        if( 0<= nx < N and 0<= ny < R ):
            if( graph[ nx ][ ny ] != 'H' ):
                return False;
    
    return True;

def main():
    
    cnt = 0;
    
    from collections import deque;
    
    N, R = map( int, input().split() ) 

    
    dq= deque();
    graph = [];
    for ro in range( N ):
        graph.append( input() );
    
    
    
    mapper = [ [ 0 ] * R for _ in range( N ) ];
    
    
    dq.append( [ ( 0, 0 ) , 0, mapper[:] ] );
    
    
    Mx = 0;
    
    dx = [ 0, 0, 1, -1 ];
    dy = [ 1, -1, 0, 0 ];
    
    mapper[ 0 ][ 0 ] = 1;
    while dq:

        pos, cnt, check = dq.popleft();

        x, y = pos;
        if( graph[ x ][ y ] == 'H' ):
            Mx = max( Mx, cnt );
            continue;
        
        

        for i in range( 4 ):
            
            dxi = dx[ i ];
            dyi = dy[ i ];
            dxi, dyi = dx[ i ], dy[ i ];

        
            nx = x + ( dxi * int( graph[ x ][ y ] ) );
            ny = y + ( dyi * int( graph[ x ][ y ] ) );
            
            
            
            if( 0<= nx < N and 0<= ny < R ):

                if( check[ nx ][ ny ] ):

                    if( isOK( graph, nx , ny ) ):
                        newcheck = [ row[: ] for row in check[ : ] ];
                        newcheck[ nx ][ ny ] = 1;
                        dq.append( [ ( nx, ny ), cnt + 1, newcheck ] );
                    
                    else:
                        print( -1 );

                        return;
                        
                else:
                    
                    newcheck = [ row[:] for row in check[:] ]
                    newcheck[ nx ][ ny ] = 1;
                    dq.append( [ ( nx, ny ), cnt + 1, newcheck ] );
                
            else:
                Mx = max( cnt + 1 , Mx )
            

    print( Mx );


if( __name__ == "__main__" ):
    main();
'''