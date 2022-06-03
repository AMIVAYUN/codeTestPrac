# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 17:49:08 2022
@FileName: 문자열 다루기 기본.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/12918
"""

def solution(s):
    
    
    return ( len( s ) == 4 or len( s ) == 6 ) and not( False in [  ord ( i ) - 57 <= 0 for i in s ])