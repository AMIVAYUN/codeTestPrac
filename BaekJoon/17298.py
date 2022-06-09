# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:34:13 2022
@FileName: 17298.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/17298
"""


import sys
#N = input()
N = int( sys.stdin.readline() );
lst = list( map( int,  sys.stdin.readline().split() ) ) 
idx = 1;
stack = [ ( idx - 1, lst[ idx - 1 ] ) ]
while stack:
    if( idx == len( lst ) ):
        break;

    while( len( stack ) and stack[ -1 ][ 1 ] < lst[ idx ] ):
        val =stack.pop();

        lst[ val[ 0 ] ] = lst[ idx ];
    
    stack.append( (idx,lst[ idx ]) );
    idx += 1;
    
while stack:
    val = stack.pop();
    lst[ val[ 0 ] ] = -1
    

for i in lst:
    print( i,end= ' ')
    