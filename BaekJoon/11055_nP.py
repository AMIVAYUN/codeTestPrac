# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:29:58 2022
@FileName: 11055.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/11055
"""


n = int( input() );

num = list( map( int, input().split() ) );

dp = [ 0 ] * n;


sum0 = 0;

num_ = list( reversed( num ) );

sum0 += num_[ 0 ];
for i in range( 1, n ):
    if( num_[ i ] <= num_[ i - 1 ] ):
        sum0 += num_[ i ];
    else:
        if( sum0 <= num_[ i ] ):
            sum0 = num_[ i ];

print( sum0 )