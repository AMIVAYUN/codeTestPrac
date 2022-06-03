# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:25:02 2022
@FileName: 약수의 개수와 덧셈.py
@author: YUNJUSEOK
@Link : https://programmers.co.kr/learn/courses/30/lessons/77884
"""

def solution(left, right):
    answer = 0;
    for i in range( left, right + 1 ):
        answer += ( ( -1 ) ** getDiv( i ) ) * i  
    return answer

def getDiv( num ):
    lst = [];
    for i in range( 1, num + 1 ):
        if( num % i == 0 ):
            lst.append( i );
    
    return len( lst );


