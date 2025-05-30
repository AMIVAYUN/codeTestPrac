# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 12:33:17 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n, m, section):
    answer = 0;
    '''
    n미터의 벽
    
    1미터 길이의 구역 n개로 나누고 1~n 번호 지정
    
    한번에 m미터씩 칠함
    
    규칙
        1. 롤러 벽 벗어나기 x
        2. 구역의 일부분만 칠하기 x
    
    롤러 페인트질 최소 횟수
    
    section은 원소의 페인트를 다시 칠해야 하는 구역
        
    '''
    from collections import deque;
    
    section = deque( section );
    
    while section:
        now = section.popleft();
        Mx = ( m - 1 ) + now

        while section and Mx >= section[ 0 ]:
            
            section.popleft();
        
        answer += 1;
        
    
    
    
    return answer