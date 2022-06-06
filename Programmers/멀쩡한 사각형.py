# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:27:28 2022
@FileName: 멀쩡한 사각형.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/62048
"""


import sys;
sys.setrecursionlimit( int( 1e6 ) )
def gcd( a, b ):
    if( a == 1 or b == 1 ):
        return 1
    if( a == b ):
        return a;
    if( a > b ):
        return gcd( a - b, b );
    if( a < b ):
        return gcd( b , a );

def solution( w,h ):
    V = gcd( w, h );
    if( V != 1 ):
        w1 = w//V; h1 = h//V;
        c = w1 + h1 - 1;
        return ( w * h ) - ( c * V );
    else:
        return ( w * h ) - ( w + h - 1)