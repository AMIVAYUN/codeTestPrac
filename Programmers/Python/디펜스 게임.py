# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:12:11 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n, k, enemy):
    '''
    병사 n명 enemy[ i ]마리 적이 등장 > 이만 큼 소모
    무적권 사용하면 한라운드 소모x
    
    ''' 
    Mx = len( enemy );
    lt = k; rt = Mx;
    answer = min( k , Mx );
    while lt <= rt:
        mid = ( lt + rt ) // 2;
        
        temp = enemy[ :mid ];
        
        srt = list( sorted( temp, reverse = True ) );
        
        if( n >= sum( srt[k:] ) ):
            lt = mid + 1;
            answer = max( answer, mid );
        else:
            rt = mid - 1;
            
        
    
    return answer