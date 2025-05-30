# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 11:04:47 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(m, musicinfos):
    lenm = len( m );
    dit = {};
    cnt = 0;
    import re;
    for music in musicinfos:
        start,end,name,code = music.split( ',' );

        startH, startS = start.split( ":" );
        
        endH,endS = end.split( ":" );
        
        timeH = int( endH ) - int( startH );
        timeS = int( endS ) - int( startS );
        
        if( timeS < 0 ):
            timeH -= 1;
            timeS += 60;
        
        timeS += 60 * timeH;
        shopcnt = code.count("#")
        code = code[ :timeS + shopcnt ]
        codelst = [];
        
        idx = 0;
        #코드 저장
        while idx < len( code ):
            if( idx + 1 < len( code ) and code[ idx + 1 ] == '#' ):
                codelst.append( code[ idx: idx + 2 ] );
                idx += 2;
            else:
                codelst.append( code[ idx ] );
                idx += 1;
                
        mlst = []
        idx = 0;
        while idx < len( m ):
            if( idx + 1 < len( m ) and m[ idx + 1 ] == '#' ):
                mlst.append( m[ idx: idx + 2 ] );
                idx += 2;
            else:
                mlst.append( m[ idx ] );
                idx += 1;
                
        idx = 0;
        codelst = codelst * len( m );
        

        for i in range( len( codelst ) - len( mlst ) ):

            if( codelst[ i : i + len( mlst ) ] == mlst ):
                dit[ name ] = ( timeS, cnt );
                break;
            
                    

        cnt += 1;
    
    lst = list( sorted( dit.items(), key = lambda x: ( -x[ 1 ][ 0 ], x[ 1 ][ 1 ] ) ) );

    answer = lst[ 0 ][ 0 ] if( len( lst ) ) else "(None)";
    
    return answer;