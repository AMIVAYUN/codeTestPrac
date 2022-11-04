# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:49:07 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N, K = map( int, input().split() );

lst = list( map( int, input().split() ) );

ans = [ 0, lst[ 0 ] ];


for i in range( 1, N ):
    ans.append( ans[ -1 ] + lst[ i ] );
    

for i in range( K ):
    a, b = map( int, input().split() );
    m = b - a + 1;
    print( a,b, ans, m )
    print( round( ( ans[ b ] - ans[ a - 1 ] ) / m, 2) )