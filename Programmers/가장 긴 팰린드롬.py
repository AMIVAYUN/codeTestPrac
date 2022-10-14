# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 20:41:42 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(s):
    answer = 0

    leng = len( s );
    
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
                print( ( x, x + offset ), ( x + 1 , x + offset - 1 ), x, offset )
                if( x + offset -1 >= 0 and dp[ x + 1 ][ x + offset - 1 ] > 0 and s[ x + offset ] == s[ x ] ):
                    dp[ x ][ x + offset ] = dp[ x + 1 ][ x + offset - 1 ] + 2;
                
    Mx = 0;
    for row in dp:
        print( row )
        Mx = max( max( row ), Mx );
            
        
    return Mx

solution( "abcdcba" )