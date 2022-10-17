# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:50:20 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n, s):
    answer = [];
    
    if( s < n ):
        return [-1];
    
    stand = s // n ;
    
    sum_ = stand * n;
    
    diff = s- sum_
    
    answer = [ stand ] * n;
    
    idx = 0;
    
    while diff > 0:
        answer[ idx ] += 1;
        diff -= 1;
        idx += 1;
    
    return sorted( answer )