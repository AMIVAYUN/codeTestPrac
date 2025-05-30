# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:35:51 2022
@FileName: 하샤드.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12947
"""


def solution(x):
   
    return not( x % sum( [ int( i ) for i in str( x ) ] ) )