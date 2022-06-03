# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:56:11 2022
@FileName: 자릿수 더하기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12931
"""


def solution(n):
    

    return sum( [ int( i ) for i in str( n ) ] )