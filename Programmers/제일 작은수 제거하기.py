# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:07:12 2022
@FileName: 제일 작은수 제거하기 .py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12935
"""


def solution(arr):
    if len( arr ) <= 1: return [ -1 ];
    lit = min( arr );
    return [ i for i in arr if i != lit ];