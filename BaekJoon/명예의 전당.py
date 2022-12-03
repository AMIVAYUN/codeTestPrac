# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:55:50 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(k, score):
    answer = [ score[ 0 ] ];
    stack = [ score[ 0 ] ];
    import bisect;
    for i in range( 1, len( score ) ):
        bisect.insort( stack, score[ i ] );
        stack = stack[ -k: ];
        answer.append( stack[ 0 ] );
    
    
    return answer