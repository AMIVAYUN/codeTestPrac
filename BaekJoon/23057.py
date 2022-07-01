# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 19:37:40 2022
@FileName: 23057.py
@author: YUNJUSEOK
@Link:
"""

import itertools;

comb = itertools.combinations;

N = int( input() ); 

num = list( map( int, input().split() ) ) ;

sum0 = sum( num );

rs = set();
cnt = 0;
for i in range( 1, N + 1 ):
    for j in comb( num, i ):
        
        rs.add( sum( j ) );


print( sum0 - len( rs ) );
    
