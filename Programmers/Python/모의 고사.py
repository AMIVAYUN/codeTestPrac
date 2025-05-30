# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 14:21:16 2022
@FileName: 모의고사.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/42840
"""


def solution(answers):
    dit = { 1: [1,2,3,4,5] ,2: [2,1,2,3,2,4,2,5], 3:[3,3,1,1,2,2,4,4,5,5] }
    dit2 = { 1: 0, 2: 0, 3: 0 };
    for i in dit:
        lenx = len( dit[ i ] );
        leny = len( answers )
        for j in range( leny ):
            if( dit[ i ][ j % lenx ] == answers[ j ] ):
                dit2[ i ] += 1;
        
    answer = [ i for i in dit if dit2[ i ] == max( dit2.values() ) ]
    return answer
        