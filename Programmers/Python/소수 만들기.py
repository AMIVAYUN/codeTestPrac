# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:18:18 2022
@FileName: 소수 만들기.py
@author: YUNJUSEOK
@Link: https://programmers.co.kr/learn/courses/30/lessons/12977
"""

def solution( nums ):
    import itertools;
    
    comb = list( itertools.combinations( nums , 3 ) );
    comb = [ sum( i ) for i in comb if isPrime( sum( i ) ) ]
    
    
    

  

    return len( comb )


def isPrime( num ):
    ran = int( num ** 0.5 ) + 1;
    for i in range( 2, ran ):
        if( num % i == 0 ):
            return False;
    
    return True;

