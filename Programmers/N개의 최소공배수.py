# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 11:07:07 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def GCD( a, b ):
    if ( b == 0 ):
        return a;
    else:
        return GCD( b, a % b );
            
def getLCM( a, b ):

    return ( a * b ) // GCD( a, b )

def solution(arr):
    answer = 0
    cons = arr[ 0 ]
    for i in range( 1, len( arr ) ):
        cons = getLCM( cons, arr[ i ] )
    return cons