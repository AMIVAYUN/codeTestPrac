# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:00:20 2022

@author: 주석
"""

N = int( input() );

import itertools;

cmb = itertools.permutations( [ i + 1 for i in range( N )], N)


for case in sorted( list( cmb ) ):
    for item in case:
        print( item, end = " " );
        
    print()