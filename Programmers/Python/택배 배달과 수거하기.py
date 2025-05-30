# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 11:58:25 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""



#SOL1
def solution(cap, n, deliveries, pickups):
    # 배달을 다니면서 빈 재활용 상자 수거
    
    # i번째 집은 원점으로 부터 거리 i
    
    # cap은 최대 실을 수 있는 상자 개수
    
    # --각 집에 배달 및 수거를 할 때 원하는 개수만큼 택배를 배달 + 수거 가능--
    
    
    answer = 0;
    
    deliveries = [ ( deliveries[ i ], i + 1 ) for i in range( n )]
    
    pickups = [ ( pickups[ i ], i + 1 ) for i in range( n )]
    
    dist = 1;
    
    
    while deliveries and pickups:
        
        rem_d, rem_p = cap, cap;
        Mxdis = 0;
        
        
        while deliveries and rem_d > 0:
            rem, dis = deliveries.pop()
            if( rem == 0 ):
                continue; 
            if( rem > rem_d ):
                Mxdis = max( Mxdis, dis );
                deliveries.append( ( rem - rem_d , dis ) );
                rem_d = 0;
            else:
                rem_d -= rem
                Mxdis = max( Mxdis, dis );
    
        while pickups and rem_p > 0:
            rem, dis = pickups.pop();
            if( rem == 0 ):
                continue; 
            if( rem > rem_p ):
                Mxdis = max( Mxdis, dis );
                pickups.append( ( rem - rem_p, dis ) );
                rem_p = 0;
            else:
                rem_p -= rem
                Mxdis = max( Mxdis, dis );

        
        answer += Mxdis * 2;


    while deliveries:

        rem_d, rem_p = cap, cap;
        Mxdis = 0;
        while deliveries and rem_d > 0:
            rem, dis = deliveries.pop()
            if( rem == 0 ):
                continue; 
            if( rem > rem_d ):
                deliveries.append( ( rem - rem_d , dis ) );
                Mxdis = max( Mxdis, dis );
                rem_d = 0;
            else:
                rem_d -= rem
                Mxdis = max( Mxdis, dis );
        
        answer += Mxdis * 2;
 
        
    while pickups:
        rem_d, rem_p = cap, cap;
        Mxdis = 0;
        while pickups and rem_p > 0:
            rem, dis = pickups.pop();
            if( rem == 0 ):
                continue;
            if( rem > rem_p ):
                Mxdis = max( Mxdis, dis );
                pickups.append( ( rem - rem_p, dis ) );
                rem_p = 0;
            else:
                rem_p -= rem
                Mxdis = max( Mxdis, dis );


        answer += Mxdis * 2;
    
    return answer
    
