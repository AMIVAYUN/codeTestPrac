# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 20:46:29 2022
@FileName: 2108.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2108
"""
import math

N = int( input() );

lst = [];
dit = {}
for i in range( N ):
    a = int( input() )
    
    lst.append( a );
    
    if( a in dit ):
        dit[ a ] += 1;
        
    else:
        dit[ a ] = 1;
    
lst = sorted( lst );

aver = int(  round( sum( lst ) / N , 0 ) );




cent = lst[ N // 2 ];


dit = sorted( dit.items(), key = lambda x: ( - x[ 1 ], x[ 0 ] ) );

ran = lst[ N - 1 ] - lst[ 0 ]


print( aver );

print( cent );

print( dit[ 1 ][ 0 ] if len( dit ) > 1 and dit[ 0 ][ 1 ] == dit[ 1 ][ 1 ] else dit[ 0 ][ 0 ]  )

print( ran );