# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 15:04:29 2022
@FileName: 큰수 만들기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/42883
"""


# TimeOut
def solution( number, k ):
    import itertools;
    Mx = -1;
    number = list( number );
    lst = [ i for i in range( len( number ) ) ]
    cmb = list( itertools.combinations( lst , k ) );
    for i in range( len( cmb ) ):
        const = number[ : ];
        cmb[ i ] = sorted( cmb[ i ] ,reverse = True)
        
        for j in cmb[ i ]:
            
            const.pop( j );
        
        Mx = max( Mx, int( "".join( i for i in const ) ) );
    
    
    return str( Mx )

def solution( number, k ):
    stack = [];
    
    for i in list( number ):
        if( k == 0 ):
            stack.append( i );
            continue;
        while ( stack and stack[ -1 ] < i and k > 0 ):
            stack.pop();
            k -= 1;
        stack.append( i );
    #testcase 12번
    if( k > 0 ):
        return "".join( i for i in stack[:len( stack ) - k ])
    
    return "".join( i for i in stack );