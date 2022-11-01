# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:12:00 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""
def isPalin( str0 ):
    leng = len( str0 );
    
    dp = [ [ 2 ] * ( leng ) for _ in range( leng ) ];

    for offset in range( leng  ):
        
        for x in range( leng - offset ):
            y = x + offset
            print( x, y )
            if( x == y ):
                dp[ x ][ y ] = 0;
            
            elif( x == y - 1 ):
                if( str0[ x ] == str0[ y ] ):
                    dp[ x ][ y ] = 0;
            
            else:
                if( str0[ x ] == str0[ y ] and str0[ x + 1 ][ y - 1 ] == 0 ):
                    dp[ x ][ y ] = 0;
    
    for row in dp:
        print( row )
                
def isPalindrome( str0 ):
    leng = len( str0 );
    
    for idx in range( leng // 2 ):
        if( str0[ idx ] != str0[ -1 * idx - 1] ):
            return False;
    return True;

    
    
n = int( input() );

for i in range( n ):
    str0 = input();
    if( isPalindrome( str0 ) ):
        print( 0 );
        continue;
        
        
    leng = len( str0 );
    for idx in range( leng ):
        tmp = str0[ :idx ] + str0[ idx + 1 : ];

        if( tmp[ 0 ] == tmp[ -1 ] ):
            if( isPalindrome( tmp ) ):
                print( 1 );
                break;
        
    else:
        print( 2 )
        
   