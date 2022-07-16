# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 12:49:29 2022
@FileName: 해시.py
@author: YUNJUSEOK
@Link:https://school.programmers.co.kr/learn/courses/30/lessons/42578
"""


def solution(clothes):
    from collections import defaultdict;
    import itertools;
    dit = defaultdict( int );
    
    for i in clothes:
        dit[ i[ 1 ] ] += 1;
        
    sum_ = 1;
    for val in dit.values():
        sum_ *= val + 1
    
    return sum_ -1
    
# test1 timeout
def solution1(clothes):
    from collections import defaultdict;
    answer = 0
    import itertools;
    dit = defaultdict( int );
    
    for i in clothes:
        dit[ i[ 1 ] ] += 1;
    keys = dit.keys();
    
    if( len( dit ) == 1 ):
        return sum( dit.values() );
    
    for i in range( 1, len( dit ) + 1 ):
        cmb = itertools.combinations( keys, i );
        for case in cmb:
            tmp = 1;
            for kind in case:
                tmp *= dit[ kind]            
            answer += tmp;
    

        
            
        
    
    return answer