# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:21:10 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""

#WA AND TimeOut
'''
def solution(n, stations, w):
    answer = 0

    field = set( [ i for i in range( 1, n + 1 ) ] )
    
    for station in stations:
        tmp = set()
        for idx in range( station - w , station + w + 1 ):
            tmp.add( idx );
        field = field.difference( tmp );
    field = list( field );
    lengths = []
    start = 0;

    for idx in range( len( field ) ):
        if( idx == len( field ) - 1 ):
            lengths.append( idx - start + 1);
            continue
        if( field[ idx + 1 ] - field[ idx ]  != 1  ):
            lengths.append( idx - start + 1 );
            start = idx + 1;
    
    
    for leng in lengths:
        div,mod = divmod( leng, ( 2 * w + 1 ) );
        
        if( mod ):
            div += 1;
        
        answer += div;
    


    
        
    return answer
'''
def solution(n, stations, w):
    answer = 0;
    start = 1;
    lengths = [];
    
    for stat in stations:
        if( start <= stat - w - 1 ):
            
            lengths.append( [ start, stat - w - 1 ] );
        
        start = stat + w + 1;
    
    
    if( start <= n ):
        lengths.append( [ start, n ] );
    stan = 2*w + 1;
    
    for start, end in lengths:
        
        leng = end - start + 1;
        
        div,mod = divmod( leng, stan );
        
        if( mod ):
            div += 1;
        answer += div;


    
        
    return answer