# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:49:41 2022
@FileName: 없는 숫자 더하기.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/86051
"""


def solution(numbers):
    answer = 45;
    for i in numbers:
        answer -= i ;
    return answer


int( True )