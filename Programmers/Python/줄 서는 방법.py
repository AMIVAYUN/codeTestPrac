# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:29:09 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


'''
4!
4!
4!
4!
4!

줄 서는 방법

'''


def factorial( n ):
    stan = 1;
    for i in range( 1, n + 1  ):
        stan *= i;
        
    return stan;


def solution(n, k):
    import itertools;
    lst = [ i for i in range( 1, n + 1 ) ];
    
    start = factorial( n - 1 );
    
    answer = [];
    
    while k != 0:
        div, k = divmod( k, start );
        
        print( div, k, start )
        
        if( k ):
            div += 1;
        
        answer.append( lst.pop( div - 1 ) );

        
        n -= 1;
        start = factorial( n - 1 );
        
    
    return answer + list( reversed( lst ) );
        
        
        

