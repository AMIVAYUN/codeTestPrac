# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 14:05:05 2022
@FileName: 1026.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1026
"""


N = int( input() );


A = list( map( int, input().split() ) );

B = list( map( int, input().split() ) );


A = sorted( A );

B = sorted( B , reverse = True );

rs = sum ( [ A[ i ] * B[ i ] for i in range( N ) ] )
