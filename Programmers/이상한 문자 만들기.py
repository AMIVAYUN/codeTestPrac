# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:55:23 2022
@FileName: 이상한 문자 만들기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12930
"""


def solution(s):
    answer = ""
    lst = s.split( " " );
    for i in lst:
        for j in range( len( i ) ):
            if( j%2 ):
                answer += i[j].lower();
            else:
                answer += i[j].upper();
        answer += " ";
    return answer[:len(answer) - 1]