# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:24:39 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(k, dungeons):
    import itertools;
    Mx = 0;
    perm = list( itertools.permutations( dungeons, len( dungeons ) ) );
    
    for case in perm:
        start = 0;
        now = k;
        for dungeon in case:
            if( now < dungeon[ 0 ] ):
                break;
            now -= dungeon[ 1 ];
            start += 1;
        Mx = max( Mx, start );
    answer = Mx
    return answer