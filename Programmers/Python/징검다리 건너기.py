# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:26:15 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(stones, k):
    '''
    징검다리가 있고 개울을 만나서 건너편으로 가려고함.
    
    징검다리 일렬로 놓여있음 한번 밟을 때마다 1씩 감소 0 이되면 더이상 못밟는다.
    
    점프를 뛰게 될시 가장 가까운 디딤돌로만 가능
    
    
    '''
    Mx = max( stones ) + 1;
    Mn = min( stones );
    answer = 0;
    sum_ = sum( stones );
    leng = len( stones );
    
    lt, rt = Mn, Mx;
    
    while lt <= rt:
        mid = ( lt + rt ) // 2 ;
        idx = 0;
        if( sum_ < mid ):
            lt = mid + 1;
        Mx_tmp = 0;
        while idx < leng:
            if( stones[ idx ] >= mid ):
                idx += 1;
            else:
                cnt = 1;
                idx += 1
                while( idx< leng and stones[ idx ] < mid ):
                    idx += 1;
                    cnt += 1;

                Mx_tmp = max( cnt, Mx_tmp );

    
        if( Mx_tmp < k ):
            lt = ( mid + 1 )
            answer = max( answer, mid );
        
        else:
            rt= mid - 1;
            
                
        
    return answer