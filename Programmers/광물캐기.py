# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 13:32:32 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(picks, minerals):
    answer = 0;
    '''
    목표: 사용 가능 곡괭이중 아무거나 하나.
    한번 사용 곡괭이 > 사용 못할떄 까지 즉 쓰면 끝
    광물은 주어진 순서대로 **
    
    광산에 모든 광물을 캐거나, 더 사용할 곡괭이가 없을떄 까지 광물 캠.
    
    곡 하나당 광물 5개
    
    [ 다이아, 철, 돌 ]
    
    ''' 
    from collections import defaultdict;
    
    mapper = { 'diamond': 0, 'iron': 1, 'stone': 2 }
    graph = [ [ 1, 1, 1 ] for _ in range( 3 ) ]
    graph[ 1 ] = [ 5, 1, 1 ];
    graph[ 2 ] = [ 25, 5, 1 ];
    
    # x값은 사용하고자 하는 곡괭이 
    # y값은 까고자 하는 돌
    
    new_minerals = [];

    '''
    leng = len( minerals );
    
    flag = leng % 5;
    
    flag = 1 if flag else 0;
    
    Mx = 25 * leng + 1;
    
    dp = [ Mx ] * ( leng // 5 + flag )
    
    newleng = leng // 5 + flag;
    
    for i in range( newleng ):
        next = minerals[ i * 5 : ( i + 1 ) * 5 ];
        
        #곡괭
        
        for i in range( 3 ):
            if( )
        
    '''    
    
    
    
    idx = 0;
    idxcnt = 0;
    #순서를 지켜야함
    while idx < len( minerals ):
        cnt = 0;
        tmp = [ 0 ] * 3;
        while idx < len( minerals ) and cnt < 5:
            cnt += 1;
            tmp[ mapper [minerals[ idx ] ] ] += 1;
            idx += 1;
        
        
        new_minerals.append( [idxcnt, tmp] );
        idxcnt += 1;
    
    sum_picks = sum( picks );
    
    new_minerals = new_minerals[ :sum_picks ];
    
    new_minerals = list( sorted( new_minerals , key = lambda x: ( x[ 1 ][ 0 ], x[ 1 ][ 1 ], x[ 1 ][ 2 ] ) ) );
    start = 0;
    while new_minerals:
        idx, next = new_minerals.pop();
        if( picks[ start ] ):
            picks[ start ] -= 1;
        
        else:
            while picks[ start ] == 0:
                
                start += 1;
            picks[ start ] -= 1;
        
        for i in range( 3 ):
            answer += graph[ start ][ i ] * next[ i ];
        
    
        
        
    return answer



solution( [1, 3, 2]	,["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])