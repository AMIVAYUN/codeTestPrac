# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 17:10:45 2022
@FileName: 1302.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1302
"""

N = int( input() );
from collections import defaultdict;
ditt = defaultdict( int );
for i in range( N ):
    inp = input();
    ditt[ inp ] += 1;
    

Mx = max( ditt.values() );
lst = [];
for key in ditt:
    if( ditt[ key ] == Mx ):
        lst.append( key );


print( sorted( lst )[ 0 ] )

    