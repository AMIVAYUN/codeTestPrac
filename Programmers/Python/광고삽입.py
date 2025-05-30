# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 10:26:37 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def getSec( str0 ):
    hour, minute,sec = map( int, str0.split( ":" ) );
    
    return ( hour * 3600 ) + ( minute * 60 ) + sec;

def getStartandEnd( str0 ):
    start,end = str0.split( "-" );
    
    return getSec( start ), getSec( end );
'''
def solution(play_time, adv_time, logs):

    endp = getSec( play_time );
    answer = '';
    endp += 1;
    timeMapper = [ 0 ] * ( endp );
    
    enda = getSec( adv_time );
    
    Mx = 0;
    for log in logs:
        start,end = getStartandEnd( log );
        
        for i in range( start, end + 1 ):
            timeMapper[ i ] += 1;
            if( Mx < timeMapper[ i ] ):
                Mx = timeMapper[ i ];
    newMapper = timeMapper[:];
    # [ 1 2 3 ] => [ 1 3 6 ]
    for idx in range( 1, endp ):
        newMapper[ idx ] = newMapper[ idx ] + newMapper[ idx - 1 ];
        
    for idx in range( endp - enda ):

        if( Mx < newMapper[ idx + enda ] - newMapper[ idx - 1 ] ):
            Mx =  newMapper[ idx + enda ] - newMapper[ idx - 1 ]
            answer = idx;
    

    return answer
'''
def getSec( str0 ):
    hour, minute,sec = map( int, str0.split( ":" ) );
    
    return ( hour * 3600 ) + ( minute * 60 ) + sec;

def getStartandEnd( str0 ):
    start,end = str0.split( "-" );
    
    return getSec( start ), getSec( end );
def getTime( sec ):
    hour = sec // 3600;
    hourleft = sec % 3600;
    minute = hourleft // 60;
    minuteleft = hourleft % 60;
    second = minuteleft;
    hour = str( hour ).rjust( 2,'0' );
    minute = str( minute ).rjust( 2, '0' );
    second = str( second ).rjust( 2, '0' );
    return hour + ":" + minute + ":" + second;
def solution(play_time, adv_time, logs):
    '''
    1. 많이 겹치는 구간 
    2. 가장 빠른 시작시간
    '''
    #누적합2 => 4 7~ 14 16 17 23 TIME OUT 12 18 24 WA
    endp = getSec( play_time );
    answer = '';
    endp += 1;
    timeMapper = [ 0 ] * ( endp );
    
    enda = getSec( adv_time );
    
    Mx = 0;
    for log in logs:
        start,end = getStartandEnd( log );
        timeMapper[ start ] += 1;
        timeMapper[ end ] -= 1;

    #구간 갯수 정보
    for i in range( 1, endp ):
        timeMapper[ i ] = timeMapper[ i ] + timeMapper[ i - 1 ];
    # 누적합
    for i in range( 1, endp ):
        timeMapper[ i ] = timeMapper[ i ] + timeMapper[ i - 1 ];
        
    answer = getTime( 0 );
    if( endp - 1 <= enda ):
        return answer;
    
    for i in range( enda - 1, endp ):
        tg = timeMapper[ i ] - timeMapper[ i - enda ] if( i >= enda ) else timeMapper[ i ];
        if( Mx < tg ):
            Mx = tg;
            answer = getTime( i - enda + 1 );
    
    return answer
      
      
      
    
    # [ 1 2 3 ] => [ 1 3 6 ]
    '''
    #누적합 => 4 7~ 14 16 17 23 TIME OUT 12 18 24 31 WA
    newMapper = timeMapper[:];
    for idx in range( 1, endp ):
        newMapper[ idx ] = newMapper[ idx ] + newMapper[ idx - 1 ];
    if( endp - 1 == enda ):
        return getTime( 0 );
    for idx in range( 1, endp - enda ):
        if( Mx < newMapper[ idx + enda ] - newMapper[ idx - 1 ] ):
            Mx = newMapper[ idx + enda ] - newMapper[ idx - 1 ];
            answer = idx;
    return getTime( answer )
    '''


solution( "99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])