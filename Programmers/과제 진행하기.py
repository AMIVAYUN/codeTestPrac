# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:32:47 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


#과제진행하기
def solution(plans):
    answer = [];
    import time;
    '''
    시작하기로 한 시각 -> 시작
   
    새로운거 시작 -> 진행중이던거 멈춤
   
    진행중 과제 끝 -> 멈춘거 이어서 ( 새로 시작하는게 우선 )
   
    멈춘거 할땐 가장 최근에 하던거 ( stack )
   
    plan이 정렬 안되어 있을 수 있음.
   
    시작시간 겹칠일 x;
   
    '''
   
    remainstack = [];
   
    dit = dict();
   
    for plan in plans:
        dit[ plan[ 0 ] ] = ( int( plan[ 1 ][ :2 ] ) * 60 + int( plan[ 1 ][ 3: ]) , int( plan[ 2 ] ) );
    newplans = list( dit.items() );
   
    newplans = list( sorted( newplans, key= lambda x: ( x[ 1 ] ) ) );
   
   
    from collections import deque;
   
    dq = deque( newplans );
   
    now = 0;
       
    while dq:
       
        subject, time = dq.popleft();
       
        start, dur = time;
       
        if( len( dq ) == 0 ):
            now = start + dur;
            answer.append( subject );
            continue;
           
        predict = sum( time );
       
        next = dq[ 0 ][ 1 ][ 0 ] ;
       
       
       
        if( predict > next ):
           
            remainstack.append( [ subject, dur - ( next - start ) ] );
       
        elif( predict == next ) :
           
            answer.append( subject );
       
        else:
            answer.append( subject );
            remain = next - predict;
           
            if remainstack:
               
                while remainstack and remain >= remainstack[ -1 ][ 1 ]:
                    sub, rem = remainstack.pop();
                    remain -= rem;
                    answer.append( sub );

                if( len( remainstack ) ):


                    remainstack[ -1 ][ -1 ] -= remain;
           
                   
               
               
   
   
       
   
   
    return answer + [ i[ 0 ] for i in remainstack[ ::-1 ] ]