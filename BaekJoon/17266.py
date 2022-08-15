# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:17:36 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

    


def t1():
    N = int( input() );

    M = int( input() );

    pos = list( map( int, input().split() ) );


    Object = [ _ for _ in range( N + 1 ) ];

    Objset = set( Object );

    lt = 0; rt = N;
    ans = 0;
    while lt <= rt:
        
        ranges = set();
        H = ( lt + rt ) // 2 ; 
        for i in pos:
            pos_start, pos_end = i - H, i + H;
            for col_pos in range( i - H , i + H + 1 ):
                if( col_pos < 0 ):
                    continue;
                ranges.add( col_pos );
            
        rs = Objset - ranges;
        
        if( len( rs ) == 0 ):
            ans = H;
            rt = H - 1
        else:
            lt = H + 1;


    print( ans )
    
    
    
def t2():
    N = int( input() );
    
    M = int( input() );
    
    checker = [ 0 for _ in range( N + 1 ) ];
    
    position = list( map( int,input().split() ) );
    
   
    lt, rt = 0, N ;
    
    ans = 0;
    
    while lt <= rt:
        mid = ( lt + rt ) // 2;
        checker_ = checker[ : ]
        for pos in position:
            for idx in range( pos - mid , pos + mid + 1 ):
                if( -1 < idx < N + 1 ):
                    checker_[ idx ] = 1;
            
            
        sum_ = sum( checker_ );
        
        if( sum_ >= N + 1 ):
            ans = mid;
            rt = mid -1;
        
        else:
            lt = mid + 1;
        
    
    print( ans );

def check( position, mid ):
    if( position[ 1 ] - position[ 0 ] > mid ):
        return False;
    if( position[ -1 ] - position[ -2 ] > mid ):
        return False;
    
    for i in range( 1, len( position ) - 2 ):
        if( ( position[ i + 1 ] - position[ i ] )/2  > mid ):
            return False;
    
    return True;

def t3():
    N = int( input() );
    
    M = int( input() );
    
    
    position = [ 0 ] + list( map( int,input().split() ) ) + [ N ];

    
    lt, rt = 0, N ;
    
    ans = 0;
    
    while lt <= rt:
        mid = ( lt + rt ) // 2;
        
        
        if( check( position, mid ) ):
            ans = mid;
            rt = mid - 1;
        else:
            lt = mid + 1;
        
    
    print( ans );


def t4():
    n = int(input())
    m = int(input())
    lights = list(map(int, input().split()))
    recent,Mx = lights[0],lights[0]
    
    for i in range(1,len(lights)):
        col = abs(recent-lights[i])
        
        if( col % 2 == 0 ):
            col = col // 2;
        else:
            col = ( col // 2 ) + 1;
        
        Mx = max( Mx, col );
        
        recent = lights[ i ];
    
    Mx = max( Mx, abs( n - lights[ -1 ] ) )
        
    
    print( Mx )
        
if( __name__ == "__main__" ):
    t4();
    