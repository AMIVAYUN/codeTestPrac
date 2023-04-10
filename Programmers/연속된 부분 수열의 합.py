# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:00:50 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(sequence, k):
    from collections import defaultdict;
    
    
    ddit = defaultdict( int );
    ddit[ -1 ] = 0;
    leng = len( sequence );
    answer = [ 0, leng + 1 ];
    for i in range( leng ):
        ddit[ i ] = sequence[ i ] + ddit[ i - 1 ];
        if( sequence[ i ] == k ):
            return [ i, i ]
        

    for i in range( -1, leng ):
        lt = i + 1; rt = leng - 1;
        stan = ddit[ i ];
        while lt <= rt: #and ( ( lt + rt ) // 2 ) - i <= answer[ 1 ] - answer[ 0 ]:
            mid = ( lt + rt ) // 2;
            
            if( ddit[ mid ] - stan == k ):
                answer = [ i + 1, mid ] if mid - ( i + 1 ) < answer[ 1 ] - answer[ 0 ] else answer;
                
            if( ddit[ mid ] - stan <= k ):
                lt = mid + 1;
            else:
                rt = mid - 1;
                
        
    
    return answer