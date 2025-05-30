# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:51:03 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(x, y, n):
    answer = 0;
    
    dp = [ 10000001 ] * 10000001;
    dp[ x ] = 0;
    for i in range( x, y + 1 ):
        dp[ i * 3 ] = min( dp[ i ] + 1, dp[ i * 3 ] );
        dp[ i * 2 ] = min( dp[ i ] + 1, dp [ i * 2 ] );
        dp[ i + n ] = min( dp[ i ] + 1, dp[ i + n ] );
        
    return dp[ y ] if dp[ y ] != 10000001 else -1;
'''
#8 WA
def solution(x, y, n):
    answer = float( 'inf' );
    from collections import deque;
    

    dq = deque();
    
    dq.append( ( y, 0 ) );
    
    while dq:
        now, cnt = dq.popleft();
        
        if( cnt > answer ):
            continue;
        
        if( now == x ):
            answer = min( cnt, answer );
            continue;
        
        if( now % 3 == 0 and now // 3 >= x ):
            dq.append( ( now//3 , cnt + 1 ) );
        
        if( now % 2 == 0 and now // 2 >= x ):
            dq.append( ( now // 2 , cnt + 1 ) );
            
        if( now - n > 1 and now - n >= x ):
            dq.append( ( now - n , cnt + 1 ) );
        

    
    return answer if answer != float( 'inf' ) else -1
    
'''