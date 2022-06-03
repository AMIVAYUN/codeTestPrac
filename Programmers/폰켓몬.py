# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:33:44 2022
@FileName: 폰켓몬.py
@author: YUNJUSEOK
@Link : https://programmers.co.kr/learn/courses/30/lessons/1845
"""


def solution(nums):
    dit = {};
    for i in nums:
        if( dit.__contains__( i ) ):
            dit[i] += 1;
        else:
            dit[ i ] = 1;
    lenx = len( dit );
    answer = lenx if lenx < len( nums )//2 else len(nums)//2
    return answer

