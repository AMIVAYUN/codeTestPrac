# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 13:14:24 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(citations):
    answer = 0;
    hidx = list( sorted( citations ) )
    leng = len( citations )
    import bisect;
    for h in range( hidx[ -1 ], -1, -1 ):
       
        if( leng - bisect.bisect_left( hidx, h ) >= h ):
            return h;