# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 15:12:23 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def change( num, k ):
    rs = ""
    while num > 0:
        num, rest = divmod( num, k );
        rs += str( rest );
    
    return rs[ ::-1 ];

def isPrime( n ):
    if( n <= 1 ):
        return False;
    for i in range( 2, int(n ** 0.5 + 1) ):
        if( n % i == 0 ):
            return False;
    
    return True;

def solution(n, k):
    answer = 0
    num = change( n, k );
    lenx = len( num )
    idx = 0;
    start = 0;
    while idx < lenx:
        str0 = ""
        while( idx < lenx and num[ idx ] != '0' ):
            str0 += num[ idx ]
            idx += 1;
        if( len( str0 ) ):
            num_ = int( str0 );
            if( isPrime( num_ ) ):
                answer += 1;
        
        
        idx += 1;

        
        
        
        
        
    
    
    
    return answer

solution( 437674, 3 )
    