# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:16:07 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(n):
    answer = 0
    flag = False;
    bn = bin( n )[ 2 : ]
    leng = len( bn )
    bn ="0"+bn;
    
    idx = leng
    point1 = leng;

    flag = True
    flag2 = True
    point2 = 0;
    while idx > 0 and flag2:
        if( bn[ idx ] == '1' and flag):
            point1 = idx;
            idx -=1
            flag = False;
            while idx > 0:
                if( bn[ idx ] == '0' ):
                    flag2 = False;
                    point2 = idx;
                    break;
                idx -= 1;
        idx -= 1
    bn = list( bn );

    bn[ point2 ] = '1'
    bn[ point1 ] = '0'
    bn = bn[ : point2 + 1 ]+ list( sorted( bn[ point2 + 1 :] ) ) 

    
    return int( ''.join( bn ), 2 )