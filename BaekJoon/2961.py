# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 20:44:51 2022
@FileName: 2961.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2961
"""


N = int( input() );
flavor = [];
for i in range( N ):
    Si, Bi = map( int, input().split() );
    
    flavor.append( ( Si, Bi ) );
import itertools;

lst = [ i for i in range( N ) ];
res = float( "inf" );
for i in range( 1, N + 1 ):
    cmb = list( itertools.combinations( lst , i ) );
    
    for case in cmb:
        S = 1; B = 0;
        for case_ in case:
            S *= flavor[ case_ ][ 0 ];
            B += flavor[ case_ ][ 1 ];

        res = min( abs( S - B ), res );

print( res ) 