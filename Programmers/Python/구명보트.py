# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:41:45 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
보트 최대 2명 무게제한 O

'''
def solution(people, limit):
    from collections import deque;
    people = list( sorted( people ) );
    
    dq = deque( people );
    answer = 0
    
    
    while dq:
        
  
        if( len( dq ) >= 2 and dq[ 0 ] + dq[ -1 ] > limit ):
            dq.pop()
            answer += 1;
        elif(len( dq ) >= 2 and dq[ 0 ] + dq[ -1 ] <= limit ):
            dq.popleft()
            dq.pop()
            answer += 1
        else:
            dq.pop()
            answer += 1
    return answer