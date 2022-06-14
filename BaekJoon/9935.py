# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 16:12:02 2022
@FileName: 9935.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/9935
"""


s = input();

c4 = input();

lenx = len( c4 )

if( lenx == 1 ):
    stack = [];
    for i in range( 0, len( s) ):
        if( s[ i ] == c4 ):
            continue;
        stack.append( s[ i ] );
    
    
else:
    stack = list( s[ 0 :lenx -1 ] );
    for i in range( lenx - 1 , len( s ) ):
    
        if( len( stack ) >= lenx - 1  and "".join( stack[ -lenx + 1 : ] ) + s[ i ] == c4 ):
            for j in range( lenx - 1 ):
                stack.pop()
            continue;

        stack.append( s[ i ] )
    

print( "".join( i for i in stack ) ) if len( stack ) else print( "FRULA" );