# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:58:56 2022
@FileName: 뉴스 클러스터링.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/17677
"""


'''
1:3 1:5 -- a and b min --> 3  a or b max 5

숫자 특수문자 공백 버림
대소문자 차이 무시

'''
def getDit( s ):
    dit = { chr( 65 + i ) for i in range( 26 ) }
    tdit = {};
    str0 = ""
    lst = [ s[ i ] + s[ i + 1 ] for i in range( len( s ) - 1 ) if s[ i ] in dit and s[ i + 1 ] in dit ]
    
    for i in lst:
        if( i in tdit ):
            tdit[ i ] +=1;
        else:
            tdit[ i ] = 1;
    
    return tdit;

def solution(str1, str2):
    val = 65536
    str1, str2 = str1.upper(), str2.upper();
    dit1 = getDit( str1 );
    dit2 = getDit( str2 );
    if( len( dit1 ) == len( dit2 ) == 0 ):
        return 1 * 65536;
    AUB = {}
    for i in dit1:
        if( i not in dit2 ):
            AUB[ i ] = dit1[ i ];
        else:
            AUB[ i ] = max( dit1[ i ], dit2[ i ] );
    for j in dit2:
        if( j not in dit1 ):
            AUB[ j ] = dit2[ j ];
    ANB= {};
    for i in dit1:
        if( i in dit2 ):
            ANB[ i ] = min( dit1[ i ], dit2[ i ] )
    
    
    
    
    answer = sum( ANB.values() ) / sum( AUB.values() ) 
    
    return int( answer * val )