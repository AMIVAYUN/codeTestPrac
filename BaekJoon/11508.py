# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:55:03 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N = int( input() );
lst = [];
for i in range( N ):
    lst.append( int( input() ) );
    

lst = list( sorted( lst, key = lambda x: -x ) );
sum_ = 0;
for i in range( 0, len( lst ), 3 ):
    sum_ += sum( lst[ i : i + 2 ] );
    
print( sum_ );
    