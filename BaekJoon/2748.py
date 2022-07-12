# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:26:42 2022
@FileName: 2748.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2748
"""


n = int( input() );

fibo = [ 0, 1 ] + [ 0 ] * 89;

for i in range( 2, n + 1 ):
    fibo[ i ] = fibo[ i - 1 ] + fibo[ i - 2 ];
    
print( fibo[ n ] )