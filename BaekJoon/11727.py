# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 18:42:57 2022
@FileName: 11727.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11727
"""

N = int( input() );


dp = [ 0 ] * 1000

dp[ 0 ] = 1

dp[ 1 ] = 3

for i in range( 2, N ):
    dp[ i ] = dp [ i - 1 ] + 2*( dp[ i - 2 ] )
    
    
print( dp[ N - 1 ])