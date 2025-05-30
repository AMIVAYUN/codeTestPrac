# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:10:36 2022
@FileName: 소수 찾기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12921
"""

def solution(n):
    lst = [];
    for i in range( 2, n + 1 ):
        if ( isPrime( i ) ):
            lst.append( i );
    return len( lst );
def isPrime( n ):
    
    for i in range( 2, int( n**0.5 )+ 1 ):
        if( n % i == 0 ):
            return False;
    
    return True;