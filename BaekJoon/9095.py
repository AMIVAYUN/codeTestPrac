# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:09:50 2022
@FileName: 9095.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/9095
"""

def main():
    lst = [ 0, 1, 2, 4 ] + [ 0 ] * 8
    
    T = int( input() );
    Nlst = [];
    for i in range( T ):
        Nlst.append( int( input() ) ) 
    
    for i in range( 4, max( Nlst ) + 1 ):
        lst[ i ] = lst [ i - 1 ] + lst [ i - 2 ] + lst [ i - 3 ]
    
    for i in Nlst:
        print( lst[ i ] )
if( __name__ == "__main__"):
    main()