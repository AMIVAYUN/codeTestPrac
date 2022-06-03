# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:29:15 2022
@FileName: 3진법 뒤집기.py
@author: YUNJUSEOK
@lINK: https://programmers.co.kr/learn/courses/30/lessons/68935
"""

#1번
def solution( n ):
    lst = [];
    while ( True ):
        if( n < 3 ):
            lst.append( n );
            break;
        lst.append( n % 3 );
        n = int( n / 3 );
    
    sum0 = 0
    for i in range( len( lst ) - 1 , -1, -1 ):
        sum0 += ( 3 ** ( len( lst ) - 1 - i ) ) * lst[ i ]; 
        
    
    return sum0