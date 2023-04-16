# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 21:09:20 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def ran( pos1, pos2 ):
    if( pos2[ 0 ] - pos1[ 1 ] >= 0):
        return True, pos2;
    else:
        return False, [ max( pos2[ 0 ], pos1[ 1 ] ), min( pos1[ 1 ], pos2[ 1 ] ) ];
def solution(targets):
    answer = 0;
    '''
    미사일 최소로
    
    
    A, B 싸우는 2차원 공간
    
    A x 축 펴행
    
    B나라 y축 평행 발사
    
    
    '''
    
    targets = list( sorted( targets, key = lambda x: ( x[ 0 ], x[ 1 ] ) ) )
    
    
    from collections import defaultdict;
    
    answer = 1;
    
    now = targets[ 0 ];


    for target in targets[ 1: ]:
        rs = ran( now, target );
        
        answer += int( rs[ 0 ] );
        
        now = rs[ 1 ];
        
        
    return answer;
    