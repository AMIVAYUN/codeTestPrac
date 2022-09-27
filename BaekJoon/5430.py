# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:56:00 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

from collections import deque;
T = int( input() );

for _ in range( T ):
    p = input()
    n = int( input() );
    lst = input()[ 1:-1 ].split(',');
    flag = True;
    
    
    if( n == 0 ):
        lst = deque();
    else:
        lst = deque( lst );
        
    Rcnt = 0;
    for word in p:
        if( word == 'R' ):
            Rcnt += 1;
        
        elif( word == 'D' ):
            if( len( lst ) < 1 ):
                flag = False;
                break;
            
            if( Rcnt % 2 ):
                lst.pop();
            else:
                lst.popleft();
    
    if( flag ):
        if( Rcnt % 2 ):
            lst.reverse()
            print( '['+','.join( lst )+']')
        else:
            print( '[' + ','.join( lst ) + ']')
    
    else:
        print( "error" )