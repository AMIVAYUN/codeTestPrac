# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:03:36 2022
@FileName: 15649.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/15649
"""


N, M = map( int, input().split() );


import itertools;

lst = [ i for i in range( 1, N + 1 ) ];

perm = itertools.permutations( lst , M );

for i in perm:
    for j in i:
        print( j , end = " " );
    print( );