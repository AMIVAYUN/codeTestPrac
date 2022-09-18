# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:33:50 2022
@FileName: 10819.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/10819
"""
def getDiff( N, lst ):
    sum_ = 0;
    for i in range( N - 1 ):
        sum_ += abs( lst[ i ] - lst[ i + 1 ] )
    return sum_
N = int( input() );


lst = list( map( int, input().split() ) );

import itertools;


perm = list( itertools.permutations( lst, N ) );
Mx = 0;
for case in perm:
    Mx = max( Mx, getDiff( N , case ) )



print( Mx )