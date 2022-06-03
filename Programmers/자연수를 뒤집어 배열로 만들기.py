# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:58:28 2022
@FileName: 자연수를 뒤집어 배열로 만들기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12932
"""


def solution(n):
    
    return list( reversed( [ int( i ) for i in str( n ) ] ) )