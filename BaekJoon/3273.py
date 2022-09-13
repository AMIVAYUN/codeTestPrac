# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:13:00 2022
@FileName: 3273.py
@author: YUNJUSEOK
@Link:
"""


n = int( input() );


lst = list( map( int, input().split() ) );


x = int( input() );

answer = 0;

dit = {};

for number in lst:
    if( number in dit ):
        answer += 1;
    else:
        dit[ x - number ] = 1;

print( answer );