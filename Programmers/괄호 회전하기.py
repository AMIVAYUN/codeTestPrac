# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def chkBystack( s ):
    stack = [ s[ 0 ] ] ;
    dit = { ")": "(" ,"}":"{","]": "[" };
    for i in range( 1, len( s ) ):
        if( stack and s[ i ] in dit and stack[ -1 ] == dit[ s[ i ] ] ):
            stack.pop();
        else:
            stack.append( s[ i ] );
    
    return len( stack ) == 0;
    
        
def solution(s):
    from collections import deque;
    dq = deque( s );
    answer = int( chkBystack( dq ) );
    
    for i in range( len( s ) - 1 ):
        val = dq.popleft();
        dq.append( val );
        answer += int( chkBystack( dq ) );

    
    
    
    return answer