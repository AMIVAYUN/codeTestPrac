# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:12:36 2022
@FileName: 15650.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/15650
"""


N, M = map( int, input().split() );


import itertools;

lst = [ i for i in range( 1, N + 1 ) ];

cmb = itertools.combinations( lst , M );

for i in cmb:
    for j in i:
        print( j, end = " " );
    print();