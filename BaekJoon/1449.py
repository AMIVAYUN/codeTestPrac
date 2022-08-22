# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 13:37:58 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N, L = map( int, input().split() );

num = list( map( int, input().split() ) );

num = list( sorted( num ) );

start = num[ 0 ];
tape = 1;
context = 0;


for i in range( 1, N ):
    
    length = num[ i ] - num[ i - 1 ];
    if( length > L ):
        tape += 1;
        context = 0;
        continue;
    context += length;
    if( context >= L ):
        context = 0;
        tape += 1;

print( tape )