# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:12:28 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def isPrime( num ):
    if( num == 1 ):
        return False;
    for i in range( 2, int ( num ** 0.5 ) + 1 ):
        if( num % i == 0 ):
            return False;
    
    return True;

N = int( input() );

lst = list( map( int, input().split() ) );

ans = 0;

for num in lst:
    if( isPrime( num ) ):
        ans += 1;

print( ans )
    