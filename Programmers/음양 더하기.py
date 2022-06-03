# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 12:55:09 2022
@FileName: 음양 더하기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/76501
"""


def solution(absolutes, signs):
    answer = [ absolutes[i] if signs[i] else absolutes[i] *-1 for i in range( len( absolutes ) ) ] 
    
    
    return sum( answer )