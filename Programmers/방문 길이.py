# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:54:57 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(dirs):
    from collections import defaultdict;
    dit = {"U": ( -1, 0 ), "D": ( 1, 0 ) , "L": ( 0,-1), "R": ( 0, 1 ) }
    answer = 0
    N = 11;
    ddit = defaultdict( list );
    x, y = 0, 0;
    for dir in dirs:
        
        dx,dy = dit[ dir ];
        nx = x + dx;
        ny = y + dy;
        if( -6 < nx < 6 and -6 < ny < 6 ):
            if( ( x, y ) not in ddit[ ( nx, ny ) ] ):

                ddit[ ( nx, ny ) ].append( ( x, y ) );
                ddit[ ( x, y ) ].append( ( nx, ny ) )
                answer += 1;
            x = nx;
            y = ny;

    return answer