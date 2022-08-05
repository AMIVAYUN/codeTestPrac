# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:41:22 2022
@FileName: .py
@author: YUNJUSEOK
@Link:
"""


N = int( input() );

lst = list( map( int, input().split() ) ) ;

srt = sorted( list( set( lst ) ) )

import bisect;


for i in lst:
    print( bisect.bisect_left( srt, i ), end = " " ) 