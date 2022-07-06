# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:56:47 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(progresses, speeds):
    stack = list( reversed( progresses ) );
    sp = list( reversed( speeds ) );
    answer = []
    cond = False;
    while stack:
        cnt = 0;
        while stack[ -1 ] > 99:
            stack.pop();
            sp.pop();
            cnt += 1;
            cond = True
        if( cond ):
            cond = False;
            answer.append( cnt );
        
        if( stack ):
            stack = [ stack[ i ] + sp[ i ] for i in range( len( stack ) ) ];
        
        
    
    
    return answer


solution([93, 30, 55],[1, 30, 5])