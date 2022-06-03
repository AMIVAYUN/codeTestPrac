# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:12:53 2022
@FileName: 짝수와 홀수.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12937
"""


def solution(num):
    dit = {True: "Odd", False:"Even"}
    return dit[ num % 2 ];