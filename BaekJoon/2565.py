# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 15:35:06 2022
@FileName: 2565.py
@author: YUNJUSEOK
@Link:https://www.acmicpc.net/problem/2565
"""


N = int( input() );

lst = [];
Mx = 0;
for i in range( N ):
    x, y = map( int, input().split() );
    lst.append( ( x, y ) );
    Mx = max( Mx, x, y );

    
dp = [ 0 ] * ( Mx + 2 );

lst = sorted( lst )

for i in range( 1, N + 1 ):
    start = lst[ i - 1 ][ 0 ];
    end = lst[ i - 1 ][ 1 ];
    
    standard = dp[ end - 1 ];
    
    
    for idx in range( end, Mx + 1):
        dp[ idx ] = max( dp[ idx ], standard + 1 );
    
   
    print( dp )
    
    

print( N - max( dp ) )
    
        