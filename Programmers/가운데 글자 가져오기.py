# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:53:53 2022
@FileName: 가운데 글자 가져오기.py
@author: YUNJUSEOK
@Link : https://programmers.co.kr/learn/courses/30/lessons/12903
"""


def solution(s):
    return s[ len(s)//2 ] if len(s)%2 else s[ len(s)//2 - 1:len(s)//2 + 1  ]