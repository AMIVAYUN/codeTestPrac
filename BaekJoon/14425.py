# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:25:00 2022
@FileName: 14425.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/14425
"""


N, M = map( int, input().split() );
from collections import defaultdict;

ddit = defaultdict( int );

for i in range( N ):
    str0 = input();
    ddit[ str0 ] += 1
    
cnt = 0;
for i in range( M ):
    str1 = input();
    cnt += ddit[ str1 ];
    

print( cnt );

    