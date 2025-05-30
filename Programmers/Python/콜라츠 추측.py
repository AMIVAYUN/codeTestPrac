# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:25:51 2022
@FileName: 콜라츠 추측.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/12943
"""


def solution(num):
    cnt = 0;
    for i in range( 500 ):
        if( num == 1 ): 
            break;
        else:
            if( num%2 ):
                num = 3 * num + 1
                
            else:
                num //= 2;
                
    
        cnt += 1;
        
        
    return cnt if cnt < 500 else -1;