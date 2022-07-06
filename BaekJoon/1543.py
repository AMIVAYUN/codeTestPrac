# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:39:37 2022
@FileName: 1543.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1543
"""


s = input();

b = input();

cnt = 0;

while b in s:
    idx = s.index( b, 0, len( s ) );
    
    s = s[ idx + len( b ): ];
    
    cnt += 1;
    
print( cnt )
