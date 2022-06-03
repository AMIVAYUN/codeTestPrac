# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:58:09 2022
@FileName: 완주하지 못한 선수.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/42576
"""


def solution(participant, completion):
    dit = dict.fromkeys( participant, 0 );
    for i in participant:
        dit[ i ] +=1;
        
    for j in completion:
        dit[ j ] -= 1;
        
    for i in participant:
        if( dit[ i ] ):
            return i;