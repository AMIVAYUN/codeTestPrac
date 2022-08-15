# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:24:13 2022
@FileName: 6603.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/6603
"""



import itertools;

while True:
    klst = list( map( int, input().split() ) );
    if( klst[ 0 ] == 0 ):
        break;
    k = klst[ 0 ];
    lst = klst[ 1: ];
    cmb = list( itertools.combinations( lst ,  6 ) )
    
    for case in cmb:
        str0 = "";
        
        for idx in case:
            str0 += str( idx ) + " " 
        
        print( str0 )
    
    print()
