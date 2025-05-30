# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:25:01 2022
@FileName: 같은 숫자는 싫어 .py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/12906
"""


def solution(arr):
    answer = [ arr[0] ];
    recent = 0;
    for i in range( 1, len( arr ) ):
        if( arr[ i ] != answer[ recent ] ):
            answer.append( arr[ i ] );
            recent +=1;
    return answer