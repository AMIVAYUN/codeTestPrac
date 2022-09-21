# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:04:38 2022
@FileName: 1181.py
@author: YUNJUSEOK
@Link:
"""


N = int( input() );

lst = [];

for i in range( N ):
    lst.append( input() );
    
    
lst = set( sorted( lst, key = lambda  x:( len( x ), x ) ) )

for ch in lst:
    print( ch )