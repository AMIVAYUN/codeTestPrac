# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 15:35:09 2022
@FileName: 15652.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/15652
"""

N, M = map( int, input().split() );


lst = [ i for i in range( 1, N + 1 ) ];
res = []


def dfs( depth, proc ):
    print( depth, proc )
    global N, M, res, lst;
    
    if( depth == M ):
        res.append( proc );
        return;
        
    
    if( depth == 0 ):
        for i in range( N ):
            temp = proc[:];
            
            temp.append( lst[ i ] );
            dfs( depth + 1, temp );
    
    else:
        for i in range( N ):
            temp = proc[:];
            if( proc[ -1 ] <= lst[ i ] ):
                temp.append( lst[ i ] );
                dfs( depth + 1, temp );
        
    
dfs( 0, []) 
for i in res:
    for j in i:
        print( j, end = " " );
        
    print()