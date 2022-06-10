# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 15:21:40 2022
@FileName: 튜플.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/64065
"""


def solution(s):
    import re;
    s = s [ 1: len( s ) - 1 ];
    lst = []; str0 = "";
    for i in range( len( s ) ):
        if( s[ i ] == '{' ):
            i+= 1
            while( s[ i ] != '}'):
                
                str0 += s[ i ]
                i+= 1;
                
            lst.append( [ int( i ) for i in (str0.split(",") ) ] );
            str0 = ""
    
    lst = sorted( lst, key = lambda x: len( x ) );
    dit = {};
    idx = 0;
    for i in lst:
        for j in i:
            if j not in dit:
                dit[ j ] = len( dit );
    
    srt = sorted( dit.items(), key= lambda x: x[ 1 ] )
    answer = []
    for i in srt:
        answer.append( i[0] );
        
        
        
            
        
    
    
    
    
    
    return answer