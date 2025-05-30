# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:38:58 2022
@FileName: 핸드폰 번호 가리기 .py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12948
"""


def solution(phone_number):
    lenx = len( phone_number );
    answer = ( "*" * ( lenx - 4 ) ) + phone_number[ lenx -4 : ]
    return answer