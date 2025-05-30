# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:39:14 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
하루에 하나씩만 구매 가능.

XYZ마트 일정 금액 지불시 10일 동안 회원자격 부여

회원 대상 한가지 제품 할인.

원하는 제품과 수량이 10일간 맞을시 회원가입 하려함.
'''
def check( ddit, wdit ):
    for key in ddit:
        if( key not in wdit or ddit[ key ] != wdit[ key ] ):
            return False;
    
    return True;
def solution(want, number, discount):
    from collections import defaultdict;
    answer = 0;
    wdit = {}
    ddit = {}
    
    for i in range( len( want ) ):
        wdit[ want[ i ] ] = number[ i ];
    
    for i in range( 10 ):
        if( discount[ i ] not in ddit ):
            ddit[ discount[ i ] ] = 1;
        else:
            ddit[ discount[ i ] ] += 1;
    
    answer += int( check( wdit, ddit ) );
    
    for i in range( 10, len( discount ) ):
        ddit[ discount[ i - 10 ] ] -= 1;
        if( discount[ i ] not in ddit ):
            ddit[ discount[ i ] ] = 1;
        else:
            ddit[ discount[ i ] ] += 1;
        answer += int( check( wdit, ddit ) );
        
    return answer