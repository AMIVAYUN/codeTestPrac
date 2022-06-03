# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 14:02:21 2022
@FileName: K번째 수.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/42748
"""


def solution(array, commands):
    
    
    answer = []
    
    for i in commands:
        tmp = array[ i[0] - 1: i[1] ]
        answer.append( sorted( tmp )[ i[ 2 ] - 1])
    
    
    return answer


