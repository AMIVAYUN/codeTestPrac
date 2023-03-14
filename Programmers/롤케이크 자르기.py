# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:24:51 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(topping):
    from collections import deque;
    answer = 0;
    ditA = dict();
    
    ditB = dict();
    
    A = [ topping[ 0 ] ]; B = deque( topping[ 1: ] );
    
    ditA[ topping[ 0 ] ] = 1;
    
    for i in B:
        if( i not in ditB ):
            ditB[ i ] = 1;
        else:
            
            ditB[ i ] += 1;  
            
    answer = int( len( ditA ) == len( ditB ) );
    
    for i in range( len( B ) ):
        val = B.popleft();
        ditB[ val ] -= 1;
        
        if( ditB[ val ] == 0 ):
            ditB.pop( val );
        
        if( val not in ditA ):
            ditA[ val ] = 1;
        else:
            ditA[ val ] += 1;
        
        
        answer += len( ditA ) == len( ditB );
    
    return answer;
    
'''
def solution(topping):
    #SOL1 TIMEOUT
    A = [ topping[ 0 ] ]; B = topping[ 1: ];
    answer = len( set( A ) ) == len( set( B ) );
    for i in range( len( B ) ):
        A.append( B.pop( 0 ) );
        answer += len( set( A ) ) == len( set( B ) );

    return answer
    
    
'''
'''
#TIMEOUT SOL2;
def solution(topping):
    
    answer = 0;
    lent = len( topping )
    for i in range( 1, lent ):
        answer += len( set( topping[ i: ] ) ) == len( set( topping[ :i ] ) );
    
    return answer;
    
'''