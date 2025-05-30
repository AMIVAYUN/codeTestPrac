# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:04:05 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(target):
    ### 잘못 생각함 생각해보니 더블 트리플은 전부 1 ~ 20 점에서 나는거임.
    ### 불보다 점수가 큰것 50보다 큰것 20 * 3 // 19 * 3 // 18 * 3 // 17 * 3하고 50임
                
    # 싱글 더블 트리플 불 싱글


    dp = [ [ 100001, 100001 ] ] * ( target + 1 );
    
    count, single = 0 , 1;
    
    Mx = 21 if target > 20 else target + 1
    
    dp[ 0 ] = [ 0, 0 ];

    #한칸씩
    for i in range( target + 1 ):

        for x in range( 1, 21 ):

            if( i + x > target ):
                break;
            # 싱글
            if( dp[ i + x ][ count ] > dp[ i ][ count ] + 1 ):
                dp[ i + x ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] + 1 ];
            
            elif( dp[ i + x ][ count ] == dp[ i ][ count ] + 1 and dp[ i + x ][ single ] < dp[ i ][ single ] + 1 ):
                dp[ i + x ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] + 1 ];
            
            if( i + ( 2 * x ) > target ):
                continue;
            #더블
            if( dp[ i + ( 2 * x ) ][ count ] > dp[ i ][ count ] + 1 ):
                dp[ i + ( 2 * x) ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] ];
            
            elif( dp[ i + ( 2 * x ) ][ count ] == dp[ i ][ count ] + 1 and dp[ i + ( 2 * x) ][ single ] < dp[ i ][ single ] ):
                dp[ i + ( 2 * x ) ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] ];
            if( i + ( 3 * x ) > target ):
                continue;
            #트리플
            if( dp[ i + ( 3 * x ) ][ count ] > dp[ i ][ count ] + 1 ):
                dp[ i + ( 3 * x) ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] ];
            
            elif( dp[ i + ( 3 * x ) ][ count ] == dp[ i ][ count ] + 1 and dp[ i + ( 3 * x) ][ single ] < dp[ i ][ single ] ):
                dp[ i + ( 3 * x ) ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] ];
            
        if( i + 50 > target ):
            continue;
            
        if( dp[ i +50 ][ count ] > dp[ i ][ count ] + 1 ):
            dp[ i + 50 ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] + 1 ];
        
        elif( dp[ i + 50 ][ count ] == dp[ i ][ count ] + 1 and dp[ i + 50 ][ single ] < dp[ i ][ single ] + 1 ):
            dp[ i + 50 ] = [ dp[ i ][ count ] + 1, dp[ i ][ single ] + 1 ];
                
    
    
    return dp[ target ];
'''
def solution(target):
    
    
    게임 시작 -> 무작위 점수 // 다트를 던져 점수를 깎아 0점으로
    남은 점수 > 득점 점수 --> 버스트 --> 실격
    외곽 : 더블
    내부: 트리플
    중앙 불 ( 50점 고정 )
    그외 지역: 싱글
    
    두 선수 -> 교대로 
    
    1. 0점 먼저 만든 사람
    2. 동 라운드시 싱글, 불 다수자
    3. 선공
    
    % 최소로 던지되 싱글 , 불 최대로 %

    
    bullcount = 0;
    while target > 50:
        target -= 50;
        bullcount += 1;
    count = 0;
    singbull = 1;
    answer = [];
    
    dp = [ [ target, bullcount ] ] * ( target + 1 );
    Mx = 21 if target > 20 else target + 1
    
    for i in range( 1, Mx ):
        dp[ i ] = [ 1 + bullcount, 1 + bullcount ];
        
    for i in range( 1, target + 1 ):

        # 싱글 더블 트리플 불 싱글
        
        #싱글
        if( i + 1 < target + 1 and dp[ i + 1 ][ count ] > dp[ i ][ count ] ):
            dp[ i + 1 ] = [ dp[ i ][ count ] + 1, dp[ i ][ singbull ] + 1 ];
        # 갯수가 같을때
        elif( i + 1 < target + 1 and dp[ i + 1 ][ count ] == dp[ i ][ count ] and dp[ i + 1 ][ singbull ] < dp[ i ][ singbull ] ):
            dp[ i + 1 ] = [ dp[ i ][ count ] + 1, dp[ i ][ singbull ] + 1 ];
        
        #싱글
        for x in range( 1, 20 ):
            if( i + x > target ):
                break;
            
            if( dp[ i + x ][ count ] > dp[ i ][ count ] + 1 ):
                dp[ i + 1 ] = [ dp[ i ][ count ] + 1, dp[ i ][ singbull ] + 1 ];
            # 갯수가 같을때
            elif( dp[ i + x ][ count ] == dp[ i ][ count ] and dp[ i + x ][ singbull ] < dp[ i ][ singbull ] + 1 ):
                dp[ i + x ] = [ dp[ i ][ count ] + 1, dp[ i ][ singbull ] + 1 ];  
            
        
        ### 잘못 생각함 생각해보니 더블 트리플은 전부 1 ~ 20 점에서 나는거임.
        ### 불보다 점수가 큰것 50보다 큰것 20 * 3 // 19 * 3 // 18 * 3 // 17 * 3하고 50임
        
        #더블
        # 갯수가 적으면
        if( i * 2 < target + 1 and dp[ i * 2 ][ count ] > dp[ i ][ count ] ):
            dp[ i * 2 ] = [ dp[ i ][ count ], dp[ i ][ singbull ] ];
        # 갯수가 같을때
        elif( i * 2 < target + 1 and dp[ i * 2 ][ count ] == dp[ i ][ count ] and dp[ i * 2 ][ singbull ] < dp[ i ][ singbull - 1 ] ):
            dp[ i * 2 ] = [ dp[ i ][ count ], dp[ i ][ singbull ] ];
        
        #트리플
        if( i * 3 < target + 1 and dp[ i * 3 ][ count ] > dp[ i ][ count ] ):
            dp[ i * 3 ] = [ dp[ i ][ count ], dp[ i ][ singbull ] ];
        # 갯수가 같을때
        elif( i * 3 < target + 1 and dp[ i * 3 ][ count ] == dp[ i ][ count ] and dp[ i * 3 ][ singbull ] < dp[ i ][ singbull ] ):
            dp[ i * 3 ] = [ dp[ i ][ count ], dp[ i ][ singbull ] ];
        
        
        
        
        
        
    
    return dp[ target ];
    
    
'''
