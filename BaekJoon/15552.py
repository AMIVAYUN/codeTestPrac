# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 17:52:03 2022
@FileName: 15552.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/15552
"""


import sys;

N = int( sys.stdin.readline() );


for i in range( N ):
    a, b = map( int, sys.stdin.readline().split() );
    
    print( a + b )''