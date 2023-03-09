# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:08:45 2023
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(book_time):
    '''
    answer = 0;
    rooms = [];
    book_time_ref = [ ( int( i[ 1 ][ : 2 ] ) - int( i[ 0 ] [ : 2 ] ) ) * 60 + 
                     ( int( i[ 1 ][ 3: ] ) - int( i[ 0 ][ 3: ] ) ) for i in book_time ]
    
    new_b = list( reversed( sorted ( [ book_time[ i ] + [ book_time_ref[ i ] ] for i in range( len( book_time ) ) ] ) ) );
    
    for reserve in new_b:
        if( answer == 0 ):
            rooms.append( reserve[ 2 ] );
            answer += 1;
                
    '''   
    
    intbook_time = [ [ int( i[ 0 ][ :2 ] ) * 60 + int( i[ 0 ][ 3: ] ),  int( i[ 1 ][ :2 ] ) * 60 + int( i[ 1 ][ 3: ] ) ] for i in book_time ]
    answer = [];
    intbook_time = list( sorted( intbook_time, key = lambda x: ( x[ 0 ], x[ 1 ] ) ) );
    
    for start,end in intbook_time:
        if( len( answer ) == 0 ):
            answer.append( end );
            continue;
        cond = True; #갱신 확인;
        for i in range( len( answer ) ):
            if( answer[ i ] + 10 <= start ):
                answer[ i ] = end;
                cond = False; # 갱신
                break;
        
        if( cond ):
            answer.append( end );
        
        answer = list( sorted( answer ) ); 
    
    return len( answer );


solution( [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]] )