# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:34:08 2022
@FileName: 5502.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/5502
"""
'''
 abba 
'''
def f1():
    leng = int( input() );

    str0 = input();

    idx = 0 ;

    stack = [];

    temp = "";

    for i in range( leng ):
        if( str0[ i ] in temp ):
            temp = temp.replace( str0[ i ], "" )
            continue;
        temp += str0[ i ];
    if( leng % 2 == 0):
        print( len( temp ) + 1 )
    else:
        print( len( temp ) - 1 if len( temp ) else 0 )



def f2():
    from collections import defaultdict;
    
    N = int( input() );
    
    M = list( input() );
    
    rev = list( reversed( M ) );
    
    dp = [[ 0 ] * ( N + 1 ) for i in range( N + 1 ) ];
    
    for i in range( 1, N + 1 ):
        for j in range( 1, N + 1 ):
            if( M[ i - 1 ] != rev[ j - 1 ] ):
                dp[ i ][ j ] = max( dp[ i - 1 ][ j ], dp[ i ][ j - 1 ] )
                
            else:
                dp[ i ][ j ] = dp[ i - 1 ][ j - 1 ] + 1
                
    print( N - dp[ -1 ][ -1 ] )
            


    
if( __name__ == "__main__" ):
    f2();
