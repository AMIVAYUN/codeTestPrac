# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:54:27 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


#1 Timeout
def getstr0( str0 ):
    proc = [];
    case = '110';
    Mn = str0;
    leng = len( str0 )
    for i in range( 0, leng - 2 ):

        if( str0[ i : i + 3 ] == case ):
            proc.append( i );

    for idx in proc:
        temp = str0[ :idx ] + str0[ idx + 3: ];
        temp = getstr0( temp );
        for i in range( len( temp ) + 1 ):
            temp2 = temp[ :i ] + case + temp[ i: ]
            Mn = min( Mn, temp2 );
    
        
    return  Mn;
#2

def getStr0_2( str0 ):
    stack = [];
    cnt = 0;
    for i in range( len( str0 ) ):
        if( str0[ i ] == '0' and ''.join( stack[ -2: ] ) == '11' ):
            for i in range( 2 ):
                stack.pop()
            cnt += 1;
            continue;
        stack.append( str0[ i ] );      

    if( cnt == 0 ):
        return str0 
    leng = len( stack );
    
    idx = leng - 1;
    while idx != -1:
        if( stack[ idx ] == '0' ):
            break;
            
        idx -= 1;
    
    forward = ''.join( stack[ :idx + 1 ] );
    tail = ''.join( stack[ idx + 1 : ] );
    
    return forward + ( '110' * cnt ) + tail;

def solution(s):
    answer = []
    

    for str0 in s :
        answer.append( getStr0_2( str0 ) );
        
    return answer