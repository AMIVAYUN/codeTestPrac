# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:08:23 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


# Memorize 
T = int ( input() );

for i in range( T ):
    
    leng = int ( input() );
    
    
    lst = list( map( int, input().split() ) )
    

    prefix_sum = { -1: 0 }
    for i in range( leng ):
        prefix_sum[ i ] = prefix_sum[ i - 1 ] + lst[ i ];
        
    dp = [ [ 0 ] * leng for _ in range( leng )  ];
    '''
    bias 2 > 1
    for idx in range( leng ):
        dp[ idx ][ idx ] = lst[ idx ];
    
    for idx in range( leng - 1 ):
        dp[ idx ][ idx + 1 ] = lst[ idx ] + lst[ idx + 1 ];
    '''
 
    for bias in range( 1, leng ):
        for x in range( leng - bias ):
            
            y = x + bias;
        
        
            '''
            for bias2 in range( 1, bias ):
                print( "internal: ", "bias2: ", bias2 , (x, y ))
                print( "좌표:", ( x, x + bias2 - 1 ), ( x + bias2, y ))
                print( dp[ x ][ x + bias2 - 1] , dp[ x+ bias2 ][ y ] )
            dp[ x ][ y ] = min( [ dp[ x ][ x + bias2 - 1 ] + dp[ x + bias2 ][ y ] for bias2 in range( bias + 1 ) ] ) + ( prefix_sum[ y ] - prefix_sum[ x - 1 ] if( x > 0 ) else prefix_sum[ y ] );
            '''
            result = float('inf')
            for cut in range(x, y):
                #print( x, y, cut )
                #print( ( dp[x][cut] + dp[cut+1][y] + ( prefix_sum[y] - prefix_sum[x-1] if x > 0 else prefix_sum[ y ] ) ) )
                result = min(result, ( dp[x][cut] + dp[cut+1][y] + ( prefix_sum[y] - prefix_sum[x-1] ) ) )

            
            dp[ x ][ y ] = result 
        
    '''
    for row in dp:
        print( row )
    '''
    
    print( dp[ 0 ][ -1 ] )