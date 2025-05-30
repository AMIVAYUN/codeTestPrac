# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:39:18 2022
@FileName: 행렬의 덧셈.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12950
"""

def solution(arr1, arr2):
    answer = [ [arr1[ i ][ j ] + arr2[ i ][ j ] for j in range( len( arr1[0]))] for i in range( len( arr1 ) ) ]
    return answer