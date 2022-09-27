# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:24:57 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def binaryInjection( s ):
    cnt = 0;
    leng = len( s )
    for i in s:
        if( i == '1' ):
            cnt += 1;
    
    return cnt;
        
def solution(s):
    answer = [];
    cnt0 = 0;
    cnt_time = 0;
    while s != '1':
        cnt = binaryInjection( s );
        cnt0 += len( s ) - cnt;
        s = bin( cnt )[2:]
        cnt_time += 1;
    
    return [ cnt_time, cnt0 ]