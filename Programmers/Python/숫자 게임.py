# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:47:28 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(A, B):
    from collections import deque;
    A = deque( ( sorted( A ) ) );
    answer = 0
    B = list( sorted( B ) );
    
    Adx = 0;
    Bdx = 0;
    lengB = len( B );
    while Bdx < lengB:
        if( A[ 0 ] < B[ Bdx ] ):
            answer += 1;
            A.popleft();
            Bdx += 1;
        
        else:
            Bdx += 1;
    
    
    return answer