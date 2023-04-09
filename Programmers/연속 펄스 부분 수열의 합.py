# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 23:05:23 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



#SOL2 ON^2 TIMEOUT
def solution(sequence):
    answer = 0;
    leng = len( sequence );
    Mx = 0; Mn = float( 'inf' );
    
    new_sequence = [ sequence[i] * -1 if i % 2 == 0 else sequence[ i ] for i in range( leng )   ]
    from collections import defaultdict;
    prefix_sum = defaultdict( int );
    
    prefix_sum[ -1 ] = 0;
    answer = 0;
    for i in range( leng ):
        prefix_sum[ i ] = prefix_sum[ i - 1 ] + new_sequence[ i ];
        answer = max( answer, prefix_sum[ i ] );
        Mx = max( Mx, prefix_sum[ i ] );
        Mn = min( Mn, prefix_sum[ i ] );
    

    return max( Mx- Mn , answer)
    
    
    '''
    #SOL1 실패 TIME OUT
    answer = 0;
    leng = len( sequence );
    Mx = 0;
    new_sequence = [ sequence[i] * -1 if i % 2 == 0 else sequence[ i ] for i in range( leng )   ]
    
    dp = [ [ 0 ] * leng for _ in range( leng ) ];
    
    for i in range( leng ):
        dp[ i ][ i ] = new_sequence[ i ];
    
    for x in range( leng ):
        for bias in range( x, leng - x ):
            y = x + bias;
            dp[ x ][ y ] = dp[ x ][ y - 1 ] + dp[ y ][ y ];
            Mx = max( Mx, abs( dp [ x ][ y ] ) )
    '''
    return Mx