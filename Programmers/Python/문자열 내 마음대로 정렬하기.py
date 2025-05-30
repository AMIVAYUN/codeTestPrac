# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:38:58 2022
@FileName: .py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/12915
"""


def solution(strings, n):
    answer = sorted( strings, key = lambda x: ( x[ n ], x ) )
    
    return answer