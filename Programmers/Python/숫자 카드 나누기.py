# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:44:57 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def gcd( a, b ):
    if( a == 0 ):
        return b;
    elif( a >= b ):
        return gcd( a % b , b )
    else:
        return gcd( b, a );
    
def getDnum( a ):
    lst = [];
    for i in range( 1, a + 1 ):
        if( a % i == 0 ):
            lst.append( i );
    
    return lst;

    
    
def solution(arrayA, arrayB):
    answer = 0;
    ga = arrayA[ 0 ];
    gb = arrayB[ 0 ];
    for num in arrayA[ 1: ]:
        ga = gcd( ga, num );
    
    for num in arrayB[ 1: ]:
        gb = gcd( gb, num )

    
    for num in arrayA:
        if( num % gb == 0 ):
            gb = 0;
            break;
        
    for num in arrayB:
        if( num % ga == 0 ):
            ga = 0;
            break;
    

    return max( ga, gb );