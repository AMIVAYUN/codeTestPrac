# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:44:11 2022
@FileName: 예산.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/12982
"""

def solution( d, budget ):
    d.sort();
    idx = 0;

    for i in range( len( d ) ):
        if( budget >= d[ idx ]):
            budget -= d[ idx ];
            idx += 1
        else:
            break;
            
    
        
    return idx;
