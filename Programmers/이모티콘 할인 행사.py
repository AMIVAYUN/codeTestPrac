# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:49:53 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(users, emoticons):
    '''
    목표
    
    1. 가입자를 최대한
    2. 판매액을 최대한
    
    n명에게 m개를 할인 판매
    
    n명은 각각 같은 기준에 따라 이모티콘 or 서비스 가입
    
        1. 일정 비율 이상 할인 모두 구매
        2. 구매 비용의 합이 일정 가격 이상이면 구매 취소 -> 서비스 가입.
        
     할인율은 10%, 20%, 30%, 40% 중 하나
     
     이모티콘은 7개
     
     4**7가지 --> 2*14 --> 16000 + a 완탐 가능 
    
    '''
    answer = ( 0, 0 );
    
    m = len( emoticons);
    
    import itertools;
    
    disRatio = [ 10, 20, 30, 40 ];
    
    product = list( itertools.product( disRatio, repeat = m ) );
    
    
    for case in product:
        new_user = 0;
        sum_ = 0;
        
        for user in users:
            price = 0;
            
            for i in range( m ):
                if user[ 0 ] <= case[ i ]:
                    
                    price += emoticons[ i ] * ( ( 100 - case[ i ] ) * 0.01 )
            
            if( int( price ) >= user[ 1 ] ):
                new_user += 1;
            else:
                sum_ += price;
        sum_ = int( sum_ )

        
        if( new_user > answer[ 0 ] ):
            answer = ( new_user, int( sum_ ) );
        elif(  new_user == answer[ 0 ] and sum_ > answer[ 1 ] ):
            answer = ( new_user, int( sum_ ) );
            
                
            
        
        
        
    
    
    
    
    
    return answer