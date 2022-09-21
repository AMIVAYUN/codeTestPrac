# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:16:56 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
from collections import deque;

# 50점

def t1():
    

    N = int( input() );
    
    M = int( input() );
    
    S = list( input() );
    
    
    check = list( ( "IO" * N ) + "I" )
    
    leng = len( check ) 
    
    cnt = 0;
    
    for i in range( M - N + 1 ):
        if( S[ i ] == 'I' ):
            
            cnt += int( check == S[ i: i + leng ] )
        
    print( cnt )
    
    
def t2():
    
    N = int( input() );
    
    M = int( input() );
    
    S = input()

    idx = 0;
    
    checker = "IOI"
    cnt = 0;
    inner_cnt = 0;
    while idx < M:

        if( S[ idx: idx + 3 ] == checker ):
            idx = idx + 2;
            inner_cnt += 1;
        else:
            idx += 1
            inner_cnt = 0;
            
        if( inner_cnt == N ):
            inner_cnt -= 1;
            cnt += 1;
        
    print( cnt )
t2()