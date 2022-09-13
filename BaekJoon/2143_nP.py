# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:27:49 2022
@FileName: 2143.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2143
"""


T = int( input() );


from collections import defaultdict;
import itertools;


ddit = defaultdict( list );

NA = int( input() );

A = list( map( int, input().split() ) );

NB = int( input() );

B = list( map( int, input().split() ) );

ans = 0;

for i in range( 1, NA + 1 ):
    cmb = itertools.combinations( A, i );
    
    for case in cmb:
        if( sum( case ) >= T ):
            continue;
        ddit[ sum( case )].append( case );
    
    

for j in range( 1, NB + 1 ):
    
    cmbb = itertools.combinations( B, j );
    
    for case in cmbb:
        print( sum( case ), case  )
        if( sum( case ) >= T ):
            continue;
        ans += len( ddit[ T - sum( case ) ] );
    

print( ans )

print( ddit )