# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 19:59:31 2022

@author: 주석
"""

N = int ( input() );

lst = sorted( list( map( int, input().split() ) ) );
sum0 = 0;
rs = [];
for i in range(N ):
    sum0 += lst [ i ];
    rs.append( sum0 );
    
print( sum( rs ) );

