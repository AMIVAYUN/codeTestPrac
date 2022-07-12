# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:14:19 2022
@FileName: 2156.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2156
"""


n = int( input() );

lst = [ 0 ] * 10001
dp = [ 0 ] * 10001;
for i in range( 1, n + 1 ):
    lst[ i ] = int( input() );
    

for i in range( 1, n + 1 ):
    dp[ i ] = max( dp[ i - 2 ]  + lst [ i ],dp[ i - 3 ] + lst[ i - 1 ]  + lst [ i ], dp[ i - 1 ])
    
print( dp )
    