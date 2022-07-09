# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:24:59 2022

@author: 주석
"""

import sys;
N , M = map( int, input().split() ) ;

k1 = set();
k2 = set();
for i in range( N ):
    k1.add( input() );
    

for i in range( M ):
    k2.add( input() );
    
rs = sorted( list( k1 & k2 ) ) 

print( len( rs ) )
for i in rs:
    print( i )