# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 21:29:58 2022

@author: 주석
"""

N, K = map( int, input().split() );

coins = [];

for i in range( N ):
    a = int( input() );
    
    if( a <= K ):
        coins.append( a ) ;
        

coins = sorted( coins, reverse = True );

cnt = 0;
for i in coins:
    cnt += K // i ;
    
    K = K % i;

print( cnt )

