# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:10:25 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution( numbers ):
    answer = [];
    for number in numbers:
        if( number % 4 == 3 ):
            bi = [ '0' ] + list( bin( number )[ 2: ] )
            
            for i in range( len( bi ) - 1, -1 , -1):
                if( bi[ i ] == '0' ):
                    bi[ i ] = '1'
                    bi[ i + 1 ] = '0'
                    
                    break;

            str0 = ''.join( bi );
 
            answer.append( int( str0 , 2 ) ); 
            
        else:
            answer.append( number + 1 );
    return answer;

solution( [2, 7 ])