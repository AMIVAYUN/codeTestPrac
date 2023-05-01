# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:06:15 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


T = int( input() );


lengA = int( input() );

A = list( map( int, input().split() ) );

lengB = int( input() );

B = list( map( int, input().split() ) ) ;

all_A = { -1: 0 };

for idx in range( lengA ):
    all_A[ idx ] = all_A[ idx - 1 ] + A[ idx ];

from collections import defaultdict;

ddit = defaultdict( int );

for x in range( lengA ):
    for y in range( x + 1 , lengA + 1 ):

        ddit[ sum( A[ x : y ] ) ] += 1;
        
answer = 0;


print( ddit );
for x in range( lengB ):
    
    for y in range( x + 1, lengB + 1 ):
        
        answer += ddit[ T - sum( B[ x: y ] ) ]

print( answer );