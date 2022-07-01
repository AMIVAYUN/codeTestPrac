# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 17:09:59 2022

@author: 주석\
    
    chk


8

110 150 74 112 54 144 56 112

480
61


6

77 89 61 118 91 142

120
20

"""

N = int( input() );

num = list( map( int, input().split() ) );

M = int( input() );
lt = 0; rt = max( num );


while lt<=rt:
    mid = ( lt + rt ) >> 1;
    sum0 = 0;
    for i in num:
        sum0 += i if i < mid else mid;
    
    if( M < sum0 ):
        rt = mid - 1;

    else:
        lt = mid + 1;
            

print( rt );
    