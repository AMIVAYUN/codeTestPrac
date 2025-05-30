# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:02:18 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



def solution( n ):
    answer = 0;
    ans = [];
    for i in range( 1, n + 1 ):
        sum_ = i;
        for j in range( i + 1, n + 1 ):
            if( sum_ >= n ):
                break;
            sum_ += j
        
        answer += int( sum_ == n )
    
    return answer
    