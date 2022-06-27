# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 15:38:06 2022
@FileName: 12865.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/12865
"""
'''
10 15
1 1
2 3
5 3
5 1
4 5
3 3
3 2
4 4
4 4
4 3

// 정답
17
// 해설
1 1
2 3
4 5
4 4
4 4
// 현재 출력
22
'''
#answer 
def t1():
    N, K = map( int ,input().split() );


    dp = [ 0 ] * ( K + 1 ) ;


    wv = [];


    for i in range( N ):
        a, b = map( int, input().split() );
        wv.append( ( a, b ) );
        
        
    for i in range( len( wv ) ):
        temp = dp[:]
        for j in range( wv[ i ][ 0 ], K + 1 ):
            
            dp[ j ] = max( dp[ j ], temp[ j - wv[ i ][ 0 ] ] + wv[ i ][ 1 ] );
            
        
    
    print( dp[ K ] );   
    
t1()


    