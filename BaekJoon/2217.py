# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:25:36 2022
@FileName: 2217.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2217
"""

N = int( input() );

lst = []

for i in range( N ):
    lst.append( int( input() ) );
    

lst = list( sorted( lst, reverse = True ) );
Mx = 0;
for i in range( N ):
    Mx = max( Mx, lst[ i ] * ( i + 1 ) );

print( Mx )

