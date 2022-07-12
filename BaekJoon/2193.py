# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:54:33 2022
@FileName: 2193.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2193
"""


fibo = [ 1, 1 ] + [ 0 ] * 89;

n = int ( input() );


for i in range( 2, n + 1 ):
    fibo[ i ] = fibo[ i - 2 ] + fibo[ i - 1 ];
    
print( fibo[ n - 1 ])