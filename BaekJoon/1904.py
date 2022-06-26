# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 13:16:54 2022
@FileName: 1904.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1904
"""


N = int( input() );


lst = [ 0 ] * 1000001
lst[ 0 ], lst[ 1 ] = 1, 2 ;
for i in range( 2, N ):
    lst[ i ] = ( lst[ i - 1 ] + lst[ i - 2 ] ) % 15746;
    
    
print( lst[ N - 1 ] )


