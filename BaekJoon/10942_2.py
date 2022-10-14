# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:01:55 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


leng = int( input() );

s = list( input().split() );



dp = [ [ 0 ] * leng for _ in range( leng ) ];


for offset in range( leng ):
    
    
    for x in range( leng - offset ):
        if( offset == 0 ):
            dp[ x ][ x + offset ] = 1;
            continue;
        elif( offset == 1 ):
            if( s[ x ] == s[ x + offset ] ):
                dp[ x ][ x + offset ] = 2;
        else:
            if( x + offset -1 >= 0 and dp[ x + 1 ][ x + offset - 1 ] > 0 and s[ x + offset ] == s[ x ] ):
                dp[ x ][ x + offset ] = dp[ x + 1 ][ x + offset - 1 ] + 2;


K = int( input() );


for i in range( K ):
    a, b = map( int, input().split() );
    ""
    a -= 1; b -= 1;
    
    print( int( dp[ a ][ b ] > 0 ) );
    
    