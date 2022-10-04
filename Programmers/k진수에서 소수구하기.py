# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:08:00 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def isPrime( num ):
    if( num == 1 ):
        return False;
    
    for i in range( 2, int(num ** 0.5) + 1 ):
        if( num % i == 0 ):
            return False;
    
    return True;
def solution(n, k):
    answer = 0;
    rs = [];
    while n != 0:
        div, mod = divmod( n, k );
        if( div ):
            rs.append( str( mod ) );
        else:
            rs.append( '0' );
        
        n = div;
        
        if( n < k ):
            rs.append( str( n ) );
            break;
    


    rs.reverse();
    
    rs = ''.join( rs ).split( '0' );
  
    print( rs )
    for num in rs:
        if( num == '' ):
            continue;
        if( isPrime( int( num ) ) ):
            answer += 1;
        
    
    
        
    return answer