# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:19:11 2022
@FileName: 10816.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/10816
"""


from collections import defaultdict;

ditt = defaultdict( int );

N = int( input() );

str0 = input().split();

for i in str0:
    ditt[ i ] += 1;


M = input();

str1 = input().split();

for i in str1:
    print( ditt[ i ], end = " " )