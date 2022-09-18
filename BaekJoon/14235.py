# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:44:24 2022
@FileName: 14235.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/14235
"""


import heapq;


N = int( input() );

Presents = [];

heapq.heapify( Presents );


for i in range( N ):
    num = list( map( int, input().split() ) );
    
    if( num[ 0 ] == 0 ):
        if( len( Presents ) ):
            print( -1 * heapq.heappop( Presents ) )
        else:
            print( -1 )
    
    else:
        for i in range( 1, len( num ) ):
            heapq.heappush( Presents, -1 * num[ i ] )

