# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 13:17:06 2022
@FileName: 1920.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1920
"""


N = int( input() );

dit = {};
Nlst = list( map( int, input().split() ) );
for i in Nlst:
    dit[ i ] = 1;
    

M = int( input() );

Mlst = list( map( int, input().split() ) ) ;

for i in Mlst:
    print( int( i in dit ) );