# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:28:53 2022
@FileName: 9461.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/9461
"""

T = int( input() );
nlst = [];
lst = [ 1,1,1 ] + [ 0 ] * 98;
for i in range( T ):
    nlst.append( int( input() ) )

    

for i in range( 3, max( nlst ) + 1):
    lst[ i ] = lst[ i -2 ] + lst[ i - 3 ];


for i in nlst:
    print( lst[ i - 1 ] );
    
