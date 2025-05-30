# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:46:21 2022
@FileName: 문자열 내림차순으로 배치하기.py
@author: YUNJUSEOK
@lINK: https://programmers.co.kr/learn/courses/30/lessons/12917
"""


def solution(s):
    lst = list( s );
    lst.sort( reverse = True );
    return ''.join( i for i in lst )