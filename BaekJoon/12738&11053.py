# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 16:15:18 2022
@FileName: 12015 & 11053.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/12738
"""

def main():
    N = int( input() )
    A = [ int( i ) for  i in input().split() ];
    
    lst = [ 1 ] * N
    for i in range( N ):
        for j in range( i ):
            if( A[ i ] > A[ j ] ):
                lst[ i ] = max( lst[ j ] + 1, lst[ i ])
                
    
    print( max( lst ) )
    
    
    
if( __name__ == "__main__"):
    main()