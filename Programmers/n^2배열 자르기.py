# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:35:57 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n, left, right):

    answer = []
    
    idx = left;
    
    for i in range( left, right + 1 ):
        div, mod = divmod( i, n );
        if( div > mod ):
            answer.append( div + 1 );
        else:
            answer.append( mod + 1 );
    
    '''
    while idx < right + 1:
        div, mod = divmod( idx, n );
        
        if( mod < div ):
            cnt = div + 1;
            
            while cnt > 0 and idx < right + 1:
                idx += 1;
                cnt -= 1;
                answer.append( div + 1 );
            --   
                
            while mod < div and idx < right + 1:
                answer.append( div + 1 );
                mod += 1;
                idx += 1;
            --  
        else:
            answer.append( mod + 1 )
            idx += 1;
        '''
        
    return answer