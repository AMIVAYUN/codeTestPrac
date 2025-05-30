# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:09:09 2022
@FileName: 거리두기 확인하기.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/81302#
"""





dx1 = [ 0, 0, 1, -1 ]
dy1 = [ -1, 1, 0, 0 ]

dx2 = [ 0, 0, 2, -2 ]
dy2 = [ 2, -2, 0, 0 ]

dx3 = [ 1, 1, -1, -1 ]
dy3 = [ -1, 1, -1, 1 ]
# for (1 , 1)
def chk4way( place, x, y, pos ):
    for i in range( 4 ):
        nx = x + dx1[ i ];
        ny = y + dy1[ i ];
        if( 0<= nx < 5 and 0<= ny < 5 ):
            if( place[ ny ][ nx ] != 'X' and getDistance( ( nx, ny ), pos ) == 1):
                return False;
            
    return True    
    
    return True;
def chkMid( place, pos1, pos2 ):
    xm = ( abs( pos2[ 0 ] - pos1[ 0 ] ) ) // 2
    ym = ( abs( pos2[ 1 ] - pos1[ 1 ] ) ) // 2 
    
    dis1 = getDistance( (0,0), pos1 );
    dis2 = getDistance( (0,0), pos2 );
    if( dis1 > dis2 ):
        xp, yp = getMidpos( pos2[ 0 ], pos2[ 1 ], xm, ym )
    else:

        xp, yp = getMidpos( pos1[ 0 ], pos1[ 1 ], xm, ym )
    
    
    if( place[ yp ][ xp ] != 'X' ):
        return False;
    return True;
        
def getMidpos( x, y ,xm, ym ):
    dit = { True: 1, False: -1}
    x +=  ( dit[ x >= 0 ] * xm )
    y += ( dit [ y >= 0 ] * ym )
    
    return x, y;    
#pos ==> ( x, y )
def chkPart( place, pos ):

    for i in range( 4 ):
        nx = pos[ 0 ] + dx1[ i ]
        ny = pos[ 1 ] + dy1[ i ]
        if( 0<= nx < 5 and 0<= ny < 5 ):
            
            if( place[ ny ][ nx ] == 'P' ):
                
                return False;
            
    

    
    for i in range( 4 ):
        nx = pos[ 0 ] + dx2[ i ];
        ny = pos[ 1 ] + dy2[ i ];
        if( 0<= nx < 5 and 0<= ny < 5 ):
            if( place[ ny ][ nx ] == 'P' ):
                if( not( chkMid( place, pos, ( nx, ny ) ) ) ):
                    
                    return False;
        
        
    for i in range( 4 ):
        nx = pos[ 0 ] + dx3[ i ];
        ny = pos[ 1 ] + dy3[ i ];
        
        if( 0<= nx < 5 and 0<= ny < 5 ):
            if( place[ ny ][ nx ] == 'P'):
                
                if( not( chk4way( place, nx, ny ,pos) ) ):
                    return False;
    
    return True;

        
                        
                                
                                
                    
                
                
    
                
                
                
                
    
def getDistance( a, b ):
    return abs( a[ 0 ] - b[ 0 ] ) + abs( a[ 1 ] - b[ 1 ] )

def solution(places):
    answer = []

    for i in places:
        lst = [];
        for y in range( 5 ):
            for x in range( 5 ):
                if( i[ y ][ x ] == 'P' ):
                    lst.append( chkPart( i,( x,y ) ) );
        
        answer.append( int( False not in lst ) );
                        
    
    return answer
