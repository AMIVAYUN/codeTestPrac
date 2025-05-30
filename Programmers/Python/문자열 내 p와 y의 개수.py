# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:43:19 2022
@FileName: 문자열내 p와 y의 개수.py
@author: YUNJUSEOK
@Link : https://programmers.co.kr/learn/courses/30/lessons/12916
"""

def solution(s):
    dit = { 'P' : 1, 'Y' : -1 }
    answer = [ dit[ i ] for i in s.upper() if i == 'P' or i == 'Y'] 

    return True if not( sum( answer ) ) else False;