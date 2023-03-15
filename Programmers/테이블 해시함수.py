# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:54:11 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(data, col, row_begin, row_end):
    answer = 0;
    col -= 1;
    row_begin -= 1;
    row_end -= 1;
    #1 데이터를 col번째 기준 값으로 정렬 동일시 기본키 ( 0 번째 원소가 큰 것 );
    
    #2 각 데이터를 행번호로 나눈 나머지 값들의 합을 구함.
    
    # begin부터 end까지 XOR
    if( col == 0 ):
        data = list( sorted( data, key = lambda x: ( x[ col ]) ) );
    else:
        data = list( sorted( data, key = lambda x: ( x[ col ], -1 * x[ 0 ] ) ) );
    
    start = data[ row_begin ];
    
    standard = 0;
    for ch in start:
        standard += ( ch % ( row_begin + 1 ) );
    
    
    for idx in range( row_begin + 1, row_end + 1 ):
        now = 0;
        
        for ch in data[ idx ]:
            now += ( ch % ( idx + 1 ) );
        
        standard ^= now;
    
    
    return standard