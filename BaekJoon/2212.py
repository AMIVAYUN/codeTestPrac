# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:41:30 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


n = int( input() );

k = int( input() );

lst = list( sorted( map( int, input().split() ) ) );

diff = [];

for i in range( n - 1 ):
    diff.append( lst[ i + 1 ] - lst[ i ] );
    
diff = list( sorted( diff ) );

print( sum( diff[ :n - k ] ) )