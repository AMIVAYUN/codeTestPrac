# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:02:30 2022
@FileName: 1003.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/1003
"""



def main():
    lst =  [ [ 0, 0 ] for i in range( 41 ) ]
    lst[ 0 ] = [ 1, 0 ]; lst[ 1 ] = [ 0, 1 ];
    T = int ( input( ) );
    nlst = [];
    for i in range( T ):
        nlst.append( int( input() ) );

    for i in range( 2, max( nlst ) + 1 ):
        lst[ i ] = [ lst[ i - 1 ][ j ] + lst[ i - 2 ][ j ] for j in range( 2 ) ]

    for i in nlst:
        print( lst[ i ][ 0 ], lst[ i ][ 1 ])



if( __name__ == "__main__" ):
    main();
