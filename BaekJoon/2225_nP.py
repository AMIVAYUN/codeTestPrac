# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:11:45 2022
@FileName: 2225.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2225
"""





def f1():
    N, K = map( int, input().split() );


    dp = [ 0 ] * ( 40001 );
    
    
    for i in range( 1, N + 1 ):
        dp[ i ] += 1;
        for j in range( i, i + K ):
            dp[ j ] += dp[ j - i ] + 1;
            
        print( dp[ :N + 1] );
        





def f2():
    N, K = map( int, input().split() );
    
    dp = [ 1 ] * ( 40001 );
    
    rs = [ 0 ] * ( 40001 );
    
    
    for i in range( 2, N + 1 ):
        dp[ i ] += 1;
        temp = dp [:]
        for j in range( i + 1, N + 1 ):
            dp[ j ] = dp[ j - 1 ] + dp[ j - 2 ];
            
                
        
    temp = dp[:]
    for i in range( K + 1, N + 1 ):
        dp[ i ] = ( i - K ) * ( sum( temp[ : i - K + 1 ] ) )
        
        
            
            
    
        
    
    print( dp[ : N + 1 ] )
    
if( __name__ == "__main__" ):
    f2();    