# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 12:37:11 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N, S = map( int, input().split() );
lst = list( map( int, input().split() ) )
import itertools;
ans = 0;
for i in range( 1, N + 1 ):
    cmb = itertools.combinations(  lst , i );
    
    for case in cmb:
        if( sum( case ) == S ):
            ans += 1;
            
            
print( ans );