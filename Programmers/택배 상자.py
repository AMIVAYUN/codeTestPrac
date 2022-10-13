# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:53:32 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution( order ):
    from collections import deque;
    answer = 0;
    nums = deque( [ i for i in range( 1, len( order ) + 1 ) ] );
    dq = deque( order );
    stack = [];
    
    while nums:
        num = nums.popleft();
        
        if( dq[ 0 ] != num ):
            while nums and dq[ 0 ] != num:
                stack.append( num );
                num = nums.popleft();
            
            if( num == dq[ 0 ] ):
                
                dq.popleft();
                answer += 1;
            
        else:
            answer += 1;
            dq.popleft();
    
        while stack and dq and stack[ -1 ] == dq[ 0 ]:
            stack.pop();
            dq.popleft()
            answer += 1;

    
    return answer;
    
#sol1
'''
def solution(order):
    from collections import deque;
    answer = 0
    stack = [];
    idx = 1;
    dq = deque( order );
    while dq and idx < len( order ) + 1:
        turn = dq.popleft()
        if( idx != turn ):
            while idx != turn and idx < len( order ) + 1:
                stack.append( idx );
                idx += 1;
        
        if( idx < len( order ) + 1 and idx == turn ):
            answer += 1;
        
        while stack and dq:
            val = stack.pop();
            tg = dq.popleft();
            if( val != tg ):
                return answer;
            answer += 1;
    
    return answer;
            
        
                
        
'''
