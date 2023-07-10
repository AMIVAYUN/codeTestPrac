# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 00:18:35 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

'''

0 1

2 3




'''



n, r, c = map( int, input().split() );

answer = 0;


def dfs( cost, depth ):
    global r, c, answer;
    
    
    if( depth == -2 ):
        answer = cost;
        return;
    
    
    
    if( r < 2 ** depth and c < 2 ** depth ):
        dfs( cost, depth - 1 );
        
    
    elif( r < 2 ** depth and c >= 2 ** depth ):
        c -= 2 ** depth;
        dfs( cost + ( ( 2 ** depth ) ** 2 ) , depth - 1 );
        
    elif( r >= 2 ** depth and c < 2 ** depth ):
        r -= 2 ** depth;
        dfs( cost + ( ( 2 ** depth ) ** 2 ) * 2 , depth - 1 );
    
    else:
        r -= 2 ** depth; c -= 2 ** depth;
        dfs( cost + ( ( 2 ** depth ) ** 2 ) * 3, depth - 1 );
    

dfs( 0, n - 1 );

print( answer );