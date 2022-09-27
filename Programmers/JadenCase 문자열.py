# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:17:50 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(s):
    answer = ''
    s = list( s );

    idx = 0;
    while idx < len( s ):
        if( s[ idx ] != " " ):
            s[ idx ] = s[ idx ].upper()
            idx += 1;
            while idx < len( s ) and s[ idx ] != " ":
                s[ idx ] = s[ idx ].lower()
                idx += 1;

        idx += 1;
        
    return ''.join( s )