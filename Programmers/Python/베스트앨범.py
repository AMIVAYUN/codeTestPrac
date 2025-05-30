# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:22:34 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(genres, plays):
    '''
    장르 별로 가장 많이 재생된 노래 두개씩;
    
    속한 노래가 많다.
    장르 내에서 많이 재생됬다.
    고유 번호가 낮다.
    
    '''
    from collections import defaultdict
    total = defaultdict( int );
    leng = len( genres );
    for i in range( leng ):
        total[ genres[ i ] ] += plays[ i ]
        
        
    makeOut = defaultdict( list );
  
    for i in range( leng ):
        makeOut[ genres[ i ] ].append( ( i,  plays[ i ] ) );
                                      
    totitems = list( total.items() );
    totitems = list( sorted( totitems, key = lambda x: ( -x[ 1 ] ) ) );
    
    for key in makeOut:
        makeOut[ key ] = list( sorted( makeOut[ key ], key = lambda x: ( -x[ 1 ], x[ 0 ] ) ) );
        
    
    answer = []
    
    for genre, uses in totitems:
        answer += [ i[ 0 ] for i in makeOut[ genre ][:2] ]
       
    
    
    return answer