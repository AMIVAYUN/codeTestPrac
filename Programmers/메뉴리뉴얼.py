# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 13:09:56 2022
@FileName: 메뉴 리뉴얼.py
@author: YUNJUSEOK
@Link:https://programmers.co.kr/learn/courses/30/lessons/72411
"""



solution( ["XYZ", "XWY", "WXA"] ,[2,3,4])

def getCourse( n, str0 ):
    import itertools;
    cmb = list(itertools.combinations( str0, n ) ) ;
    lst = [];
    
    for i in cmb:
        i = sorted( i );
        #조합에 문제가 안생기게 정렬
        str1 = ""
        for j in i:
            str1 += j;
        lst.append( str1 );
    
    
    return lst
def solution(orders, course):
    answer = []
    for i in course:
        dit = {};
        for j in orders:
            if( len( j ) >= ( i ) ):
                cmb = getCourse( i, j );
                for k in cmb:
                    if( k in dit ):
                        dit [ k ] += 1;
                    else:
                        dit [ k ] = 1;
        if (len( dit ) >= 1 ):
            mx = max( dit.values() );
            lst = [ i for i in dit if dit[ i ] == mx and dit[ i ] >= 2 ];
            answer += lst;
            
            
    
       
    return sorted( answer ) #결과도 정렬