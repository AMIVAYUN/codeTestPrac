# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 16:18:17 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
Timeout
def solution(begin, end):
    
    answer = [ 0 ] * ( end + 1 );
    
    for i in range( begin, end + 1 ):
        for case in range( 2, i + 1 ):
            if( i % case == 0 ):
                answer[ i ] = i//case;
                break;
        
    return answer[ begin: end + 1 ]
'''

def isPrime( n ):
    if( n == 1 ):
        return False;
    
    for i in range( 2, int( n ** 0.5 ) + 1 ):
        if( n % i == 0 ):
            return False;
    
    return True;

def solution(begin, end):
    answer = []


    
    for i in range( begin, end + 1 ):
        if( i == 1 ):
            answer.append( 0 );
            continue;
        for idx in range( 2, int( i ** 0.5 ) + 1):
            div = i // idx;
            if( div > 10 ** 7 ):
                continue;
            if( i % idx == 0 ):
                answer.append( div )
                break;
        else:
            answer.append( 1 );
                
    
    return answer
            
            
            
    
    
    
    return answer;