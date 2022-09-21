# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:03:00 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


S = list( input() );

T = list( input() );

while len( T ) != len( S ):
    if( T[ -1 ] == 'A' ):
        T.pop()
    else:
        T.pop()
        T.reverse();
    

print( int( T == S ) )