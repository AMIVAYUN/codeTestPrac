# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 13:04:38 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


def solution(word):
    import itertools;
    lst = [];
    for i in range( 1, 6 ):
        
        comb = itertools.product( ["A","E","I","O","U"] , repeat= i )
        
        lst = lst + list( comb );
    dit = {};
    idx = 1;
    for wd in sorted( lst ):
        dit[ ''.join( wd ) ] = idx;
        idx += 1
    return dit[ word ] 