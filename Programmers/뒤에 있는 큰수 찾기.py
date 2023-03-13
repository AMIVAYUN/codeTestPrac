# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:38:49 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(numbers):
    import heapq;
    lenN = len( numbers );
    answer = [ -1 ] * lenN;
    numbers = [ ( numbers[ i ], i ) for i in range( lenN ) ];
    stack = [ numbers[ 0 ] ];
    heapq.heapify( stack );
    
    
    for i in range( 1, lenN ):
        while stack and stack[ 0 ][ 0 ] < numbers[ i ][ 0 ]:
            val = heapq.heappop( stack );
            answer[ val[ 1 ] ] = numbers[ i ][ 0 ];
        
        heapq.heappush( stack, numbers[ i ] );
    
    
    
    return answer