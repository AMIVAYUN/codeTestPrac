# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:12:17 2022
@FileName: 두개 뽑아서 더하기.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/68644
"""


def solution(numbers):
    import itertools
    numslist = { sum( i ) for i in itertools.combinations( numbers, 2 ) };
    answer = list( numslist );
    answer.sort();
    return answer