# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 20:46:04 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(a):
    answer = -1
    lena = len( a )
    dit = {};
    if( lena < 4 ):
        return 0;
    for i in range( lena ):
        if( a[ i ] in dit ):
            dit[ a[ i ] ] += 1;
        else:
            dit[ a[ i ] ] = 1;
            
    for i in dit:
        if( dit[ i ] >= answer ):
            cnt = 0;
            idx = 0;
            
            while idx < lena - 1:
                if( ( a[ idx ] == i or a[ idx + 1 ] == i ) and a[ idx ] != a[ idx + 1 ]):
                    cnt +=1
                    idx += 2;
                else:
                    idx += 1;
            print( i, cnt )
            answer = max( answer, cnt );
    return answer * 2





a = solution([2, 3, 4, 1, 1, 1, 1, 5, 6, 7] )

print( a )