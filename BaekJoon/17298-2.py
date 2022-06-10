# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 19:51:45 2022
@FileName: 17298 -2 .py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/17298
"""


def main():
    N = int( input() );
    A = [ int( i ) for i in input().split() ];
    stack = [ 0 ];
    result = [ -1 ] * N ;
    for i in range( 1, N ):
        while( stack[ -1 ] < A[ i ] ):
            idx = stack.pop();
            result[ idx ] = A[ i ];
        
        stack.append( i );
            
        



if( __name__ == "__main__"):
    main()