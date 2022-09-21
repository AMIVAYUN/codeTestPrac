# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:00:09 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


T = int( input() );

def getDist( a, b ):
    return ( ( a[ 0 ] - b[ 0 ] ) **2 + ( a[ 1 ] - b[ 1 ] ) **2 ) **0.5


for i in range( T ):
    x1,y1,r1,x2,y2,r2 = map( int, input().split() );
    r3 = getDist( ( x1, y1 ), ( x2, y2 ) )
    if( x1 == x2 and y1 == y2 and r1 == r2 ):
        print( -1 )
    
    elif( r1 + r2 ) > r3 > abs( r1 - r2 ):
        print( 2 );
    elif int( r1 + r2 ) == r3 :
        print( 1 );
    else:
        print( 0 );
    
    