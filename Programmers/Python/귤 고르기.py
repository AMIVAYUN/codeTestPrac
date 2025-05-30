# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:34:45 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(k, tangerine):
    answer = 0;
    '''
    서로 다른 종류의 수 최소화
    '''
    from collections import defaultdict;
    ddit = defaultdict( int );
    for cuul in tangerine:
        ddit[ cuul ] += 1;
    
    lst = ddit.items();
    
    lst = list( sorted( lst, key = lambda x: -x[ 1 ] ) );
    
    for cuul in lst:
        if( k <= 0 ):
            return answer;
        size, val = cuul
        k -= val;
        answer += 1;
        
    return answer