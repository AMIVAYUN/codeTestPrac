# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 12:49:10 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(storey):
    answer = 0;
    move = int( 1e6 );
    while storey > 0:
        move = storey % 10;
        storey = storey // 10;
        
        if( move > 5 or ( move == 5 and storey % 10 >= 5) ):
            storey += 1;
            move = 10 - move;
            answer += move;
        else:
            answer += move;
            
        
    return answer





'''
#2 BFS TimeOut;
def solution(storey):
    from collections import deque;
    import math;
    Mn = int( 1e8 )
    dq = deque();
    
    answer = 0;
    
    dq.append( ( 0, storey ) );
    
    while dq:

        cnt, now = dq.popleft();
        
        if( cnt > Mn ):
            continue;
        Neg = False;
        if( now < 0 ):
            Neg = True;
            now *= -1;
        start = 1;

        for i in range( 8 ):
        
            if( 0.0 < now / start < 1.0 ):
                start /= 10;
                break;
        
            start *= 10;
    
        start = math.trunc( start );
        
        tt = now // start;

        if( Neg ):
            now *= -1;
            if( now + ( tt * start ) == 0 ):
                Mn = min( Mn, cnt + tt );
            
            else:
                if( cnt + tt < Mn ):
                    
                    dq.append( ( cnt + tt, now + ( tt * start ) ) );
            
            
            offset = tt + 1 if( tt + 1 < 10 ) else 1;
            
            if( now + ( ( tt + 1 ) * start ) == 0 ):
                Mn = min( Mn, cnt + offset );
            
            else:
                if( cnt + offset < Mn ):
                    dq.append( ( cnt + offset, now + ( ( tt + 1 ) * start ) ) );
            
            
            
            
            
        else:
            if( now - ( tt * start ) == 0 ):
                Mn = min( Mn, cnt + tt );
            
            else:
                if( cnt + tt < Mn ):
                    dq.append( ( cnt + tt, now - ( tt * start ) ) );
            
            
            offset = tt + 1 if( tt + 1 < 10 ) else 1;
            
            if( now - ( ( tt + 1 ) * start ) == 0 ):
                Mn = min( Mn, cnt + offset );
            
            else:
                if( cnt + offset < Mn ):
                    
                    dq.append( ( cnt + offset, now - ( ( tt + 1 ) * start ) ) );
            
    
    
        
    return Mn;

'''

'''
#1 23.1
Mn = int( 1e8 );
import math;
def dfs( cnt, now ):
    print( now, cnt )
    global Mn;
    if( Mn < cnt ):
        return;
    
    if( now == 0 ):
        Mn = min( cnt, Mn );
        return;
    
    Neg = now < 0;
    
    #음수라면 먼저 양수 존에서 해결.
    if( Neg ):
        now *= -1;
    

    
    start = 1;

    for i in range( 8 ):
        
        if( 0.0 < now / start < 1.0 ):
            start /= 10;
            break;
        
        start *= 10;
    
    start = math.trunc( start );
    
    tt = now // start;
    
    if( Neg ):
        now *= -1;
        dfs( cnt + tt, now + ( tt * start ) );
        dfs( cnt + ( tt+ 1 ), now + ( (tt + 1 ) * start ) );
        
    else:
        offset = tt + 1 if tt + 1 < 10 else 1;
        dfs( cnt + tt, now - ( tt * start ) );
        dfs( cnt + ( offset ), now - ( (tt + 1 ) * start ) );
    
    
def solution(storey):
    global Mn, start;
    
    dfs( 0, storey );
    return Mn;
    
'''