# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 15:27:48 2022

@author: 주석
"""

N = int( input() );

Mx = 50001;

lst = [ Mx ] * 100001;


for i in range( 1, N + 1 ):
    if( i % 5 == 0 ):
        lst[ i ] = min( lst[ i ], i // 5 );
    if( i % 2 == 0 ):
        lst[ i ] = min( lst [ i ] , i // 2 );
     
    lst[ i ] = min( lst[ i ], lst[ i - 2 ] + 1, lst[ i - 5 ] + 1 )

print( lst[ N ] if lst[ N ] != Mx else -1 )
    

    
