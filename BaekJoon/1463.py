# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 12:53:57 2022
@FileName: 1463.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1463
"""


def main():
    lst = [ 0 ] * ( int( 1e6 ) + 1 );

    n = int( input() );
    
    for i in range( 2, n + 1 ):
        lst[ i ] = lst[ i - 1 ] + 1;
        
        if( i % 3 == 0 ):
            lst[ i ] = min( lst[ i ], lst[ i //3 ] + 1 );
        
        if( i % 2 == 0 ):
            lst[ i ] = min( lst[ i ], lst[ i // 2 ] + 1 );
    
    print( lst[ n ] )
        
        
    
    
    
    
    
    
    



if( __name__ == "__main__"):
    main()

