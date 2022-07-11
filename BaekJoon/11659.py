# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:49:20 2022

@author: 주석
"""

N, M = map( int, input().split() );

sum0 = 0;
lst = [ 0 ];
for i in map( int, input().split() ):
    sum0 += i;
    lst.append( sum0 );


for i in range( M ):
    a, b = map( int, input().split() );
    
    print( lst[ b ] - lst[ a - 1 ] )