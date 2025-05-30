# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:31:39 2022
@FileName: 나누어 떨어지는 숫자 배열.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/12910
"""


def solution(arr, divisor):
    arr.sort();
    answer = [ i for i in arr if i % divisor == 0 ]
    return answer if len( answer ) else [ -1 ]