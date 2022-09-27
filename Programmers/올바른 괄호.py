# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:35:54 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(s):
    answer = True
    
    
    if( s[ 0 ] == ")" ):
        return False;
    
    stack = [ s[0] ]
    idx = 1;
    while idx < len( s ) :
        if( s[ idx ] == '(' ):
            stack.append( s[ idx ] )
        else:
            if( not( len( stack ) ) or stack[ -1 ] != '(' ):
                return False;
            tg = stack.pop();
        idx += 1

    return False if stack or idx != len( s ) else True