# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:17:36 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def t1():
    N = int( input() );

    M = int( input() );

    pos = list( map( int, input().split() ) );


    Object = [ _ for _ in range( N + 1 ) ];

    Objset = set( Object );

    lt = 0; rt = N;
    ans = 0;
    while lt <= rt:
        
        ranges = set();
        H = ( lt + rt ) // 2 ; 
        for i in pos:
            pos_start, pos_end = i - H, i + H;
            for col_pos in range( i - H , i + H + 1 ):
                if( col_pos < 0 ):
                    continue;
                ranges.add( col_pos );
            
        rs = Objset - ranges;
        
        if( len( rs ) == 0 ):
            ans = H;
            rt = H - 1
        else:
            lt = H + 1;


    print( ans )
    
    
    
def t2():
    