# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:02:16 2022
@FileName: 실패율.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/42889
"""

#사전형 정렬에 대해서 더 배울 수 있는 시간이었다 우선순위 별로 나열하는 것이 이렇게 간단하게 될 줄 몰랐다.
def solution(N, stages):
    dit = {};
    for i in range( 1, N + 2 ):
        dit[ i ] = 0;
        
    for j in stages:
        dit[ j ] += 1;
            
    dit2 = {};
    sum0 = sum( stages );
    for i in dit:
        idx = ( len( stages ) - sum( [ dit[ j ] for j in range( 1, i ) ] ) );
        dit2[ i ] =( dit[ i ] / idx ) if idx != 0 else 0 
    dit2 = { i: dit2[i] for i in dit2 if i < N + 1 }
    
    
    answer = sorted( dit2.items(), key = lambda x: ( -x[1], x[0] ) );
    
    return [ i[0] for i in answer]