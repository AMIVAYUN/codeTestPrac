# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:22:27 2022
@FileName: 문자열을 정수로 바꾸기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12925
"""


def solution(s):
    dit = { "+": 1 , "-": -1 }
    return dit[ s[ 0 ] ] * int( s[ 1: ] ) if dit.__contains__( s[ 0 ] ) else int( s )