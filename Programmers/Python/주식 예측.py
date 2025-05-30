# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:43:05 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(prices):
    from collections import defaultdict;
    answer = [ 0 ] * len( prices );
    stack = [ 0 ];
    leng = len( prices )
    for idx in range( 1,leng ):
        if( prices[ stack[ -1 ] ] <= prices[ idx ] ):
            stack.append( idx );
        
        else:
            while stack and prices[ stack[ -1 ] ] > prices[ idx ]:
                i = stack.pop();

                answer[ i ] = ( idx - i )
                
            stack.append( idx );
    
   
    while stack:
        i = stack.pop()
        answer[ i ] = leng - i -1;
        
    return answer