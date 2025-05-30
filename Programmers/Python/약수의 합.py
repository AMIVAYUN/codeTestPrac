# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:50:38 2022
@FileName: 약수의 합.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12928
"""


def solution(n):
    return sum( [ i for i in range( 1, n + 1 ) if n % i == 0  ])