# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:40:25 2022
@FileName: 1149.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1149
"""


# 빨초파로 나눠서 해보자




def main1():
    R,G,B = 0, 1, 2;
    N = int( input() );
    lst = [];
    rs = [];
    for _ in range( N ):
        lst.append( list( map( int, input().split() ) ) )
    
    
    start0 = 0;
    sum0 = 0;
    sum1 = 0
    start1 = 0
    
    for j in range( len( lst ) ):
        sum0 += lst[ j ][ start0 % 3 ];
        sum1 += lst[ j ][ start1 ]
        start0 += 1;
        start1 -= 1;
        start1 %= 3
        
    rs.append( ( sum0 , sum1 ) );
    start0 = 1;
    sum0 = 0;
    sum1 = 0
    start1 = 1
    for j in range( len( lst ) ):
        sum0 += lst[ j ][ start0 % 3 ];
        sum1 += lst[ j ][ start1 ]
        start0 += 1;
        start1 -= 1;
        start1 %= 3
    
    rs.append( ( sum0 , sum1 ) );
    
    
    start0 = 2;
    sum0 = 0;
    sum1 = 0
    start1 = 2
    for j in range( len( lst ) ):
        sum0 += lst[ j ][ start0 % 3 ];
        sum1 += lst[ j ][ start1 ]
        start0 += 1;
        start1 -= 1;
        start1 %= 3
    
    rs.append( ( sum0 , sum1 ) );
    
    
    print( rs ) ;
    
    
def main():
    N = int( input() );
    lst = [];
    for _ in range( N ):
        lst.append( list( map( int, input().split() ) ) )
    
    if( N == 1 ):
        print( min( lst[ 0 ] ) )
        return;
    dp = [ [ 0 ] * 3 for _ in range( N ) ]
    
    for i in range( 3 ):
        dp[ 0 ][ i ] = lst[ 0 ][ i ];
    
    for i in range( 1, N  ):
        for j in range( 3 ):
            bias1, bias2 = ( j + 1 ) % 3 , ( j - 1 ) % 3;
            dp[ i ][ j ] = min( dp[ i - 1 ][ bias1 ], dp[ i - 1 ][ bias2 ] ) + lst[ i ][ j ];
    print( min( dp[ N - 1 ] ) );
    
        
        
        
        


if( __name__ == "__main__" ):
    main()