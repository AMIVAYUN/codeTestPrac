# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 20:02:28 2022
@FileName: 2812.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2812
"""


#2812

N, K = map( int, input().split() ) ;

num = input() ;


idx = 1;

stack = [ num[ 0 ] ];

for i in range( 1, N ):
    while stack and K > 0 and num[ i ] > stack[ - 1 ]:
        stack.pop();
        K -= 1;
    stack.append( num[ i ] );

if( K > 0 ):
    print( ''.join( i for i in stack[ : len( stack ) - K ] ) )
else:
    print( ''.join( i for i in stack ) );
    
    