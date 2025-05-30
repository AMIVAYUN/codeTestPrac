# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:10:22 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(brown, yellow):
    sum_ = brown + yellow;
    answer = [];
    for i in range( 2 , sum_ + 1 ):
        
        if( sum_ % i or i < int( sum_ ** 0.5 ) ):
            continue;
     
        a, b = i, sum_ // i
      
        if( ( a - 2 ) * ( b - 2 ) == yellow ):
            answer = list( sorted( [ a, b ], reverse = True ) );
            
    return answer
        