# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:07:41 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(s):
    answer = ''
    answer = sorted( list( map( int, s.split() ) ) )
    return str( answer[0] )+ " " + str( answer[-1] )