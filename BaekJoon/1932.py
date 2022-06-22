# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:34:29 2022
@FileName: 1932.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1932
"""
# 1 풀이 미스
def main1():
    N = int( input() );
    lst = [];
    rs = [ ];
    for _ in range( N ):
        lst.append( list(map( int, input().split() ) ) );
        
    rs.append( sum( [ lst[ i ][ 0 ] for i in range( N ) ] ) );
    rs.append( sum( [ lst[ i ][ -1 ] for i in range( N ) ] ) );
    
    
    for _ in range( 1, N - 1 ):
        start = lst[ 0 ][ 0 ] + max( lst[ 1 ][ 0 ], lst[ 1 ][ 1 ] ) + lst[ N - 1 ][ _ ];
        
        for j in range ( N - 1, 2, -1 ):
            nextP = max( lst[ j - 1 ][ _ - 1 ], lst[ j - 1 ][ _ ] );
            print( _, nextP )
            start += nextP;
                    
        rs.append( start );
    
    print( rs );


#2 답 도출 실패
def main2():
    N = int( input() );
    lst = [];
    rs = [ ];
    for _ in range( N ):
        lst.append( list(map( int, input().split() ) ) );
        
    rs.append( sum( [ lst[ i ][ 0 ] for i in range( N ) ] ) );
    rs.append( sum( [ lst[ i ][ -1 ] for i in range( N ) ] ) );
    
    
    dp = [ [ 0 ] * len( lst[ i ] ) for i in range( len( lst ) ) ]
   
    
    for i in range( 1, N - 1 ):
        dp[ N - 1 ][ i ] = lst[ 0 ][ 0 ] + max( lst[ 1 ][ 0 ], lst[ 1 ][ 1 ] ) + lst[ N - 1 ][ i ];
    
    
    print( dp )
    
    
    for i in range( N - 2 , 1, -1 ):
        for j in range( 1, len( lst[ i ] ) ):
            dp[ i ][ j ] = max( lst[ i ][ j ] + dp[ i + 1 ][ j ], lst[ i ][ j ] + dp[ i + 1 ][ j + 1 ]) ;
    
    print( dp );
    print( rs );


def main():
    N = int( input() );
    lst = [];
    if( N == 1 ):
        print( int( input( ) ) );
        return;
    for _ in range( N ):
        lst.append( list(map( int, input().split() ) ) );
    

    dp = [ [ 0 ] * len( lst[ i ] ) for i in range( len( lst ) ) ]
    
    dp[ 0 ][ 0 ] = lst[ 0 ][ 0 ];

    
    
    for i in range( N ):
        for j in range( len( lst[ i ] ) ):
            if( j == 0 ):
                dp[ i ][ j ] = dp[ i - 1 ][ j ] + lst[ i ][ j ]
                
            elif( j == i ):
                dp[ i ][ -1 ] = dp[ i - 1 ][ -1 ] + lst[ i ][ -1 ];
            else:
                dp[ i ][ j ] = max( dp[ i - 1 ][ j - 1 ], dp[ i - 1 ][ j ] ) + lst[ i ][ j ];
            
    
    print( max( dp[ N - 1 ] ) );




if( __name__ == "__main__"):
    main()