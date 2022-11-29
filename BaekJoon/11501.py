# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:33:58 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def sol1():
    #8% WA
    T = int( input() );
    for _ in range( T ):
        leng = int( input() );
        answer = 0;
        stock = list( map( int, input().split() ) );
        stack = [];
        for i in range( leng ):
            if( stock[ i ] > stock[ i + 1 ] or i == leng - 1 ):
                
                while stack:
                    val = stack.pop();
                    answer += stock[ i ] - val;
            
            else:
                stack.append( stock[ i ] );
                
        
        print( answer );




T = int( input() );
    
for i in range( T ):
    leng = int( input() );
    answer = 0;
    stock = list( map( int, input().split() ) );
    
    Mx = stock.pop();
    stack = [ Mx ];
    while stock:
        
        if( Mx >= stock[ -1 ] ):
            stack.append( stock.pop() );
        
        else:
            while stack:
                answer += Mx - stack.pop();
            
            Mx = stock.pop();
    while stack:
        answer += Mx - stack.pop();
    
    print( answer );
        

        