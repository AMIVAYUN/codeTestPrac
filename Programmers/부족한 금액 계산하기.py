# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:49:35 2022
@FileName: 부족한 금액 계산하기.py
@author: YUNJUSEOK
@Link : https://programmers.co.kr/learn/courses/30/lessons/82612
"""

def solution(price, money, count):
    sum0 = 0;
    for i in range( 1, count + 1 ):
        sum0 += i;
    answer = money - ( price * sum0);

    return abs( answer ) if answer < 0 else 0


