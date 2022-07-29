# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 14:05:17 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

def sol1():
    def comp( a, b ):
        if( abs( a ) < abs( b ) ):
            return a;
        else:
            return b;

    N = int( input() );

    lst = list( map( int, input().split() ) );

    answer = None

    lst = sorted( lst );

    for i in lst:
        tmp = lst[ :i ] + lst[ i + 1: ]
        
        lt = 0; rt = N - 1;
        ans = 0;
        
        
        while( lt <= rt ):
            mid = ( lt + rt ) // 2;
            if( lst[ mid ] + i <= 0 ):
                lt = mid + 1;
                ans = mid;
            else:
                rt = mid - 1;
        
        subrs = i + lst[ ans ];
        if( answer == None ):
            answer = subrs;
        else:
            answer = comp( subrs, answer );
        
        if( answer == 0 ):
            break;

    print( answer) 

def sol2():
    N = int( input() );

    lst = list( map( int, input().split() ) );

    lst = sorted( lst );
    
    answer = ( 0, 0 );
    
    lt = 0; rt = N - 1 ;
    ans = None;
    while lt < rt:
        tmp = lst[ lt ] + lst[ rt ]
        if( ( ans == None ) or ( abs( ans ) > abs( tmp ) ) ):
            ans = tmp;
            answer = ( lt, rt );
            
        if( tmp <= 0 ):
            lt = lt + 1;
        else:
            rt = rt - 1;
        
    for rs in answer:
        print( lst[rs], end = " ")
    
 

sol2()