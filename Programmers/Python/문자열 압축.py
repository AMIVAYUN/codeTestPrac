# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 17:41:46 2022
@FileName: 문자열 압축.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/60057
"""
s = "abcabcabcabcdededededede"
answer = 0

def zip1( s, n ):
    
    lst = [ s[ i : i + n ] for i in range( 0, len( s ), n ) ];
    idx = 0;
    cnt = 1;
    result = "";
   
    
    while( idx < len( lst ) ):
        while( idx != len( lst ) -1 and lst[ idx ] == lst[ idx + 1 ] ):
            cnt += 1;
            idx += 1;
            
        if( cnt > 1 ):
            result += str( cnt ) + lst[ idx ];
            cnt = 1;
            idx += 1;
        else:
            result += lst[ idx ]
            idx += 1;
            
        
        
    
    return result;


def solution(s):
    answer = len( s );
    for i in range( 1, len( s ) ):
        answer = min( answer, len( zip1( s, i ) ) );
    return answer