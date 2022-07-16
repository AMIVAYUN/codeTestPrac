# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 11:01:16 2022
@FileName: 9252.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/9252
"""
a = list ( input() );

b = list ( input() );

dp = [ [""] * ( len( b ) + 1 ) for _ in range( len( a ) + 1 ) ];

cond = False
for i in range( 1, len( a ) + 1 ):
    for j in range( 1, len( b ) + 1 ):
        
        if( a[ i - 1 ] != b[ j - 1 ] ):
            dp[ i ][ j ] = dp[ i - 1 ][ j ] if len( dp[ i - 1 ][ j ] ) > len( dp[ i ][ j - 1 ] ) else dp[ i ][ j - 1 ]
        else:
            dp[ i ][ j ] = ( dp[ i - 1 ][ j - 1 ] + a[ i - 1 ] );


            
    
print( len( dp[ -1 ][ -1 ] ) );

print( dp[ -1 ][ -1 ] );

