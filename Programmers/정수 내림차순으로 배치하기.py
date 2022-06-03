# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:01:42 2022
@FileName: 정수 내림차순으로 배치하기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12933
"""


def solution(n):
    return int( ''.join( str( j ) for j in ( list( sorted( [ int( i ) for i in str( n ) ], key = lambda x: -x ) ) ) ) )