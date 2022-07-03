# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 15:32:42 2022
@FileName: 1439.py
@author: YUNJUSEOK
@Link:
"""


def f3():
    str0 = input();
    lenx = len( str0 );
    lst = [ int( i ) for i in list( str0 ) ]
    cond = lst[ 0 ]
    cnt = [ 0, 0 ]
    cnt[ cond ] += 1
    for i in range( 1, lenx ):
        if( cond == lst[ i ] ):
            continue;
        cnt[ lst[ i ] ] += 1
        cond = lst[ i ] 
      
    print( min( cnt ) )
    
    
f3()