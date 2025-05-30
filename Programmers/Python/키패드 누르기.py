# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:36:17 2022
@FileName: 키패드 누르기.py
@author: YUNJUSEOK

@Link: https://programmers.co.kr/learn/courses/30/lessons/67256
"""
def process( numbers , hand ):
    ditL = { 1: 'L' ,4: 'L', 7: 'L' }
    ditR = { 3: 'R', 6:'R', 9 : 'R'  }
    dit2 = { 1: ( 0, 0 ), 2: ( 0, 1 ), 3: ( 0, 2 ), 4: ( 1, 0 ), 5:( 1, 1 ), 6:( 1, 2 ), 7:( 2, 0), 8:( 2, 1 ), 9: ( 2, 2 ), '*': ( 3, 0 ), 0: ( 3, 1 ), '#': ( 3,2 ) }
    result = [];
    posL, posR = dit2['*'],dit2['#']
    for i in numbers:
        if( i in ditL ):
            result.append( ditL[ i ] );
            posL = dit2[ i ];
        elif( i in ditR ):
            result.append( ditR[ i ] );
            posR = dit2[ i ] ;
            
        else:
            disL = abs( dit2[ i ][0] - posL[0]  ) + abs ( dit2[ i ][ 1 ] - posL[ 1 ] ) 
            disR = abs( dit2[ i ][0] - posR[0] ) + abs ( dit2[ i ][ 1 ] - posR[ 1 ] ) 
            if( disL > disR ):
                posR = dit2[ i ];
                result.append( "R" );
            elif( disL < disR ):
                posL = dit2[ i ];
                result.append( "L" );
            else:
                if( hand == 'right' ):
                    posR = dit2[ i ];
                    result.append( "R" );
                else:
                    posL = dit2[ i ];
                    result.append( "L" );
    
    return result;
                      
                       
            
def solution(numbers, hand):    
    
    
    str0 = process( numbers, hand );
    answer = '';
    for i in str0:
        answer += i;
    return answer

