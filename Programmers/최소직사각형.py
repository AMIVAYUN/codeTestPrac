# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:40:06 2022
@FileName: 최소직사각형.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/86491
"""


def solution(sizes):
    for i in sizes:
        if( i[ 0 ] < i[ 1 ] ):
            i[ 0 ], i[ 1 ] = i[ 1 ], i[ 0 ];
    answer = max( [ i[0] for i in sizes ] ) * max( [ i[1] for i in sizes ] ); 
    return answer