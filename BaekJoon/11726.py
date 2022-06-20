# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:59:33 2022
@FileName: 11726.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11726
"""

lst =[ 0, 1, 2, 3 ] + ( [ 0 ] * 998 )
n = int( input() );
for i in range( 4, n + 1):
    lst[ i ] = lst[ i - 1 ] + lst[ i - 2 ];

    
print( lst[ n ] % 10007 )
