# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 19:02:43 2022
@FileName: 17245.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/17245
"""

# 70% Timeout
def t1():
    
    N = int( input() );
    
    
    serverRoom = [0] * 10000001;
    sum_ = 0;
    Mx = 0;
    for i in range( N ):
        row = list( map( int, input().split() ) );
        sum_ += sum( row );
        for idx in row:
            Mx = max( Mx, idx );
            for j in range( 1, idx + 1 ):
                serverRoom[ j ] += 1;
    
    
    lt = 0; rt= Mx + 1;
    
    sec = 0;
    
    while lt<= rt:
        mid = ( lt + rt ) // 2;
        
        active = sum( serverRoom[: mid + 1 ] );
        
        if( active >= sum_ /2 ):
            sec = mid;
            rt = mid - 1;
        else:
            lt = mid + 1
    
            
        
    
    print( sec )
    
def t2():
    N = int( input() );
    
    serverRoom = [];
    
    sum_ = Mx = 0;
    
    for i in range( N ):
        row = list( map( int, input().split() ) );
        sum_ += sum( row );
        serverRoom.append( row );
        Mx = max( max( row ), Mx );
    
    
    lt = 0; rt = Mx + 1;
    sec = 0;
    while lt<= rt :
        mid = ( lt + rt ) // 2;
        active = 0;
        for i in range( N ):
            for j in range( N ):
                active += serverRoom[ i ][ j ] if serverRoom[ i ][ j ] < mid else mid;
        
        if( active >= sum_ / 2 ):
            sec = mid;
            rt = mid - 1;
        else:
            lt = mid + 1;
    print( sec );
    
    
t2()