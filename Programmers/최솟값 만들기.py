# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:27:07 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(A,B):
    answer = 0
    
    A = list( sorted( A ) );
    B = list( sorted( B , reverse = True ) );
    
    
    return sum( [ A[ i ] * B[ i ] for i in range( len( A ) ) ])