# -*- coding: utf-8 -*-
"""
Created on Wed May 25 12:47:05 2022
@FileName: 4963.py
@author: YUNJUSEOK
@Link: https://www.acmicpc.net/problem/4963
DFS

"""
import sys;
sys.setrecursionlimit( int( 1e6 ) );
lst = [];
dx = [ 0, 0, -1, -1, -1, 1, 1, 1]
dy = [ 1, -1, 0, 1, -1, 0, 1, -1 ]

cnt = 0;

def dfs( x, y ):
    
    lst[ y ][ x ] = 0;
    
    for i in range( len( dx ) ):
        if( x + dx[ i ] >= 0 and x + dx[ i ] < w and y + dy[ i ] >= 0 and y + dy[ i ] < h):
           
            if( lst[ y + dy[ i ] ][ x + dx[ i ] ] == 1 ):
                dfs( x + dx[ i ], y + dy[ i ] );
            
            
    return;
    
while True:
    lst = [];
    cnt = 0;
    w, h = map( int, input().split() );
    if( w == 0 and h == 0 ):
        break;
    for i in range( h ):
        lst.append( list( map( int, input().split() ) ) );
    
    for y in range( h ):
        for x in range( w ):
            if( lst[ y ][ x ] == 1 ):
                
                dfs( x, y );
                cnt += 1;
    
    print( cnt );
    

    


