# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:47:10 2022
@FileName: x만큼 간격이 있는 n개 숫자.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12954
"""


def solution(x, n):
    if( x == 0 ):
        return [ 0 ] * n
    answer = [ i for i in range( abs( x ), abs( x*n) +1  , abs( x ) ) ]
    return answer if x > 0 else [ -i for i in answer ];