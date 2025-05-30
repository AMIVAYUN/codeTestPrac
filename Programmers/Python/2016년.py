# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:35:36 2022
@FileName: 2016년.py
@author: YUNJUSEOK
@link: https://programmers.co.kr/learn/courses/30/lessons/12901
"""

def solution(a, b):
    import datetime;
    dt = datetime.date( 2016, a, b );
    lst = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    answer = lst[ dt.weekday() ];
    return answer

