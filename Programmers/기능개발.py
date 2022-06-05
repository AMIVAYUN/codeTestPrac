# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:39:17 2022
@FileName: 기능개발.py
@author: YUNJUSEOK
@Link:
"""


def solution(progresses, speeds):
    answer = []
    from collections import deque;
    pdeq = deque( progresses );
    sdeq = deque( speeds );
    while pdeq:
        cnt = 0;
        if( pdeq[ 0 ] == 100 ):
            while( pdeq and pdeq[ 0 ] == 100 ):
                pdeq.popleft();
                sdeq.popleft();
                cnt += 1;
        if( cnt ):
            answer.append( cnt );
        pdeq = deque( [ pdeq[ i ] + sdeq[ i ] if pdeq[ i ] + sdeq[ i ] < 100 else 100 for i in range( len( pdeq ) ) ] );
       

solution( [93, 30, 55], 	[1, 30, 5]) ;