# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:34:27 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n, words):
    from collections import defaultdict
    answer = [ 0, 0 ]
    ddit = defaultdict( int );
    idx = 0;
    context = words[ 0 ][ 0 ]
    while idx < len( words ):
        
        for i in range( 1, n + 1 ):
            if( len( words[ idx ] ) == 1 or context != words[ idx ][ 0 ] or ddit[ words[ idx ] ] ):
                answer = [ i, idx // n + 1  ]
                return answer;
            ddit [ words[ idx ] ] += 1
            context = words[ idx ][ -1 ];
            idx += 1;
        
        
        
        
    return answer